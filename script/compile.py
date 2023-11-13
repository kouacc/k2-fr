import os
import tarfile
import glob
import subprocess

os.chdir("YK2")
trads=glob.glob('*.json')
for json in trads:
    subprocess.run(['../reARMP', json])
    os.remove(json)
binaires=glob.glob('*.bin')
for bins in binaires:
  os.rename(bins,bins[:-9])
fichiers=glob.glob('*.bin')
