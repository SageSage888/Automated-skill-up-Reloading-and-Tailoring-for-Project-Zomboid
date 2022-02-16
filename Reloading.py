from random import choice
import autoit
import time
import Save
from tkinter import *


def right_click(x, y):
    for i in range(0, 15):
        autoit.mouse_click("right", x, y+1, 1)


def left_click(x, y):
    for i in range(0, 15):
        autoit.mouse_click("left", x-1, y, 1)

choice = None
# insert tkinter with 2 buttons here
# ----------------------------------
def btn_reloading():
    global choice
    choice = 1
    root.destroy()

def btn_tailoring():
    global choice
    choice = 2
    root.destroy()
    
root = Tk()
root['bg'] = '#fafafa'
root.title('PZ Reloading & Tailoring bot')
canvas = Canvas(root, height=300, width=250)
canvas.pack()
frame = Frame(root, bg='grey')
frame.place(relx=0.15, rely= 0.15, relwidth=0.7,relheight=0.7)
title = Label(frame, text='Choose skill',bg='grey', font=50)
title.pack()
btn_reload = Button(frame,text='Reloading', bg='white', command = btn_reloading)
btn_reload.pack()
btn_tailor = Button(frame,text='Tailoring', bg='white', command = btn_tailoring)
btn_tailor.pack()


root.mainloop()
print(choice)
# ----------------------------------

# choice = int(input('What will you improve? Reloading - 1, Tailoring - 2 \n'))
coordinates = Save.load_saves(choice)
if choice == 1:
    print('Reloading mode selected')
    n = input('Enter number of cycles: ')
    time.sleep(2)
    for i in range(0, int(n)):
        right_click(coordinates[0][0], coordinates[0][1])
        time.sleep(1)
        left_click(coordinates[1][0], coordinates[1][1])
        time.sleep(17)
        right_click(coordinates[0][0], coordinates[0][1])
        time.sleep(1)
        left_click(coordinates[1][0], coordinates[1][1])
        time.sleep(17)
    print('reloading is done')
elif choice == 2:
    print('Tailoring mode selected')
    n = input('Enter number of cycles: ')
    time.sleep(2)
    pass
