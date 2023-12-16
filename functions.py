def draw_line_by_pixel(x1, y1, x2, y2, frame_buffer, typ):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        direction_x = 1
    else:
        direction_x = -1

    if y1 < y2:
        direction_y = 1
    else:
        direction_y = -1
    err = dx - dy
    coordinates = []

    while True:
        coordinates.append((x1, y1))
        frame_buffer[y1][x1] = typ

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += direction_x
        if e2 < dx:
            err += dx
            y1 += direction_y

    print(*coordinates)
