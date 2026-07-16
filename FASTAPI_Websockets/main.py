from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, exclude: WebSocket = None):
        for connection in self.active_connections:
            if connection != exclude:
                await connection.send_text(message)

    
manager = ConnectionManager()

# Read the HTML file directly and serve it at the root URL
@app.get("/")
async def get():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# WebSocket endpoint for handling real-time communication
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            # Send private confirmation to sender
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            # Send message to everyone else
            await manager.broadcast(f"Client #{client_id} says: {data}", exclude=websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} has left the chat")