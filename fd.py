import os
import zipfile
import shutil
import datetime
import sys
arg = sys.argv


def decorator(file, dest, keyword):
    def caller(function):
        def wrap():
            function(file, dest, keyword)
        return wrap()
    return caller

@decorator(arg[2], arg[3], arg[1])
def rename_a_file(file, dest, keyword):
    if keyword == "rename":
        os.rename(file, dest)
        
@decorator(arg[2], arg[3], arg[1])
def copy_file(file, dest, keyword):
    if keyword == "copy":
        shutil.copy(file, dest)

@decorator(arg[2], arg[3], arg[1])
def move_file(file, dest, keyword):
    if keyword == "move":
        shutil.move(file, dest)



