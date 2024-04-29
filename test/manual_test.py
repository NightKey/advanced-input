import os, sys
parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, parent_dir)
from advanced_input import get_advanced_input, PriorityOrder
from threading import Thread
from time import sleep

input_handler = get_advanced_input()

def thread_one():
    user_input = input_handler.input(priority=PriorityOrder.High)
    print(user_input)

def main():
    backgroundThread = Thread(target=thread_one)
    backgroundThread.start()
    sleep(.1)
    input_handler.read("Press any character to exit...", PriorityOrder.Low)
    input_handler.stop()

main()
