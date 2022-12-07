import os
import glob
import img2pdf
from natsort import natsorted
from tkinter import filedialog

dir = 'ダイアログが表示された時に初めのパスを指定する'
fld = filedialog.askdirectory(initialdir = dir)

os.chdir(fld)
cur_dir = os.getcwd()
dirs = os.listdir(cur_dir)

if dirs:
    types_0 = ("jpg", "png", "jpeg","JPG","JPEG","PNG")
    files_0 = []
    for j in types_0:
        files_0 += glob.glob(os.path.join(cur_dir,r"*."+j))
        new_filelist_0 = natsorted(files_0)
        if new_filelist_0:
            with open(os.path.join(cur_dir, f"{cur_dir}.pdf"), "wb") as f0:
                f0.write(img2pdf.convert([file  for file in new_filelist_0]))
                new_filelist_0.clear()
for f in dirs:
    if os.path.isdir(os.path.join(cur_dir, f)):
        for sf in os.listdir(os.path.join(cur_dir,f)):
            if os.path.isdir(os.path.join(cur_dir, f, sf)):
                types_1 = ("jpg", "png", "jpeg","JPG","JPEG","PNG")
                files_1 = []
                for t in types_1:
                    files_1 += glob.glob(os.path.join(cur_dir, f, sf, r"*."+t))
                    new_filelist_1 = natsorted(files_1)
                    if new_filelist_1:
                        with open(os.path.join(cur_dir, f, sf, f"{sf}.pdf"), "wb") as f1:
                            f1.write(img2pdf.convert([file  for file in new_filelist_1]))
                            new_filelist_1.clear()
        types_2 =  ("jpg", "png", "jpeg","JPG","JPEG","PNG")
        files_2 = []
        for i in types_2:
            files_2 += glob.glob(os.path.join(cur_dir, f, r"*."+i))
            new_filelist_2 = natsorted(files_2)
            if new_filelist_2:
                with open(os.path.join(cur_dir, f, f"{f}.pdf"), "wb") as f2:
                    f2.write(img2pdf.convert([file for file in new_filelist_2]))
                    new_filelist_2.clear()
