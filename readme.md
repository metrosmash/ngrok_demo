# ngrok Demo

A small learning project exploring how to build an HTTP API using only Python's standard library, then make that API reachable from outside the device running it with ngrok.

The API uses `http.server` for HTTP handling and `json` to format responses. It does not use a web framework or third-party runtime packages. ngrok provides a public tunnel to the locally running API; it does not deploy or host the application.

## API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message. |
| `GET` | `/generate_random_number` | Returns a random integer from 1 through 10. |

Example responses:

```json
{"message": "Hello from Python API"}
```

```json
{"Random_Number": 7}
```

Unknown paths return a JSON error with HTTP status `404`.

## Run locally

Python 3.14 is used by the Docker image, Dev Container, and CI workflow.

Start the API from the repository root:

```bash
python -m src.random_numbers
```

The server listens on port `5000`. While it is running, visit `http://localhost:5000/` or `http://localhost:5000/generate_random_number`. Stop it with `Ctrl+C`.

## Expose the API with ngrok

1. Install ngrok and configure it with your ngrok account's authentication token, following the [ngrok setup guide](https://ngrok.com/docs/getting-started/).
2. Start the API locally using the command above.
3. In a second terminal, start a tunnel to the API port:

   ```bash
   ngrok http 5000
   ```

4. Open the HTTPS forwarding URL printed by ngrok, adding `/` or `/generate_random_number` to test the endpoints.

Keep both the API and ngrok processes running while using the public URL. The URL and access are controlled by ngrok and may change when the tunnel restarts. Treat the forwarding URL as public, and never commit your ngrok authentication token to this repository.

## Run with Docker Compose

If Docker Engine and the Compose plugin are available, start the API from the repository root:

```bash
docker compose up --build
```

Compose publishes container port `5000` on host port `8000`. Visit `http://localhost:8000/` to test it. To expose this container through ngrok, run the tunnel on the host against port `8000`:

```bash
ngrok http 8000
```

Stop Compose with `Ctrl+C`; remove the stopped container with `docker compose down`.

## Tests

Install the development dependencies and run pytest:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

GitHub Actions runs the tests and builds the Docker image on pushes.

## Development container

Install the VS Code Dev Containers extension, open this repository in VS Code, then run **Dev Containers: Reopen in Container** from the Command Palette. The Dev Container uses Python 3.14, installs `requirements-dev.txt`, and includes the GitHub Actions extension.
