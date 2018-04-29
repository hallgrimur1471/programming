#!/usr/bin/env python3

"""
spylint: Svarmi's pylint wrapper
"""

import argparse
from os import path
from os.path import abspath
from glob import iglob
from subprocess import PIPE

from svarmi.utils import error, bash_command

def join(a, b):
    """
    Handy wrapper to join paths
    """
    return abspath(path.join(a, b))

parser = argparse.ArgumentParser()
parser.description = (
    "Watches FILE for changes and lints it's "
    "code when changes are detected. if --lines LINES is specified: "
    "only outputs LINES number of lines from pylint's analysis, instead of "
    "the default which is 66"
)
parser.add_argument(
    "files_or_directories", metavar="FILE", nargs='+',
    help="file or directory to watch changes in. "
         "Recursively lints .py files if directory specified"
)
parser.add_argument(
    "--lines", type=int,
    help="number of lines to output"
)
args = parser.parse_args()

# setup
home_dir = path.expanduser("~")
pylintrc_file = join(home_dir, ".pylintrc2")
pylint_write_file = join(home_dir, ".pylint.d/pylint_last_analysis")

# find all files we need to lint, some arguments might be directories
files = [] # files to lint
for file_or_dir in map(abspath, args.files_or_directories):
    if path.isfile(file_or_dir):
        files.append(file_or_dir)
    elif path.isdir(file_or_dir):
        for file_ in iglob(join(file_or_dir, '**/*.py')):
            files.append(file_)
    else:
        error("unrecognized file:", file_or_dir)

# analyse all files
results = ""
for file_ in files:
    print("analysing {} ...".format(file_))
    result = bash_command("pylint --rcfile={} {}".format(pylintrc_file, file_),
                          stdout=PIPE)
    results += result.stdout.decode()

# print analyse results
bash_command("clear")
lines = results.split('\n')
if args.lines:
    total_lines = args.lines
else:
    total_lines = 66
for i in range(min(total_lines, len(lines))):
    print(lines[i])
