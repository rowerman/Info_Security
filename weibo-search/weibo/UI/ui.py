import tkinter as tk
from tkinter import messagebox, font, filedialog, ttk
import importlib
import sys
import re
import subprocess
import datetime
from tkcalendar import DateEntry

sys.path.append("..") 

import settings

# Import settings module
sys.path.insert(0, '../settings.py')  # replace with the path to your settings.py

def select_directory(label):
    # 打开文件夹对话框，让用户选择一个文件夹
    directory_path = filedialog.askdirectory()

    # 将用户选择的文件夹路径显示在Label组件中
    label.config(text=directory_path)

    # 读取settings.py文件
    with open('../settings.py', 'r',encoding='utf-8') as file:
        lines = file.readlines()

    # 修改IMAGES_STORE的值
    for i, line in enumerate(lines):
        if 'IMAGES_STORE' in line:
            lines[i] = 'IMAGES_STORE = \'{}\'\n'.format(directory_path)

    # 将修改后的配置写回settings.py文件
    with open('../settings.py', 'w',encoding='utf-8') as file:
        file.writelines(lines)
'''
def execute_commands():
    # List of commands to execute
    commands = [
        'scrapy crawl search -s JOBDIR=crawls/search',
    ]
    # Execute each command
    for command in commands:
        subprocess.Popen(command, shell=True, cwd='../spiders/', creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
'''
def save_settings():
    flag = True

    with open('../settings.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('../settings.py', 'w', encoding='utf-8') as f:
        for line in lines:
            if 'DOWNLOAD_DELAY' in line:
                line = 'DOWNLOAD_DELAY = {}\n'.format(DOWNLOAD_DELAY.get())
            elif 'DEFAULT_REQUEST_HEADERS' in line and 'cookie' in line:
                line = re.sub(r"'cookie': '.*?'", "'cookie': '{}'".format(cookie.get()), line)
            elif 'KEYWORD_LIST1' in line and flag:
                flag = False
                line = 'KEYWORD_LIST1 = [\'{}\']\n'.format(KEYWORD_LIST1.get())
            elif 'WEIBO_TYPE' in line:
                line = 'WEIBO_TYPE = {}\n'.format(WEIBO_TYPE.get())
            elif 'CONTAIN_TYPE' in line:
                line = 'CONTAIN_TYPE = {}\n'.format((CONTAIN_TYPE.get()))
            elif 'REGION' in line:
                line = 'REGION = [\'{}\']\n'.format(REGION.get())
            elif 'FURTHER_THRESHOLD' in line:
                line = 'FURTHER_THRESHOLD = {}\n'.format(FURTHER_THRESHOLD.get())
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
    value = var_dict.get('weibo.pipelines.MysqlPipeline')
    if value :
        mysql_host = mysql_entries[0][0].get()
        mysql_port = mysql_entries[1][0].get()
        mysql_user = mysql_entries[2][0].get()
        mysql_password = mysql_entries[3][0].get()
        mysql_database = mysql_entries[4][0].get()
        with open('../settings.py', 'r',encoding='utf-8') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if 'MYSQL_HOST' in line:
                lines[i] = f"MYSQL_HOST = '{mysql_host}'\n"
            elif 'MYSQL_PORT' in line:
                lines[i] = f"MYSQL_PORT = {mysql_port}\n"
            elif 'MYSQL_USER' in line:
                lines[i] = f"MYSQL_USER = '{mysql_user}'\n"
            elif 'MYSQL_PASSWORD' in line:
                lines[i] = f"MYSQL_PASSWORD = '{mysql_password}'\n"
            elif 'MYSQL_DATABASE' in line:
                lines[i] = f"MYSQL_DATABASE = '{mysql_database}'\n"
        with open('../settings.py', 'w',encoding='utf-8') as file:
            file.writelines(lines)

    importlib.reload(settings)  # Reload the settings module
    messagebox.showinfo("Info", "Settings saved")
def update_frame_size(event):
    canvas.itemconfig(frame_id, width=canvas.winfo_width(), height=canvas.winfo_height())

root = tk.Tk()
root.title("Settings")
root.geometry("900x600")
root.configure(bg='lightgray')
my_font = font.Font(family="Arial", size=14)

# 创建一个滚动条
scrollbar = tk.Scrollbar(root, width=20, troughcolor='gray', relief='sunken')
scrollbar.pack(side="right", fill="y")

# 创建一个Canvas，将滚动条与Canvas关联
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.configure(bg="lightgray")
canvas.pack(side="left", fill="both", expand=True)

# 配置滚动条的命令
scrollbar.config(command=canvas.yview)

# 创建一个Frame，将其添加到Canvas中
frame = tk.Frame(canvas)
frame_id = canvas.create_window((0, 0), window=frame, anchor="nw", width=canvas.winfo_width(), height=canvas.winfo_height())
canvas.bind("<Configure>", update_frame_size)



for i in range(20):  # Adjust the range as needed
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

DOWNLOAD_DELAY_frame = tk.Frame(frame,bg="lightgray")
DOWNLOAD_DELAY_frame.grid(row=0, column=0, sticky="NSEW",padx=(0,40),pady=5)
DOWNLOAD_DELAY_label = tk.Label(DOWNLOAD_DELAY_frame, text="DOWNLOAD_DELAY:", font=my_font,bg="lightgray")
DOWNLOAD_DELAY_label.pack(side="left")
DOWNLOAD_DELAY = tk.StringVar()
entry1 = tk.Entry(DOWNLOAD_DELAY_frame,textvariable=DOWNLOAD_DELAY,font=my_font)
entry1.insert(0, settings.DOWNLOAD_DELAY)  # Set the default value
entry1.pack(side="left", fill="x", expand=True)

cookie_frame = tk.Frame(frame,bg="lightgray")
cookie_frame.grid(row=0, column=1,sticky="NSEW",padx=5,pady=5)
cookie_label = tk.Label(cookie_frame, text="cookie:", font=my_font,bg="lightgray")
cookie_label.pack(side="left")
cookie = tk.StringVar()
entry2 = tk.Entry(cookie_frame,textvariable=cookie,font=my_font)
entry2.insert(0, settings.DEFAULT_REQUEST_HEADERS['cookie'])  # Set the default value
entry2.pack(side="left", fill="x", expand=True)

KEYWORD_LIST1_frame = tk.Frame(frame,bg="lightgray")
KEYWORD_LIST1_frame.grid(row=1, column=0, sticky="NSEW",padx=(0,40),pady=5)
KEYWORD_LIST1_label = tk.Label(KEYWORD_LIST1_frame, text="KEYWORD_LIST:", font=my_font,bg="lightgray")
KEYWORD_LIST1_label.pack(side="left")
KEYWORD_LIST1 = tk.StringVar()
entry3 = tk.Entry(KEYWORD_LIST1_frame,textvariable=KEYWORD_LIST1,font=my_font)
entry3.insert(0, settings.KEYWORD_LIST1)  # Set the default value
entry3.pack(side="left", fill="x", expand=True)

WEIBO_TYPE_frame = tk.Frame(frame,bg="lightgray")
WEIBO_TYPE_frame.grid(row=1, column=1,sticky="NSEW",padx=5,pady=5)
WEIBO_TYPE_label = tk.Label(WEIBO_TYPE_frame, text="WEIBO_TYPE:", font=my_font,bg="lightgray")
WEIBO_TYPE_label.pack(side="left")
WEIBO_TYPE = tk.StringVar()
entry4 = tk.Entry(WEIBO_TYPE_frame,textvariable=WEIBO_TYPE,font=my_font)
entry4.insert(0, settings.WEIBO_TYPE)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

CONTAIN_TYPE_frame = tk.Frame(frame,bg="lightgray")
CONTAIN_TYPE_frame.grid(row=2, column=0, sticky="NSEW",padx=(0,40),pady=5)
CONTAIN_TYPE_label = tk.Label(CONTAIN_TYPE_frame, text="CONTAIN_TYPE:", font=my_font,bg="lightgray")
CONTAIN_TYPE_label.pack(side="left")
CONTAIN_TYPE = tk.StringVar()
entry4 = tk.Entry(CONTAIN_TYPE_frame,textvariable=CONTAIN_TYPE,font=my_font)
entry4.insert(0, settings.CONTAIN_TYPE)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

REGION_frame = tk.Frame(frame,bg="lightgray")
REGION_frame.grid(row=2, column=1, sticky="NSEW",padx=5,pady=5)
REGION_label = tk.Label(REGION_frame, text="REGION:", font=my_font,bg="lightgray")
REGION_label.pack(side="left")
REGION = tk.StringVar()
entry4 = tk.Entry(REGION_frame,textvariable=REGION,font=my_font)
entry4.insert(0, settings.REGION)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

START_DATE_frame = tk.Frame(frame,bg="lightgray")
START_DATE_frame.grid(row=3, column=0, sticky="NSEW",padx=(0,40),pady=5)  # Change the row and column as needed
START_DATE_label = tk.Label(START_DATE_frame, text="START_DATE:", font=my_font,bg="lightgray")
START_DATE_label.pack(side="left")
START_DATE = tk.StringVar()
date_entry = DateEntry(START_DATE_frame, textvariable=START_DATE, font=my_font, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
default_date = datetime.datetime.strptime(settings.START_DATE, '%Y-%m-%d').date()
date_entry.set_date(default_date)
date_entry.pack(side="left",fill="x",expand=True)

END_DATE_frame = tk.Frame(frame,bg="lightgray")
END_DATE_frame.grid(row=3, column=1, sticky="NSEW",padx=5,pady=5)  # Change the row and column as needed
END_DATE_label = tk.Label(END_DATE_frame, text="END_DATE:", font=my_font,bg="lightgray")
END_DATE_label.pack(side="left")
END_DATE = tk.StringVar()
date_entry = DateEntry(END_DATE_frame, textvariable=END_DATE, font=my_font, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
default_date = datetime.datetime.strptime(settings.END_DATE, '%Y-%m-%d').date()
date_entry.set_date(default_date)
date_entry.pack(side="left", fill="x", expand=True)

FURTHER_THRESHOLD_frame = tk.Frame(frame,bg="lightgray")
FURTHER_THRESHOLD_frame.grid(row=4, column=0, sticky="NSEW",padx=(0,40),pady=5)
FURTHER_THRESHOLD_label = tk.Label(FURTHER_THRESHOLD_frame, text="FURTHER_THRESHOLD:", font=my_font,bg="lightgray")
FURTHER_THRESHOLD_label.pack(side="left")
FURTHER_THRESHOLD = tk.StringVar()
entry4 = tk.Entry(FURTHER_THRESHOLD_frame,textvariable=FURTHER_THRESHOLD,font=my_font)
entry4.insert(0, settings.FURTHER_THRESHOLD)  # Set the default value
entry4.pack(side="left", fill="x", expand=True)

pipelines = [
    '存储为Csv文件',
    '存储在Mysql数据库中',
    '存储在Mongo数据库中',
    '爬取数据时下载图片',
]

pipeline_entries = []
row = 5
var_dict = {}

for pipeline in pipelines:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(frame, text=pipeline, variable=var,font=my_font,bg="lightgray")
    checkbox.grid(row=row, column=0, sticky="w",padx=(0,5),pady=5)

    entry = tk.Entry(frame, font=my_font)
    entry.grid(row=row, column=1, sticky="w",padx=5,pady=5)
    entry.grid_remove()  # Initially hide the entry

    label = tk.Label(frame, text="", font=my_font)
    label.grid(row=row+1, column=1, sticky="w",padx=5,pady=5)
    label.grid_remove()  # Initially hide the label

    button = tk.Button(frame, text="选择文件夹", command=lambda: select_directory(label))
    button.grid(row=row+1, column=0, sticky="w",padx=5,pady=5)
    button.grid_remove()  # Initially hide the button

    # Create five entries for 'weibo.pipelines.CsvPipeline'
    if pipeline == '存储在Mysql数据库中':
        mysql_entries = []
        for i, mysql_label in enumerate(['MYSQL_HOST', 'MYSQL_PORT', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DATABASE']):
            label = tk.Label(frame, text=mysql_label, font=my_font,bg="lightgrey",width=30)
            label.grid(row=row + i + 4, column=0, sticky="NSEW",padx=5,pady=5)  # Change column to 1
            label.grid_remove()  # Initially hide the label
            mysql_entry = tk.Entry(frame, font=my_font,width=30)
            mysql_entry.grid(row=row + i + 4, column=1, sticky="NSEW",padx=5,pady=5)  # Change column to 2
            mysql_entry.grid_remove()  # Initially hide the entry
            mysql_entries.append((mysql_entry, label))


    def show_entry(var=var, pipeline=pipeline, entry=entry, button=button,
                   label=label):  # Use default arguments to capture the current pipeline, entry, button and label
        if var.get():
            entry.grid()  # Show the entry when the checkbox is checked
            if pipeline == '爬取数据时下载图片':
                button.grid()  # Show the button when the specific checkbox is checked
                label.grid()  # Show the label when the specific checkbox is checked
            # Show the five entries and their labels when the 'weibo.pipelines.CsvPipeline' checkbox is checked
            if pipeline == '存储在Mysql数据库中':
                for mysql_entry, mysql_label in mysql_entries:
                    mysql_entry.grid()
                    mysql_label.grid()
            pipeline_entries.append((pipeline, entry))
        else:
            entry.grid_remove()  # Hide the entry when the checkbox is unchecked
            button.grid_remove()  # Hide the button when the checkbox is unchecked
            label.grid_remove()  # Hide the label when the checkbox is unchecked
            # Hide the five entries and their labels when the 'weibo.pipelines.CsvPipeline' checkbox is unchecked
            if pipeline == '存储在Mysql数据库中':
                for mysql_entry, mysql_label in mysql_entries:
                    mysql_entry.grid_remove()
                    mysql_label.grid_remove()
            if (pipeline, entry) in pipeline_entries:
                pipeline_entries.remove((pipeline, entry))

    checkbox.config(command=show_entry)
    var_dict[pipeline] = var
    row += 1

root1 = tk.Tk()
root1.geometry('800x300')
root1.title("使用说明")
# 创建一个Style对象
style = ttk.Style()
# 设置Treeview的字体大小
style.configure("Treeview", font=('Arial', 14),rowheight=50)  # 设置字体为Helvetica，大小为18
# 创建一个Treeview组件
tree = ttk.Treeview(root1, columns=('A', 'B'), show='headings')
# 设置列的宽度和标题
tree.column('A', width=227, anchor='center')
tree.column('B', width=1300, anchor='w')
tree.heading('A', text='参数')
tree.heading('B', text='说明')


# 向Treeview组件中插入数据
data = [
    ('DOWNLOADDELAY', '访问完一个页面再访问下一个时需要等待的时间，默认为10秒'),
    ('cookie', '微博用户的cookie'),
    ('KEYWORD_LIST', '要爬取的内容关键词'),
    ('WEIBO_TYPE', '要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博'),
    ('CONTAIN_TYPE', '筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博'),
    ('REGION', '只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”'),
    ('START_DATE', '搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期'),
    ('END_DATE', '搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期'),
    ('FURTHER_THRESHOLD', '进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。建议数值大小设置在40到50之间')
]
for item in data:
    tree.insert('', 'end', values=item)

# 创建一个Scrollbar组件，设置它的orient为'horizontal'，表示它是一个水平滚动条
scrollbar = tk.Scrollbar(root1, orient='horizontal')
# 设置Treeview组件的xscrollcommand为scrollbar的set方法，这样当Treeview组件滑动时，Scrollbar组件也会跟着滑动
tree.configure(xscrollcommand=scrollbar.set)
# 将Scrollbar组件的command设置为Treeview组件的xview方法，这样当滑动滚动条时，Treeview组件也会跟着滑动
scrollbar.configure(command=tree.xview)

# 将Treeview组件放置在第五行到第九行
tree.grid(row=0, column=2, rowspan=11, sticky='nsew')
scrollbar.grid(row=11, column=2, sticky='ew')

# 设置第二列的权重为1，这样当窗口大小改变时，这一列会获得额外的空间
root1.grid_columnconfigure(2, weight=1)
# 设置第十一行的权重为1，这样当窗口大小改变时，这一行会获得额外的空间
root1.grid_rowconfigure(11, weight=1)

button = tk.Button(frame, text="Save", command=save_settings,bg="gray",width=100, height=2)
button.grid(row=row+6, column=0,columnspan=2,padx=5,pady=5,sticky="EW")
# execute_button = tk.Button(root, text="Execute Commands", command=execute_commands)
# execute_button.grid(row=row, column=1, columnspan=2)  # Adjust the row and column as needed

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
root.mainloop()
