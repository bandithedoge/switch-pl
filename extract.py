# This is the extraction script for Nintendo Switch translation files, written by bandithedoge for the switch-pl project. It saves about 10-20 minutes of otherwise incredibly tedious work involving manually moving 20+ files to a bunch of different directories.

import os
import re
import libyaz0

key_file = "~/.switch/prod.keys"
hactool = "hactool -k " + key_file + " --disablekeywarns "

nca_dir = "nca/"
nsp_dir = "nsp/"
romfs_dir = "romfs/"
msbt_dir = "msbt/"
message_dir = romfs_dir + "message/EUen/"

nsp_command = hactool + "--intype=pfs0 --pfs0dir=" + nca_dir + " -x "
nca_command = hactool + "--romfsdir=" + romfs_dir + " "

for title in os.listdir(nsp_dir):
    print("\nExtracting " + title)
    os.system(nsp_command + nsp_dir + title + "/00")

for nca in os.listdir(nca_dir):
    print("\n Extracting " + nca)
    os.system(nca_command + nca_dir + nca)

for msbt in os.listdir(message_dir):
    if msbt.endswith(".szs") or msbt.endswith(".msbt"):
        msbt_name = re.sub("\.szs$", "", msbt)
        with open(message_dir + msbt, "rb") as input, open(msbt_dir + msbt_name, "wb") as output:
            if msbt.endswith(".szs"):
                decompressed = libyaz0.decompress(input.read())
            else:
                decompressed = input.read()
            output.write(decompressed)
