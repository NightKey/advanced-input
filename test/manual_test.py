import os, sys
parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, parent_dir)
from advanced_input import get_advanced_input, PriorityOrder
from threading import Thread
from time import sleep

input_handler = get_advanced_input()

def thread_one():
    while (user_input := input_handler.read(priority=PriorityOrder.High)) != "\n":
        print(user_input)

def main():
    backgroundThread = Thread(target=thread_one)
    backgroundThread.start()
    sleep(.1)
    a = input_handler.read("Press any character to exit...", PriorityOrder.Low)
    print(a)
    input_handler.stop()

main()
