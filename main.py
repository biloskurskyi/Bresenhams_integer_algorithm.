import numpy as np
import matplotlib.pyplot as plt
import math
import time
from functions import draw_line_by_pixel

fun = input(
    "Виберіть функціонал(1 - відображення у пікселях, 2 - відображення малюнком, 3 - відображення у консолі, 4 - комбінація 1 та 2): ")

center_x = 16
center_y = 16


num_lines = int(input("Кількість ліній: "))
radius = int(input("Радіус: "))
if radius >= 16:
    radius = 15.9

if fun == "1":
    frame_buffer = np.zeros((33, 33), dtype=np.int8)
    plt.figure()
    col = input(
        "Виберіть колір(1 - viridis, 2 - plasma, 3 - magma, else - gray): ")
    if col == "1":
        cmap = 'viridis'
    elif col == "2":
        cmap = 'plasma'
    elif col == "3":
        cmap = 'magma'
    else:
        cmap = 'gray'
    for i in range(num_lines):
        angle = 2 * np.pi * i / num_lines
        end_x = center_x + int(radius * np.cos(angle))
        end_y = center_y + int(radius * np.sin(angle))

        draw_line_by_pixel(center_x, center_y, end_x, end_y, frame_buffer, 1)
        plt.imshow(frame_buffer, cmap=cmap, origin='lower')
        plt.title(f"Line {i + 1}")
        plt.draw()
        plt.pause(0.05)

        time.sleep(0.05)
    plt.xlim(0, 32)
    plt.ylim(0, 32)
    plt.show()

elif fun == "2":
    col = input(
        "Виберіть колір(1 - green, 2 - red, 3 - blue, else - gray): ")
    if col == "1":
        typ = 'green'
    elif col == "2":
        typ = 'red'
    elif col == "3":
        typ = 'blue'
    else:
        typ = 'gray'
    for i in range(num_lines):
        angle = 2 * np.pi * i / num_lines
        end_x = center_x + int(radius * np.cos(angle))
        end_y = center_y + int(radius * np.sin(angle))

        line_x = [center_x, end_x]
        line_y = [center_y, end_y]

        plt.plot(line_x, line_y, color=typ)

        plt.title(f"Line {i + 1}")
        plt.axis('equal')
        plt.draw()
        plt.pause(0.01)

        time.sleep(0.01)

    plt.xlim(0, 32)
    plt.ylim(0, 32)
    plt.show()

elif fun == "3":
    col = input(
        "Виберіть шрифт(1 - o, else - *): ")
    if col == "1":
        typ = 'o'
    else:
        typ = '*'

    frame_buffer_1 = np.full((32, 32), ' ', dtype='<U1')
    for i in range(num_lines):
        angle = 2 * math.pi * i / num_lines
        end_x = center_x + int(radius * math.cos(angle))
        end_y = center_y + int(radius * math.sin(angle))
        draw_line_by_pixel(center_x, center_y, end_x, end_y, frame_buffer_1, typ)

    for row in frame_buffer_1:
        print(' '.join(row))

elif fun == "4":
    col = input(
        "Виберіть колір(1 - viridis, 2 - plasma, 3 - magma, else - gray): ")
    if col == "1":
        cmap = 'viridis'
    elif col == "2":
        cmap = 'plasma'
    elif col == "3":
        cmap = 'magma'
    else:
        cmap = 'gray'

    col_ = input(
        "Виберіть колір(1 - green, 2 - red, 3 - blue, else - gray): ")
    if col_ == "1":
        typ = 'green'
    elif col_ == "2":
        typ = 'red'
    elif col_ == "3":
        typ = 'blue'
    else:
        typ = 'gray'
    frame_buffer = np.zeros((32, 32), dtype=np.int8)
    plt.figure()
    for i in range(num_lines):
        angle = 2 * np.pi * i / num_lines
        end_x = center_x + int(radius * np.cos(angle))
        end_y = center_y + int(radius * np.sin(angle))

        draw_line_by_pixel(center_x, center_y, end_x, end_y, frame_buffer, 1)
        plt.imshow(frame_buffer, cmap=cmap, origin='lower')
        plt.title(f"Line {i + 1}")
        plt.draw()
        plt.pause(0.01)

        time.sleep(0.01)

    for i in range(num_lines):
        angle = 2 * np.pi * i / num_lines
        end_x = center_x + int(radius * np.cos(angle))
        end_y = center_y + int(radius * np.sin(angle))

        line_x = [center_x, end_x]
        line_y = [center_y, end_y]

        plt.plot(line_x, line_y, color=typ)

        plt.title(f"Line {i + 1}")
        plt.axis('equal')
        plt.draw()
        plt.pause(0.01)

        time.sleep(0.01)
    plt.show()
else:
    print("Такого функціоналу не існує!")
