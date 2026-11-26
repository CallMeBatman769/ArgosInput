import time
from pynput import mouse
import math
COUNTDOWN = ["5", "4", "3", "2", "1"]
MOVEMENT_SPEED = []
AVERAGES = []

#The needed tests for it to calculate the average
NEEDED_TESTS = 2

#Time it captures the movement for in seconds.
TEST_TIME = 20

previous_position = None
previous_time = None

def on_move(x, y):
    global MOVEMENT_SPEED, previous_position, previous_time

    current_time = time.perf_counter()
    current_position = (x, y)

    if previous_position is not None:

        dx = x - previous_position[0]
        dy = y - previous_position[1]

        distance = math.sqrt(dx**2 + dy**2)
        elapsed = current_time - previous_time

        if elapsed > 0:
            speed = distance / elapsed
            #print(f"Speed: {speed:.2f} pixels/seconds")

        MOVEMENT_SPEED.append(speed)
    previous_position = current_position
    previous_time = current_time

def start_test():
        previous_position = None
        previous_time = None
        print("Getting speed...")
        listener = mouse.Listener(on_move=on_move)
        listener.start()
        time.sleep(TEST_TIME)
        listener.stop()
        listener.join()

def main():
    global previous_time, previous_position, MOVEMENT_SPEED
    average = 0
    print("Recording begins in")
    for num in COUNTDOWN:
        print(num)
        time.sleep(1)
    for i in range(NEEDED_TESTS):
        start_test()
    #print(f"Measured speeds: {MOVEMENT_SPEED}")
    average = sum(MOVEMENT_SPEED) / len(MOVEMENT_SPEED)
    MOVEMENT_SPEED = []
    print(f"Average speed for user one: {average}")
    AVERAGES.append(average)
    average = 0
    print("Starting test two...")
    for num2 in COUNTDOWN:
         print(num2)
         time.sleep(1)
    for i in range(NEEDED_TESTS):
         start_test()
    average = sum(MOVEMENT_SPEED) / len(MOVEMENT_SPEED)
    AVERAGES.append(average)

    difference = abs(AVERAGES[0] - AVERAGES[1])

    percentage = difference / AVERAGES[0] * 100
    if percentage <= 5:
         print("Likely same person")
    else:
         print("Different person")
    

if __name__ == "__main__":
    main()