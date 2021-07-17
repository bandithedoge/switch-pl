# This is the extraction script for Nintendo Switch translation files, written by bandithedoge for the switch-pl project. It saves about 10-20 minutes of otherwise incredibly tedious work involving manually moving 20+ files to a bunch of different directories.

import os
import re
import libyaz0

key_file = "~/.switch/prod.keys"
hactool = "hactool -k " + key_file + " --disablekeywarns "

folders = {
        "nca": "nca/",
        "nsp": "nsp/",
        "romfs": "romfs/",
        "msbt": "msbt/",
        "message": "romfs/message/EUen/"
        }

for folder in folders:
    if not os.path.exists(folders[folder]):
        os.makedirs(folders[folder])

nsp_command = hactool + "--intype=pfs0 --pfs0dir=" + folders["nca"] + " -x "
nca_command = hactool + "--romfsdir=" + folders["romfs"] + " "

for title in os.listdir(folders["nsp"]):
    print("\nExtracting " + title)
    os.system(nsp_command + folders["nsp"] + title + "/00")

for nca in os.listdir(folders["nca"]):
    print("\n Extracting " + nca)
    os.system(nca_command + folders["nca"] + nca)

for msbt in os.listdir(folders["message"]):
    if msbt.endswith(".szs") or msbt.endswith(".msbt"):
        msbt_name = re.sub("\.szs$", "", msbt)
        with open(folders["message"] + msbt, "rb") as input, open(folders["msbt"] + msbt_name, "wb") as output:
            if msbt.endswith(".szs"):
                decompressed = libyaz0.decompress(input.read())
            else:
                decompressed = input.read()
            output.write(decompressed)
