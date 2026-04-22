import multiprocessing
import random
import time
from datetime import datetime

def worker(name):
    # Wait a random time between 0 and 1 seconds
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)

    # Print current time
    current_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f"Process {name}: {current_time}")

if __name__ == "__main__":
    processes = []

    # Create 3 processes
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i, ))
        processes.append(p)
        p.start()
    # Wait for all processes to finish
    for p in processes:
        p.join()
