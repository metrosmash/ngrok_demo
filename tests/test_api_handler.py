
import json
import threading
import urllib.request
import urllib.error
from http.server import HTTPServer
from src.random_numbers import APIHandler
import pytest



@pytest.fixture(scope="module")
def server():
    # Port 0 asks the OS for any free port, so tests don't clash with other programs
    httpd = HTTPServer(("localhost", 0), APIHandler)
    port = httpd.server_address[1]

    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    yield f"http://localhost:{port}"

    httpd.shutdown()
    httpd.server_close()


def get(url):
    """Return (status_code, parsed_json) for a GET request."""
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as err:
        return err.code, json.loads(err.read())


def test_root_returns_message(server):
    status, body = get(server + "/")
    assert status == 200
    assert body == {"message": "Hello from Python API"}


def test_root_returns_json_content_type(server):
    with urllib.request.urlopen(server + "/") as resp:
        assert resp.headers["Content-Type"] == "application/json"

def test_generate_random_number(server):
    status, body = get(server + "/generate_random_number")
    assert status  == 200
    assert type(body["Random_Number"]) == int

def test_generate_random_number_returns_json_content_type(server):
    with urllib.request.urlopen(server + "/generate_random_number") as resp:
        assert resp.headers["Content-Type"] == "application/json"


def test_unknown_path_returns_404(server):
    status, body = get(server + "/nope")
    assert status == 404
    assert body == {"Error": "Path not recognized"}
