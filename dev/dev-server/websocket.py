import asyncio
from json import dumps as json_dumps
from typing import Set
from websockets import serve as websocket_serve
from websockets.legacy.server import WebSocketServerProtocol


class Websocket:
    def __init__(self) -> None:
        self.running = False
        self.connected: Set[WebSocketServerProtocol] = set()

    async def reload_clients(self) -> None:
        if self.connected:
            for client in self.connected:
                message = json_dumps({"type": "command", "command": "reload"})
                await asyncio.wait([client.send(message) for client in self.connected])

    async def register(self, websocket) -> None:
        self.connected.add(websocket)

    async def unregister(self, websocket) -> None:
        self.connected.remove(websocket)

    async def handler(self, websocket, path) -> None:
        await self.register(websocket)

        try:
            async for message in websocket:
                pass
        finally:
            await self.unregister(websocket)

    async def async_start(self) -> None:
        self.running = True
        async with websocket_serve(self.handler, "localhost", 5010):
            while self.running:
                await asyncio.sleep(1)

    def start(self) -> None:
        asyncio.run(self.async_start())

    async def stop(self) -> None:
        self.running = False
