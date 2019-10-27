from Arduino import Arduino
import time

board = Arduino('9600')
board.pinMode(13, "OUTPUT")
board.digitalWrite(13, "LOW")

while True:
    board.digitalWrite(13, "HIGH")
    time.sleep(2)
    board.digitalWrite(13, "LOW")
    time.sleep(2)