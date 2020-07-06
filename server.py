from ctypes import windll, Structure, c_long, byref
import socket
import threading
import time
from keymap import KEYMAP

PORT = 3308

server = socket.socket()
server.bind(('0.0.0.0', PORT))
server.listen(5)
client = None
# client, addr = server.accept()

PREV_X, PREV_Y = -1, -1
PREV_MOUSE_LEFT = windll.user32.GetKeyState(0x01) & 0x8000
PREV_MOUSE_RIGHT = windll.user32.GetKeyState(0x02) & 0x8000


class Mouse(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def getKeyDown(keycode):
    state = windll.user32.GetKeyState(keycode)
    if (state != 0) and (state != 1):
        return True
    return False


def getMousePos():
    pt = Mouse()
    windll.user32.GetCursorPos(byref(pt))
    return (pt.x, pt.y)


def threadLoop():
    global server
    global client
    global PREV_X
    global PREV_Y
    global PREV_MOUSE_LEFT
    global PREV_MOUSE_RIGHT
    while True:
        try:
            mouse_left = windll.user32.GetKeyState(0x01)
            mouse_left = mouse_left & 0x8000
            mouse_right = windll.user32.GetKeyState(0x02)
            mouse_right = mouse_right & 0x8000
            x, y = getMousePos()

            if mouse_left != PREV_MOUSE_LEFT:
                PREV_MOUSE_LEFT = mouse_left
                if mouse_left != 0:
                    #  Left Pressed
                    print('LP')
                else:
                    # Left Released
                    print('LR')

            if mouse_right != PREV_MOUSE_RIGHT:
                PREV_MOUSE_RIGHT = mouse_right
                if mouse_right != 0:
                    # Right Pressed
                    print('RP')
                else:
                    # Right Pressed
                    print('RR')
            if x != PREV_X or y != PREV_Y:
                PREV_X, PREV_Y = x, y
                print(x, y)

            pass
        except:
            pass
        # TODO: Increase time period if Required
        time.sleep(0.025)


th = threading.Thread(target=threadLoop)
th.start()
th.join()
