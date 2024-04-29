from .input import AdvancedInput, is_input_ready, get_character_from_input
from .constants import PriorityOrder, EventType, EventWithType
current_input_extender: AdvancedInput = None

def get_advanced_input():
    global current_input_extender
    if current_input_extender is None:
        current_input_extender = AdvancedInput()
        current_input_extender.start()
    return current_input_extender
