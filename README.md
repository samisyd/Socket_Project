# Python Sockets

This project demonstrates a simple TCP client/server communication example using Python sockets.

## Project Files

- `server.py` - Starts a TCP server that listens on port `9999` and responds to client requests.
- `client.py` - Connects to the server and lets you request the current time or date.
- `main.py` - A minimal starter script.
- `pyproject.toml` - Project metadata for the Python environment.

## Requirements

- Python 3.13+
- `uv` (recommended) or a standard Python installation

## Run the Server

From the project folder, start the server:

```bash
uv run python server.py
```

Or, if you are using plain Python:

```bash
python server.py
```

## Run the Client

Open a second terminal and run:

```bash
uv run python client.py
```

Or:

```bash
python client.py
```

## How It Works

1. The server listens for incoming TCP connections on `localhost:9999`.
2. The client connects to the server.
3. The server sends a welcome message and waits for a request.
4. The client can send:
   - `1` to receive the current time
   - `2` to receive the current date
   - `0` to exit

## Notes

- The server uses `localhost` for local testing.
- If you see a connection error, make sure the server is running before starting the client.
- Press `Ctrl+C` in the server terminal to stop the server gracefully.
