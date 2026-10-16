# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.random_numbers import generate_random_number

def test_generate_random_num():
    assert generate_random_number(1, 10, is_test = True) == 1