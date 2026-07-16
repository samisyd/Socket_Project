# FastAPI WebSockets

A simple real-time chat application built with FastAPI and WebSockets. The app serves a browser-based chat interface and broadcasts messages between connected clients.

## Features

- Real-time messaging over WebSockets
- Broadcast messages to all connected clients except the sender
- Send a private confirmation back to the sender
- Simple HTML/JavaScript front end served by FastAPI

## Project Files

- [main.py](main.py) — FastAPI app and WebSocket endpoint
- [index.html](index.html) — Chat UI and client-side WebSocket logic
- [pyproject.toml](pyproject.toml) — Project dependencies and metadata

## Requirements

- Python 3.13+
- FastAPI
- Uvicorn
- WebSockets

## Installation

Using `uv`:

```bash
uv sync
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

## Running the App

Start the development server:

```bash
uv run uvicorn main:app --reload
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

## Usage

1. Open the app in your browser.
2. A unique client ID is generated automatically.
3. Enter a message and press Send.
4. Your message will appear in the chat and be broadcast to other connected clients.

## Notes

This project is based on the FastAPI WebSocket tutorial:
https://fastapi.tiangolo.com/advanced/websockets/
