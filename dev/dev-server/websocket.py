import asyncio
from websockets import serve as websocket_serve


class Websocket:
    async def handler(self, websocket, path):
        async for message in websocket:
            await websocket.send(message)

    async def async_start(self):
        async with websocket_serve(self.handler, "localhost", 5010):
            await asyncio.Future()

    def start(self):
        asyncio.run(self.async_start())
