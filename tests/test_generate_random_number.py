import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.random_numbers import generate_random_number


var = generate_random_number(0, 10)
print(var)