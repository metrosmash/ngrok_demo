"""
This Script chooses a random number and exposes it to an api "/"
using python, random and request
"""
import random 
# import requests


def generate_random_number(min: int, max: int) -> int:
    """
    Generates a random number from the range of min to max 
    """
    random_number = random.randint(min, max)

    return random_number 

