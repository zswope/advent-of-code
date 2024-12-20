from tkinter import *
import re
import time

star1 = 0
star2 = 0
import os
with open(os.path.basename(__file__).split('_')[0]+'.txt', 'r') as file:
    data = file.readlines()
#     data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """.split('\n')
    data = [line.split('\n')[0] for line in data if line]
    data = ''.join(data)

running = False
curIdx = 0
colors = {
    1: 'red',
    2: 'green',
    3: 'white',
}
coloring = []
curColor = 2

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')
matches = pattern.finditer(data)
enabled = True
idx = 0
for match in matches:
    coloring += [curColor] * (match.start() - idx)
    idx = match.end()
    if match.group() == 'do()':
        curColor = 2
        coloring += [curColor] * len(match.group())
        enabled = True
    elif match.group() == 'don\'t()':
        curColor = 1
        coloring += [curColor] * len(match.group())
        enabled = False
    else:
        n1, n2 = map(int, match.groups())
        star1 += (n1*n2)
        if enabled:
            coloring += [3] * len(match.group())
            star2 += (n1*n2)
        else:
            coloring += [curColor] * len(match.group())
coloring += [curColor] * (len(data) - idx)

def apply_color(start, end, color):
    start_idx = f'1.{start}'
    end_idx = f'1.{end}'
    w.tag_add(color, start_idx, end_idx)
    w.tag_configure(color, foreground=color)

def process(idx):
    apply_color(idx, idx+1, colors[coloring[idx]])
    if idx + 1 < len(coloring):
        apply_color(idx+1, idx+2, colors[coloring[idx+1]])
        return idx+2
    return idx+1

# pretty standard stuff
def toggle():
    global running
    if running:
        pause()
    else:
        resume()
def pause():
    global running
    running = False
    btnStart.config(text="Resume")
def resume():
    global running
    running = True
    btnStart.config(text="Pause")

def reset():
    pause()
    btnStart.config(text="Start")
    global curIdx
    curIdx = 0
    w.delete('1.0',END)
    w.insert('1.0',data)
    apply_color(0,len(data),'gray')


master = Tk()
master.title('AoC Day 3 - Visualized')
master.minsize(1800,1100)

btnStart = Button(master, text="Start", command=toggle)
btnReset = Button(master, text="Reset", command=reset)

lbl1 = StringVar()
lbl2 = StringVar()
lblStar1 = Label(master, textvariable=lbl1)
lblStar2 = Label(master, textvariable=lbl2)
lbl1.set("Star 1 = ")
lbl2.set("Star 2 = ")

btnStart.pack()
btnReset.pack()
lblStar1.pack()
lblStar2.pack()

w = Text(master)
w.pack(expand=YES,fill=BOTH)
reset()

while True:
    try:
        master.update()
    except:
        exit()
    if running:
        if curIdx < len(data):
            curIdx = process(curIdx)
        else:
            pause()
            btnStart.config(text="Done!")
            lbl1.set('Star 1 = %d'%star1)
            lbl2.set('Star 2 = %d'%star2)
