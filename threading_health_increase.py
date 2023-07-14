import threading
import time
import sys
import os

# Global variable for health
health = 100

# Function for decreasing health over time
def decrease_health():
    global health
    while health > 0:
        health -= 1
        time.sleep(0.3)
        print(f"Health decreased. Current health: {health}", end="\r")

# Function for listening to user input and increasing health
def increase_health():
    global health
    while health > 0:
        input()  # Wait for user to press Enter
        if health < 100:
            health += 1
        else:
            health = 100
        try:
            os.system("clear")
        except:
            os.system("cls")
        print(f"Health increased. Current health: {health}", end="\r")

# Create and start the threads
decrease_thread = threading.Thread(target=decrease_health)
increase_thread = threading.Thread(target=increase_health)
decrease_thread.start()
increase_thread.start()

# Wait for the health to reach 0
decrease_thread.join()

# Stop the increase thread by exiting the program
sys.exit()

# homework
# --------------------------------------
# use another thread to decrease the sleep value over time using global variable 