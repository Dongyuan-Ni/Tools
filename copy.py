import os
import shutil

def copytree(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        if os.path.isdir(s):
            copytree(s, d)
        else:
            if os.path.getsize(s) <= 50000:
                shutil.copy2(s, d)
                print(s)


src_dir = '/dest-dir/ALLDATA'
dst_dir = '/dest-dir/ALLDATA2'

copytree(src_dir, dst_dir)
