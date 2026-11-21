import os
import shutil

def copy_static(static_dir, copy_dir="./public"):
    if os.path.exists(copy_dir):
        shutil.rmtree(copy_dir)

    os.mkdir(copy_dir)

    copy_files(static_dir, copy_dir)

def copy_files(static_dir, copy_dir):

    for item in os.listdir(static_dir):
        new_path = os.path.join(static_dir, item)
        new_copy_dir = os.path.join(copy_dir, item)

        if os.path.isdir(new_path):
            os.mkdir(new_copy_dir)
            copy_files(new_path, new_copy_dir)

        elif os.path.isfile(new_path):
            shutil.copy(new_path, new_copy_dir)
