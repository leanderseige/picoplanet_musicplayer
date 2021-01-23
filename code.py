import pulseio
import board
import time
import touchio
from digitalio import DigitalInOut, Direction, Pull
from song import song
from notes import notes

# init buttons
# touch1 = touchio.TouchIn(board.A0)
# touch2 = touchio.TouchIn(board.A1)
# touch3 = touchio.TouchIn(board.A2)

# init LEDs
ledG = DigitalInOut(board.D5)
ledG.direction = Direction.OUTPUT
ledR = DigitalInOut(board.D6)
ledR.direction = Direction.OUTPUT
ledB = DigitalInOut(board.D7)
ledB.direction = Direction.OUTPUT

# turn red = calibration

ledR.value = True
ledG.value = True
ledB.value = True

# init PWMs

pwmspk1 = pulseio.PWMOut(board.D1, duty_cycle=0x7fff, frequency=440, variable_frequency=True)
pwmspk2 = pulseio.PWMOut(board.D2, duty_cycle=0x7fff, frequency=440, variable_frequency=True)
pwmspk3 = pulseio.PWMOut(board.D3, duty_cycle=0x7fff, frequency=440, variable_frequency=True)

# use button values to set freqency, no sound if near low level

while True:
    for n in song:
        pwmspk1.frequency = int(round(notes[n[0][0]]))
        pwmspk1.duty_cycle = 0x7fff
        pwmspk2.frequency = int(round(notes[n[1][0]]))
        pwmspk2.duty_cycle = 0x7fff
        pwmspk3.frequency = int(round(notes[n[2][0]]))
        pwmspk3.duty_cycle = 0x7fff
        ledR.value = False
        ledG.value = False
        ledB.value = False
        for x in [0,8,4,2]:
            if n[0][1] == x:
                pwmspk1.duty_cycle = 0
                ledR.value = True
            if n[1][1] == x:
                pwmspk2.duty_cycle = 0
                ledG.value = True
            if n[2][1] == x:
                pwmspk3.duty_cycle = 0
                ledB.value = True
            time.sleep(.1)

