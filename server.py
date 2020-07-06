from ctypes import windll, Structure, c_long, byref
import socket
import threading
import time

PORT = 3308

server = socket.socket()
server.bind(('0.0.0.0', PORT))
server.listen(5)
client = None
# client, addr = server.accept()

PREV_X, PREV_Y = -1, -1
PREV_MOUSE_LEFT = windll.user32.GetKeyState(0x01)
PREV_MOUSE_RIGHT = windll.user32.GetKeyState(0x02)


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
            pass
        except:
            pass
        # TODO: Increase time period if Required
        time.sleep(0.025)


th = threading.Thread(target=threadLoop)
th.start()
th.join()
