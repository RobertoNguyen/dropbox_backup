#!
# Dropbox automatic backup script
#

import os, shutil, send2trash, sys, distutils.dir_util, time

def dbBackup():

    start = time.time()

    # Change directory to source folder
    source_dir = os.chdir(r'D:\Dropbox\Dropbox\Camera Uploads')
    destination_dir = (r'D:\My Pictures\Camera Roll\dropbox')
    print('Directory changed to', os.getcwd())

    # Another method to copy, except copies entire tree vs. file by file.
    #distutils.dir_util.copy_tree(r'D:\Dropbox\Dropbox\Camera Uploads',
    #                             r'D:\My Pictures\Camera Roll\dropbox')

    # Creates a new directory if destination directory not found.
    if os.path.exists(destination_dir) == False:
        os.mkdir(destination_dir)
        print('Directory created')

    # Files that will not be copied nor deleted
    exclude = [
        '.dropbox',
        'desktop.ini'
        ]

    # Loops through source directory and copy+delete each picture
    pics = 0
    vids = 0
    others = 0

    for item in os.listdir(source_dir):
        if item not in exclude:
            shutil.copy(item, r'D:\My Pictures\Camera Roll\dropbox')
            if '.jpg' or '.png' in item:
                pics += 1
            elif '.mp4' in item:
                vids += 1
            else:
                others += 1

            send2trash.send2trash(item)
            print(item + ': moved and deleted')

    total = pics + vids + others

    end = time.time()
    print('Backup is complete. It took %s seconds' % round(end - start, 4))
    print('Total items copied: %s | Photos: %s Videos: %s Others: %s' % (total, pics, vids, others))

if __name__ == "__main__":
    dbBackup()
