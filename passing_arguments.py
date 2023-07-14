import threading

# Function with parameters
def greet(name):
    print("Hello,", name)

# Create a thread with function and arguments
t = threading.Thread(target=greet, args=("Alice",))

# Start the thread
t.start()

# Wait for the thread to finish
t.join()

print("Thread finished")