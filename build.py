# This is the build script for Nintendo Switch translation files, written by bandithedoge for the switch-pl project. It saves about 10-20 minutes of otherwise incredibly tedious work involving manually moving 20+ files to a bunch of different directories.
# The script requires that all MSBT files in "msbt/" follow the <name>.msbt format, which is ensured by the SZS extraction script (WIP)
# The resulting "contents" directory can theoretically be copied to the SD card and used.

import os
import libyaz0

# titles that contain MSBT text files packed in .szs
files_szs = {
        "010000000000080B": ["localNews"],
        "0100000000001000": ["flaunch", "gift", "interrupt", "migration", "notification", "option", "qlaunch", "common", "setting", "dataErase"],
        "0100000000001001": ["auth", "common"],
        "0100000000001002": ["cabinet", "common"],
        "0100000000001003": ["controller", "button", "common"],
        "0100000000001004": ["dataErase", "common"],
        "0100000000001005": ["error", "common"],
        "0100000000001006": ["netConnect", "common"],
        "0100000000001007": ["playerSelect", "common"],
        "0100000000001008": ["swkbd", "common"],
        "0100000000001012": ["starter", "common", "setting"],
        "0100000000001013": ["myPage", "common", "setting"],
        "0100000000001015": ["maintenance", "common", "setting"],
        "010000000000100C": ["overlayDisp", "common"],
        "010000000000100D": ["photoViewer", "common"]
        }

# titles that contain uncompressed MSBT files
files_msbt = {
        "0100000000000803": ["Cruiser"],
        "0100000000001009": ["MiiEditN"]
        }

# create a list of all files
files = []
for title in files_szs:
    for file in files_szs[title]:
        files.append(file)

# convert the list of files to a dictionary and back to a list in order to get rid of duplicates
files_list = list(dict.fromkeys(files))

folders = {
        "msbt": "msbt/",
        "szs": "szs/",
        "contents": "atmosphere/contents/"
        }

for folder in folders:
    if not os.path.exists(folders[folder]):
        os.makedirs(folders[folder])

# compress the files and output to "szs/"
for file in files_list:
    print("Compressing " + file)
    msbt_file = file + ".msbt"
    szs_file = file + ".msbt.szs"
    with open(folders["msbt"] + msbt_file, "rb") as szs, open(folders["szs"] + szs_file, "wb+") as out:
        compressed = libyaz0.compress(szs.read(), 0, 9)
        out.write(compressed)

# copy both the compressed szs and uncompressed msbt files to the correct path for layeredfs
for title in files_szs:
    output = folders["contents"] + title + "/romfs/message/EUen/"
    if not os.path.exists(output):
        os.makedirs(output)

    for file in files_szs[title]:

        szs_file = file + ".msbt.szs"
        szs_in = folders["szs"] + szs_file
        szs_out = output + szs_file

        with open(szs_out, "wb+") as lfs_out, open(szs_in, "rb") as lfs_in:
            print("Copying " + szs_in + " to " + szs_out)
            lfs_out.write(lfs_in.read())

for title in files_msbt:
    output = folders["contents"] + title + "/romfs/message/EUen/"
    if not os.path.exists(output):
        os.makedirs(output)

    for file in files_msbt[title]:
        msbt_file = file + ".msbt"
        msbt_in = folders["msbt"] + msbt_file
        msbt_out = output + msbt_file

        with open(msbt_out, "wb") as lfs_out, open(msbt_in, "rb") as lfs_in:
            print("Copying " + msbt_in + " to " + msbt_out)
            lfs_out.write(lfs_in.read())
