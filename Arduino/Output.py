from Arduino import Arduino

def init():
    global board
    global pin
    pin = 13
    board = Arduino('9600')
    board.pinMode(pin, "OUTPUT")
    board.digitalWrite(pin, "LOW")

def write(output):
    board.digitalWrite(pin, "HIGH" if output is True else "LOW")
