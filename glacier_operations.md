##########################
# AWS Glacier operations #
##########################

## Installing the required stuff

```
$ sudo -H python3 -m pip install glacier_upload==1.2 # https://github.com/tbumi/glacier-upload
$ sudo -H python3 -m pip install --upgrade awscli
$ aws configure
```

## Compressing a directory

```
$ dir_to_compress="some_directory"; nohup bash -c "tar -c ${dir_to_compress} | pv --numeric --timer -s $(du -sb ./${dir_to_compress} | awk '{print $1}') | gzip --verbose --best > ${dir_to_compress}.tar.gz" 1>${dir_to_compress}_compression_progress.log 2>&1 &
# (The `du` command for `pv` might take a long time in the beginning
# while nothing will be written to progress output!)
```

### View compression progress

```
$ dir_being_compressed="some_directory"; watch -n 1 "ls -lash | grep ${dir_being_compressed}; echo; tail ${dir_being_compressed}_compression_progress.log"
```

## Uploading an archive

```
$ file_to_upload="some_directory.tar.gz"; archive_description="Nydus linux partition snapshot from 30 Apr 2018"; nohup stdbuf -oL glacier_upload --vault-name xelnaga --file-name ${file_to_upload} --arc-desc "${archive_description}" --num-threads 1 --part-size 128 > ${file_to_upload%.*.*}_upload_progress.log &
```

## View upload progress

```
$ file_being_uploaded="some_directory.tar.gz"; tail -f ${file_being_uploaded%.*.*}_upload_progress.log
```

## Sending a job request to download an archive

```
$ archive_id="KJklhlpR9Tk1QN9DWxMsHsRaIxdalkjee9-EklSffI__HQaXsS1aZzr6PiJ0Hwf9NiEp3IkjodtlxTjvYy8KldbN-vnidbEFt6GOCteDlH5BTI8vzHbtJb43riRiZF_26PA"; job_description="Retrieve archive on $(date +%F) $(date +%T)"; aws glacier initiate-job --account-id - --vault-name xelnaga --job-parameters "{\"Type\": \"archive-retrieval\", \"ArchiveId\": \"${archive_id}\", \"Description\": \"${job_description}\", \"Tier\": \"Bulk\"}"
```

## Downloading the archive

```
$ file_name="some_directory.tar.gz"; job_id="oexIrYJXoJJmBRyKgUlnY8OaxtDTxKCaNn_u24px8qLzoC2wLIi74rEsDFovP72xhfbpJoHoa1XSTZjv1"; nohup aws glacier get-job-output --account-id - --vault-name xelnaga --job-id "${job_id}" ${file_name} > ${file_name%.*.*}_download.log &
```

## View download progress

```
$ file_being_downloaded="some_directory.tar.gz"; watch -n 1 "ls -lash | grep ${file_being_downloaded}"
```

## Decompressing the archive

```
$ file_to_decompress="some_directory.tar.gz"; nohup bash -c "cat ${file_to_decompress} | gzip -d | pv --numeric --timer -s $(ls -al ${file_to_decompress} | awk '{print $5}') | tar x" 1>${file_to_decompress%.*.*}_decompression_progress.log 2>&1 &
```

## View decompression status

```
$ file_being_decompressed="nydus_ubuntu16.tar.gz"; watch -n 1 "ls -lash | grep ${file_being_u
ncompressed%.*.*}; echo; tail ${file_being_decompressed%.*.*}_decompression_progress.log"
```

## List archives in vault

```
aws glacier initiate-job --account-id - --vault-name xelnaga --job-parameters '{"Type": "inventory-retrieval"}'

# read job-id from output and replace in next command:

aws glacier get-job-output --account-id - --vault-name xelnaga --job-id 'DioUrZvyOyE07g_QeyblZuDnM3_XLw2JneifktG9iKDs57vasdfUF2LbnFc6VPU1r3khsiUleHvxsU3IR67FJFfpP1-RX' vault_inventory.json
```