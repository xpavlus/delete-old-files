#! /usr/bin/env python
import glob
import os
from datetime import datetime
from optparse import OptionParser
from os.path import normpath, isfile, isdir
from shutil import rmtree

op = OptionParser()
op.add_option("-d", dest="dir",
              help="Directory to clean old files", metavar="DIR")
op.add_option("-a", dest="file_age", default=14, type="int",
              help="How old file should be")

(option, args) = op.parse_args()

dir_path = option.dir
days_to_keep = option.file_age

for file in [normpath(f) for f in os.listdir(dir_path)]:
    file_path = os.path.join(dir_path, file)
    file_age = datetime.now() - datetime.fromtimestamp(os.stat(file_path).st_mtime)
    if file_age.days > days_to_keep:
        if isfile(file_path):
            os.unlink(file_path)
        elif isdir(file_path):
            rmtree(file_path)
        else:
            pass
