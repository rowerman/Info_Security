import tkinter as tk
from tkinter import messagebox, font
import importlib
import sys
import re
import datetime
from tkcalendar import DateEntry
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
            elif 'KEYWORD_LIST' in line:
                line = 'KEYWORD_LIST = [\'{}\']\n'.format(KEYWORD_LIST.get())
            elif 'WEIBO_TYPE' in line:
                line = 'WEIBO_TYPE = {}\n'.format(WEIBO_TYPE.get())
            elif 'CONTAIN_TYPE' in line:
                line = 'CONTAIN_TYPE = {}\n'.format((CONTAIN_TYPE.get()))
            elif 'REGION' in line:
                line = 'REGION = [\'{}\']\n'.format(REGION.get())
            elif 'START_DATE' in line:
                line = 'START_DATE = \'{}\'\n'.format(START_DATE.get())
            elif 'END_DATE' in line:
                line = 'END_DATE = \'{}\'\n'.format(END_DATE.get())
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

KEYWORD_LIST_frame = tk.Frame(root)
KEYWORD_LIST_frame.grid(row=1, column=0, sticky="ew")
KEYWORD_LIST_label = tk.Label(KEYWORD_LIST_frame, text="KEYWORD_LIST:", font=my_font)
KEYWORD_LIST_label.pack(side="left")
KEYWORD_LIST = tk.StringVar()
entry3 = tk.Entry(KEYWORD_LIST_frame,textvariable=KEYWORD_LIST,font=my_font)
entry3.insert(0, settings.KEYWORD_LIST)  # Set the default value
entry3.pack(side="left", fill="x", expand=True)

WEIBO_TYPE_frame = tk.Frame(root)
WEIBO_TYPE_frame.grid(row=1, column=1, sticky="ew")
WEIBO_TYPE_label = tk.Label(WEIBO_TYPE_frame, text="WEIBO_TYPE:", font=my_font)
WEIBO_TYPE_label.pack(side="left")
WEIBO_TYPE = tk.StringVar()
entry4 = tk.Entry(WEIBO_TYPE_frame,textvariable=WEIBO_TYPE,font=my_font)
entry4.insert(0, settings.WEIBO_TYPE)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

CONTAIN_TYPE_frame = tk.Frame(root)
CONTAIN_TYPE_frame.grid(row=2, column=0, sticky="ew")
CONTAIN_TYPE_label = tk.Label(CONTAIN_TYPE_frame, text="CONTAIN_TYPE:", font=my_font)
CONTAIN_TYPE_label.pack(side="left")
CONTAIN_TYPE = tk.StringVar()
entry4 = tk.Entry(CONTAIN_TYPE_frame,textvariable=CONTAIN_TYPE,font=my_font)
entry4.insert(0, settings.CONTAIN_TYPE)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

REGION_frame = tk.Frame(root)
REGION_frame.grid(row=2, column=1, sticky="ew")
REGION_label = tk.Label(REGION_frame, text="REGION:", font=my_font)
REGION_label.pack(side="left")
REGION = tk.StringVar()
entry4 = tk.Entry(REGION_frame,textvariable=REGION,font=my_font)
entry4.insert(0, settings.REGION)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

START_DATE_frame = tk.Frame(root)
START_DATE_frame.grid(row=3, column=0, sticky="ew")  # Change the row and column as needed
START_DATE_label = tk.Label(START_DATE_frame, text="START_DATE:", font=my_font)
START_DATE_label.pack(side="left")
START_DATE = tk.StringVar()
date_entry = DateEntry(START_DATE_frame, textvariable=START_DATE, font=my_font, background='darkblue', foreground='white', borderwidth=2)
default_date = datetime.datetime.strptime(settings.START_DATE, '%Y-%m-%d').date()
date_entry.set_date(default_date)
date_entry.pack(side="left", fill="x", expand=True)

END_DATE_frame = tk.Frame(root)
END_DATE_frame.grid(row=3, column=1, sticky="ew")  # Change the row and column as needed
END_DATE_label = tk.Label(END_DATE_frame, text="END_DATE:", font=my_font)
END_DATE_label.pack(side="left")
END_DATE = tk.StringVar()
date_entry = DateEntry(END_DATE_frame, textvariable=END_DATE, font=my_font, background='darkblue', foreground='white', borderwidth=2)
default_date = datetime.datetime.strptime(settings.END_DATE, '%Y-%m-%d').date()
date_entry.set_date(default_date)
date_entry.pack(side="left", fill="x", expand=True)

pipelines = [
    'weibo.pipelines.CsvPipeline',
    'weibo.pipelines.MysqlPipeline',
    'weibo.pipelines.MongoPipeline',
    'weibo.pipelines.MyImagesPipeline',
    # 'weibo.pipelines.MyVideoPipeline'
]

pipeline_entries = []
row = 4
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
