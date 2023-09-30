#Import the timer class
from timer import Timer
#Two timer objects, one work and one for break
work_timer = Timer(25)
break_timer = Timer(5)

#This is some wizard magic the looks for any key interrupt on linux and returns something when it happens, idk how it works I found it on stack overflow
def wait_for_any_input():
     import sys, tty, termios
     fd = sys.stdin.fileno()
     old = termios.tcgetattr(fd)
     try:
          tty.setraw(fd)
          return sys.stdin.read(1)
     finally:
          termios.tcsetattr(fd, termios.TCSADRAIN, old)

#This runs a work timer for 25 minutes, then a break timer for 5
def pomodoro():
	work_timer.start_timer()
	print("Ok, time for a 5 minute break!")
	break_timer.start_timer()

#Asks the user how many sessions they want, if it is not an integer, it asks again
repetitions = input("How many work sessions do you want to do? ")
while True:
	try:
		repetitions = int(repetitions)
		break
	except:
		repetitions = input("Integers only, try again! ")
		

#Waits until the user presses any key on the keyboard then starts the timer
print("Press any key to start")
wait_for_any_input()

#Does a pomodoro session the amount of times specified by the user
for x in range(repetitions):
	pomodoro()