import tkinter as tk
from tkinter import messagebox, font
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
            if 'DOWNLOAD_DELAY' in line:
                line = 'DOWNLOAD_DELAY = {}\n'.format(DOWNLOAD_DELAY.get())
            elif 'DEFAULT_REQUEST_HEADERS' in line and 'cookie' in line:
                line = re.sub(r"'cookie': '.*?'", "'cookie': '{}'".format(cookie.get()), line)
            for pipeline in pipelines:  # Change here, loop over all pipelines, not just the ones with entries
                if pipeline in line:
                    if var_dict[pipeline].get():
                        entry = next((e for p, e in pipeline_entries if p == pipeline), None)
                        priority = '    \'{}\': {}'.format(pipeline, entry.get() if entry else 1)
                        line = re.sub(r"#?\s*'{}': \d+".format(pipeline), priority, line)
                    else:
                        line = re.sub(r"#?\s*'{}': \d+".format(pipeline), '#    \'{}\': 1'.format(pipeline), line)
            f.write(line)

    importlib.reload(settings)  # Reload the settings module
    messagebox.showinfo("Info", "Settings saved")




root = tk.Tk()
root.title("Settings")
root.geometry("900x500")
my_font = font.Font(family="Arial", size=14)

DOWNLOAD_DELAY_frame = tk.Frame(root)
DOWNLOAD_DELAY_frame.grid(row=0, column=0, sticky="ew")
DOWNLOAD_DELAY_label = tk.Label(DOWNLOAD_DELAY_frame, text="DOWNLOAD_DELAY:", font=my_font)
DOWNLOAD_DELAY_label.pack(side="left")
DOWNLOAD_DELAY = tk.StringVar()
entry1 = tk.Entry(DOWNLOAD_DELAY_frame,textvariable=DOWNLOAD_DELAY,font=my_font)
entry1.insert(0, settings.DOWNLOAD_DELAY)  # Set the default value
entry1.pack(side="left", fill="x", expand=True)

cookie_frame = tk.Frame(root)
cookie_frame.grid(row=0, column=1, sticky="ew")
cookie_label = tk.Label(cookie_frame, text="cookie:", font=my_font)
cookie_label.pack(side="left")
cookie = tk.StringVar()
entry2 = tk.Entry(cookie_frame,textvariable=cookie,font=my_font)
entry2.insert(0, settings.DEFAULT_REQUEST_HEADERS['cookie'])  # Set the default value
entry2.pack(side="left", fill="x", expand=True)

pipelines = [
    'weibo.pipelines.CsvPipeline',
    'weibo.pipelines.MysqlPipeline',
    'weibo.pipelines.MongoPipeline',
    'weibo.pipelines.MyImagesPipeline',
    # 'weibo.pipelines.MyVideoPipeline'
]

pipeline_entries = []
row = 3
var_dict = {}

for pipeline in pipelines:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=pipeline, variable=var,font=my_font)
    checkbox.grid(row=row, column=0, sticky="w")

    entry = tk.Entry(root, font=my_font)
    entry.grid(row=row, column=1, sticky="ew")
    entry.grid_remove()  # Initially hide the entry

    def show_entry(var=var, pipeline=pipeline, entry=entry):  # Use default arguments to capture the current pipeline and entry
        if var.get():
            entry.grid()  # Show the entry when the checkbox is checked
            pipeline_entries.append((pipeline, entry))
        else:
            entry.grid_remove()  # Hide the entry when the checkbox is unchecked
            if (pipeline, entry) in pipeline_entries:
                pipeline_entries.remove((pipeline, entry))

    checkbox.config(command=show_entry)
    var_dict[pipeline] = var
    row += 1

button = tk.Button(root, text="Save", command=save_settings)
button.grid(row=row, column=0, columnspan=2)

root.mainloop()
