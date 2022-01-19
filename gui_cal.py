import tkinter as t
import tkinter.ttk as tk

from postfix_upgrade import *

# Main
root = t.Tk()
root.title('누나의 워라밸을 위하여')
root.geometry('1000x500')
root.resizable(width=False, height=True)
# Default
# Global Variables & Constants
row_position = 190
index = 4
entry_list = []
label_list = []
result_list = []
status = 1

# Scrollbar
scrollbar = t.Scrollbar(root, orient="vertical", command=root.yview)
scrollbar.pack(side="right", fill="y")


# Functions
# Button click
def click_add():
    global row_position, entry_list, index, label_list
    if index > 99:
        return False
    row_position += 30
    index += 1
    new_entry = t.Entry(width=80)
    new_entry.place(x=120, y=row_position)
    new_label = t.Label(root, text=str(index), font=('System', 10))
    new_label.place(x=100, y=row_position)
    new_result = t.Entry(width=20)
    new_result.place(x=700, y=row_position)
    entry_list.append(new_entry)
    label_list.append(new_label)
    result_list.append(new_result)


def click_minus():
    global row_position, entry_list, index, label_list
    if len(entry_list) < 5:
        return False
    row_position -= 30
    index -= 1
    entry_list.pop().destroy()
    label_list.pop().destroy()
    result_list.pop().destroy()


def click_fr():
    global entry_list, result_list, status
    if status == 1:
        for i in range(len(entry_list)):
            ans = solution_fraction(entry_list[i].get())
            result_list[i].delete(0, 20)
            result_list[i].insert(0, string=str(ans))
        button_cal['text'] = '소수계산'
    else:
        for i in range(len(entry_list)):
            ans = solution(entry_list[i].get())
            result_list[i].delete(0, 20)
            result_list[i].insert(0, string=str(ans))
        button_cal['text'] = '분수계산'
    status = -status


# Rows of a datatable
button_up = t.Button(root, text='+', font=('System', 15), command=click_add)
button_up.place(x=20, y=40)

button_down = t.Button(root, text='-', font=('System', 15), command=click_minus)
button_down.place(x=60, y=40)

table_label = t.Label(root, text='행 추가/감소', font=('System', 15))
table_label.place(x=10, y=15)

button_cal = t.Button(root, text='분수계산', font=('System', 15), command=click_fr)
button_cal.place(x=500, y=50)

# Input
i = 1
height = 100
while i <= 4:
    entry = t.Entry(width=80)
    entry.place(x=120, y=height)
    label = t.Label(root, text=f'{i}', font=('System', 10))
    label.place(x=100, y=height)
    result = t.Entry(width=20)
    result.place(x=700, y=height)
    entry_list.append(entry)
    label_list.append(label)
    result_list.append(result)

    i += 1
    height += 30

# ======================================================

root.mainloop()
