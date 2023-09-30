#Imports the time and datetime module for the timer
import time
import datetime

#I copied this timer thing from online lmao
def countdown(m):
 
    # Calculate the total number of seconds
    total_seconds = m * 60
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1

class Timer:
	#We attribute a length
	def __init__(self, length):
		self.length = length
	
	#Start a timer with the length specified in self.length
	def start_timer(self):
		countdown(self.length)
