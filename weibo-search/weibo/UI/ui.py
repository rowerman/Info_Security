import tkinter as tk
from tkinter import messagebox
import importlib
import sys
import re

from weibo import settings

# Import settings module
sys.path.insert(0, '../settings.py')  # replace with the path to your settings.py

def save_settings():
    with open('../settings.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('../settings.py', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith('DOWNLOAD_DELAY'):
                f.write('DOWNLOAD_DELAY = {}\n'.format(entry1.get()))
            elif line.startswith('KEYWORD_LIST'):
                cookie = '    \'cookie\': \'{}\''.format(entry2.get())
                f.write(line.replace('    \'cookie\': \'PC_TOKEN=67bb3d0d4e; login_sid_t=e543e272edcee7d8227260f2cffb83ee; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=2846898638827.7886.1702883046242; SINAGLOBAL=2846898638827.7886.1702883046242; ULV=1702883046244:1:1:1:2846898638827.7886.1702883046242:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFik.OrxkOD-XU2KCZ9GUY.5JpX5o275NHD95QcSKBRS0M7eon7Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo-X1hMNehzRe5tt; SSOLoginState=1702883076; SUB=_2A25Ie59VDeRhGeBL71oW9y7OwzyIHXVr-J6drDV8PUNbmtANLVj5kW9NRxyi9I0zrEio6OnBxCh5b2j37yPD8oza; ALF=1734419076\'',cookie))
            else:
                f.write(line)

    messagebox.showinfo("Info", "Settings saved")

root = tk.Tk()
root.title("Settings")
root.geometry("900x500")


label1 = tk.Label(root, text="DOWNLOAD_DELAY")
label1.pack()
entry1 = tk.Entry(root)
entry1.insert(0, settings.DOWNLOAD_DELAY)  # Set the default value
entry1.pack()

label2 = tk.Label(root, text="cookie")
label2.pack()
entry2 = tk.Entry(root)
entry2.insert(0, settings.DEFAULT_REQUEST_HEADERS['cookie'])  # Set the default value
entry2.pack()

button = tk.Button(root, text="Save", command=save_settings)
button.pack()

root.mainloop()
