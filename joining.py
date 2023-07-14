import threading
import time

# Function executed by a thread
def my_function():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

# Create a thread
t = threading.Thread(target=my_function)

# Start the thread
t.start()

# Wait for the thread to finish
# comment the next line to see the difference
t.join()

print("All threads finished")