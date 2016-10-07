#!/usr/bin/env python3
from zipfile import *


def getFiles():
    files = []
    print("=========================")
    print("What files will be used?")
    print("Press enter to finish...")
    print("=========================")
    filename = input(">>")
    while filename != "":
        files.append(filename)
        filename = input(">>")
    print("========================")
    print("Files to add to archive:")
    print("========================")
    for fname in files:
        print(fname)
    cont = input("Is this correct?[Y/n]")
    if cont == 'Y' or cont == 'y' or cont == '':
        return files
    else:
        return getFiles()

def createZipArchive(files):
    print('\n')
    name = input("Filename (no extension): ")
    if name == '':
        createZipArchive(files)
    name += '.zip'
    print("========================")
    print("Creating archive", name, "...")
    print("========================")
    with ZipFile(name, 'w') as zname:
        for f in files:
            zname.write(f)
def main():
    createZipArchive(getFiles())
    print("\nFinished!")

if __name__ == '__main__':
    main()
