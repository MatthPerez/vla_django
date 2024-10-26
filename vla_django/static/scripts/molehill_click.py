import pyautogui

# a, b = pyautogui.position()


def molehill_1(x, y):
    pyautogui.click(x, y)

    for column in range(12):
        for line in range(17):
            x_coord = x + 50 * line
            y_coord = y + 50 * column
            pyautogui.click(x=x_coord, y=y_coord)


def half_molehill_1(x, y):
    pyautogui.click(x, y)

    for column in range(6):
        for line in range(17):
            x_coord = x + 50 * line
            y_coord = y + 50 * column
            pyautogui.click(x=x_coord, y=y_coord)


def molehill_2(x, y):
    pyautogui.click(x, y)

    for column in range(12):
        for line in range(9):
            x_coord = x + 100 * line
            y_coord = y + 50 * column
            pyautogui.click(x=x_coord, y=y_coord)


def molehill_4(x, y):
    pyautogui.click(x, y)

    for column in range(6):
        for line in range(8):
            x_coord = x + 100 * line
            y_coord = y + 100 * column
            pyautogui.click(x=x_coord, y=y_coord)

    for column in range(12):
        x_coord = x + 50 * 16
        y_coord = y + 50 * column
        pyautogui.click(x=x_coord, y=y_coord)


# molehill_1(3190, 590)
# half_molehill_1(3190, 590)
# half_molehill_1(3190, 890)

# molehill_2(3190, 590)

# molehill_4(3190, 590)

# 3983 606
