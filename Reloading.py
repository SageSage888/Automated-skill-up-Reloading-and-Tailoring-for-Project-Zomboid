import autoit
import time
import Save


def right_click(x, y):
    for i in range(0, 15):
        autoit.mouse_click("right", x, y+1, 1)


def left_click(x, y):
    for i in range(0, 15):
        autoit.mouse_click("left", x-1, y, 1)


choice = int(input('What will you improve? Reloading - 1, Tailoring - 2 \n'))
coordinates = Save.load_saves(choice)
if choice == 1:
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
    n = input('Enter number of cycles: ')
    time.sleep(2)
    pass
