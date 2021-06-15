import asyncio
from websockets import serve as websocket_serve


class Websocket:
    def __init__(self) -> None:
        self.running = False

    async def handler(self, websocket, path) -> None:
        async for message in websocket:
            await websocket.send(message)

    async def async_start(self) -> None:
        self.running = True
        async with websocket_serve(self.handler, "localhost", 5010):
            while self.running:
                await asyncio.sleep(1)

    def start(self) -> None:
        asyncio.run(self.async_start())

    async def stop(self) -> None:
        self.running = False
