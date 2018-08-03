#!/usr/bin/env bash

# rsync A B
#
# This is an experiment to try to use rsync to make two folders identical.
# So if there is extra stuff in B it should be deleted when A is synced into it
#
# This test has symlinks, binaries, text files and directories

# replace a string in file
replace() {
  local file="$1"
  local old_string="$2"
  local new_string="$3"

  cat "$file" \
      | sed 's,'"${old_string}"','"${new_string}"',g' \
      | sudo tee "$file" > /dev/null
}

# cd to directory of this script
cd $(dirname $(readlink -f "$0"))

# generate a large file (246 MB)
if [[ ! -f A/large_file ]]; then
  echo "Generating a large (246 MB) file ..."
  ./generate_large_output.py > A/large_file
fi

# make backup
rm -rf .A.backup
cp -r A .A.backup

# make B identical to A
rm -rf B
cp -ra A B

# now let's make some changes to A ...

# remove:
rm A/dir1/RsyncFeedback.l # broken symlink
rm -d A/empty_dir1 # empty directory
rm A/socket_client.py # text file

# modify:
replace "A/socket_server.py" "main" "adalstuffid"
# let's even modify this binary file
replace "A/a.out" "GLIBC_2.2.5" "GLIBC_2.2.4" # hehe

# add:
touch A/file2.txt
echo "hi" > A/file2.txt
ln -s A/file2.txt A/real_symlink2

# let's take a look a the sizes of A and B:
echo "A size: `du -bc A | tail -1 | awk '{print $1}'`"
echo "B size: `du -bc B | tail -1 | awk '{print $1}'`"

# now let's try to diff
printf "\nrsync:"
rsync -rlptD --delete --info=STATS A/ B

# now let's check the difference
printf "\nDiff:\n"
diff -r A B 2>/dev/null

# revert back to original state
rm -rf A
cp -r .A.backup A
