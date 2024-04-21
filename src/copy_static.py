import shutil, os


def copy_static(source, destination):
    if not os.path.exists(destination):
        print(f"Creating: {destination}")
        os.mkdir(destination)

    dir_items = os.listdir(source)

    for item in dir_items:
        fp = os.path.join(source, item)
        dp = os.path.join(destination, item)

        if os.path.isdir(fp):
            copy_static(fp, dp)
        else:
            print(f"Copying {fp}")
            shutil.copy(fp, dp)
