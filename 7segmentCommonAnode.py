import RPi.GPIO as io
import time

io.setmode(io.BOARD)

a=7
b=11
c=12
d=13
e=15
f=16
g=18

s1 = 19
s2 = 21


io.setup(a, io.OUT)
io.setup(b, io.OUT)
io.setup(c, io.OUT)
io.setup(d, io.OUT)
io.setup(e, io.OUT)
io.setup(f, io.OUT)
io.setup(g, io.OUT)
io.setup(s1, io.OUT)
io.setup(s2, io.OUT)


def segment1(digit):
	if (digit == 0):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.LOW)
		io.output(f, io.LOW)
		io.output(g, io.HIGH)
	elif (digit == 1):
		io.output(a, io.HIGH)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.HIGH)
		io.output(e, io.HIGH)
		io.output(f, io.HIGH)
		io.output(g, io.HIGH)
	elif (digit == 2):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.HIGH)
		io.output(d, io.LOW)
		io.output(e, io.LOW)
		io.output(f, io.HIGH)
		io.output(g, io.LOW)
	elif (digit == 3):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.HIGH)
		io.output(f, io.HIGH)
		io.output(g, io.LOW)
	elif (digit == 4):
		io.output(a, io.HIGH)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.HIGH)
		io.output(e, io.HIGH)
		io.output(f, io.LOW)
		io.output(g, io.LOW)
	elif (digit == 5):
		io.output(a, io.LOW)
		io.output(b, io.HIGH)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.HIGH)
		io.output(f, io.LOW)
		io.output(g, io.LOW)
	elif (digit == 6):
		io.output(a, io.LOW)
		io.output(b, io.HIGH)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.LOW)
		io.output(f, io.LOW)
		io.output(g, io.LOW)
	elif (digit == 7):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.HIGH)
		io.output(e, io.HIGH)
		io.output(f, io.HIGH)
		io.output(g, io.HIGH)
	elif (digit == 8):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.LOW)
		io.output(f, io.LOW)
		io.output(g, io.LOW)
	elif (digit == 9):
		io.output(a, io.LOW)
		io.output(b, io.LOW)
		io.output(c, io.LOW)
		io.output(d, io.LOW)
		io.output(e, io.HIGH)
		io.output(f, io.LOW)
		io.output(g, io.LOW)
		
while True:
		for tens in range(0,10,+1):
			for ones in range(0,10,+1):
				for repeat in range(25):
					io.output(s1,io.LOW)
					io.output(s2,io.HIGH)
					segment1(ones)
					time.sleep(0.002)
					io.output(s1,io.HIGH)
					io.output(s2,io.LOW)
					segment1(tens)
					time.sleep(0.002)

					