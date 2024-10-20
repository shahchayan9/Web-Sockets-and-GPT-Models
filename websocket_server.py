import asyncio
import websockets
import random

async def echo(websocket, path):
    async for message in websocket:
        random_number = random.randint(1, 100)
        modified_message = f"{message} {random_number}"
        
        print(f"Received: {message}, Modified: {modified_message}")
        
        await websocket.send(modified_message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket Server started at ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
