import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def add_project():
    project_name = project_entry.get()
    schedule = schedule_entry.get_date()
    project_manager = manager_entry.get()

    table.insert('', 'end', values=(project_name, schedule, project_manager))


def delete_project():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)

window = tk.Tk()
window.title('캘린더 관리 프로그램')

project_label = tk.Label(window, text='프로젝트')
project_label.pack()
project_entry=tk.Entry(window)
project_entry.pack()

schedule_label = tk.Label(window, text='일정')
schedule_label.pack()
schedule_entry=DateEntry(window)
schedule_entry.pack()

manager_label = tk.Label(window, text='담당자')
manager_label.pack()
manager_entry=tk.Entry(window)
manager_entry.pack()

add_button = tk.Button(window, text='프로젝트 추가',command=add_project)
add_button.pack()

delete_button = tk.Button(window, text='프로젝트 삭제', command=delete_project)
delete_button.pack()

table=ttk.Treeview(window, columns=('프로젝트', '일정', '담당자'), show='headings')
table.heading('프로젝트', text='프로젝트')
table.heading('일정', text='일정')
table.heading('담당자', text='담당자')
table.pack()

window.mainloop()