import tkinter as t
from math import gcd
from fractions import Fraction as fr
from postfix_upgrade import *

# Main
root = t.Tk()
root.title('누나의 워라밸을 위하여')
root.geometry('1000x500')
root.resizable(width=False, height=True)

# Default
# Global Variables & Constants
status = 1

frame = t.Frame(root)
frame.pack()
scrollbar = t.Scrollbar(frame, width=20)
scrollbar.pack(side="left", fill="y")
scrollbar_x = t.Scrollbar(frame, width=20, orient=t.HORIZONTAL)
scrollbar_x.pack(side='bottom', fill='x')
scrollbar2 = t.Scrollbar(frame, width=20)
scrollbar2.pack(side='right', fill='y')

text = t.Text(frame, width=80, wrap='none', bd=2, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set)
text2 = t.Text(frame, width=20, wrap='none', state=t.DISABLED, bd=2, yscrollcommand=scrollbar2.set)
text.pack(side="left")
text2.pack(side='right')


scrollbar2['command'] = text2.yview
scrollbar["command"] = text.yview
scrollbar_x['command'] = text.xview


def click_fr():
    global status
    text2['state'] = t.NORMAL
    status = 1
    button_lcm['state'] = t.NORMAL
    i = 1
    text2.delete('1.0', 'end')
    while text.get(f'{i}.0', 'end'):
        ans = solution_fraction(text.get(f'{i}.0', f'{i}.end'))
        text2.insert(f'{i}.0', str(ans) + "\n")
        i += 1
    text2['state'] = t.DISABLED

def click_cal():
    global status
    text2['state'] = t.NORMAL
    status = 0
    button_lcm['state'] = t.DISABLED
    i = 1
    text2.delete('1.0', 'end')
    while text.get(f'{i}.0', 'end'):
        ans = solution(text.get(f'{i}.0', f'{i}.end'))
        text2.insert(f'{i}.0', str(ans) + "\n")
        i += 1
    text2['state'] = t.DISABLED


def click_lcm():
    text2['state'] = t.NORMAL

    def arr_lcm(elem: list) -> int:
        def lcm(x: int, y: int) -> int:
            return int(x * y / gcd(x, y))

        while len(elem) > 1:
            elem.append(lcm(elem.pop(), elem.pop()))
        return elem[0]

    i = 1
    deno = set()
    save = []
    while text.get(f'{i}.0', 'end'):
        value = re.sub(r'[\n\t]', '', text2.get(f'{i}.0', f'{i}.end'))
        if value:
            fraction = value.split('/')
        else:
            fraction = ['0', '1']
        save.append(fraction)
        deno.add(int(fraction[1]))
        i += 1
    deno = list(deno)
    lcm = str(arr_lcm(deno))

    text2.delete('1.0', 'end')

    for i, tuple in enumerate(save, start=1):
        if tuple[0] != '0':
            text2.insert(f'{i}.0', str(solution_fraction(tuple[0] + '*' + lcm + '/' + tuple[1])) + '/'
                         + str(solution_fraction(tuple[1] + '*' + lcm + '/' + tuple[1])) + "\n")
        else:
            text2.insert(f'{i}.0', '\n')

    text2['state'] = t.DISABLED


def click_clear():
    text2['state'] = t.NORMAL
    entry['state'] = t.NORMAL

    text.delete('1.0', 'end')
    text2.delete('1.0', 'end')
    entry.delete(0, 'end')

    text2['state'] = t.DISABLED
    entry['state'] = t.DISABLED


def click_sum():
    entry['state'] = t.NORMAL
    global status
    i = 1
    if status:
        ans = fr(0)
        entry.delete('0', 'end')
        while text2.get(f'{i}.0', 'end'):
            value = re.sub(r'\n', '', str(text2.get(f'{i}.0', f'{i}.end')))
            if value:
                ans += fr(value)
            i += 1
        entry.insert(1, f'{ans}')

    else:
        ans = 0
        entry.delete('0', 'end')
        while text2.get(f'{i}.0', 'end'):
            value = re.sub(r'\n', '', str(text2.get(f'{i}.0', f'{i}.end')))
            if value:
                ans += float(value)
            i += 1
        entry.insert(1, f'{ans}')
    entry['state'] = t.DISABLED


button_fr = t.Button(root, text='분수꼴', command=click_fr)
button_fr.place(x=20, y=20)
button_cal = t.Button(root, text='소수꼴', command=click_cal)
button_cal.place(x=20, y=50)
button_lcm = t.Button(root, text='통분', command=click_lcm)
button_lcm.place(x=70, y=20)
button_sum = t.Button(root, text='합', command=click_sum)
button_sum.place(x=20, y=80)

button_clear = t.Button(root, text='지우기', command=click_clear)
button_clear.place(x=20, y=120)

entry = t.Entry(root, width=20, state=t.DISABLED, disabledbackground='white')
entry.place(x=710, y=350)
label = t.Label(root, text='합계:', font=('System', 15))
label.place(x=650, y=350)

root.mainloop()
