"""
This Script chooses a random number and exposes it to an api "/"
using python, random and request
"""
import random 
from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler
import json


MIN = 1
MAX = 10
RANDOM_SEED = 43


def generate_random_number(min: int, max: int, random_seed: int = RANDOM_SEED, is_test: Bool = False) -> int:
    """
    Generates a random number from the range of min to max 
    """
    if is_test == True:
        random.seed(random_seed)
    random_number = random.randint(min, max)

    return random_number 


class APIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        request_path = self.path
        
        if request_path == "/":
            response = {"message":"Hello from Python API"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))

        elif request_path == "/generate_random_number":
            random_number = generate_random_number(MIN, MAX)
            response = {"Random_Number": random_number}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))

        else:
            response = {"Error": "Path not recognized"}
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        

