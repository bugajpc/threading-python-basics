import threading

# Global variable accessible by all threads
global_var = 0

# Function executed by each thread
def increment_global():
    global global_var
    global_var += 1

# Create multiple threads
threads = []
for _ in range(5):
    t = threading.Thread(target=increment_global)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(global_var)  # Output: 5