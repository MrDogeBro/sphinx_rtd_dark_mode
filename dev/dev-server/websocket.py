import asyncio
from websockets import serve as websocket_serve


class Websocket:
    async def socket_handler(self, websocket, path):
        async for message in websocket:
            await websocket.send(message)

    def start(self):
        asyncio.get_event_loop().run_until_complete(
            websocket_serve(self.socket_handler, "localhost", 5010)
        )
        asyncio.get_event_loop().run_forever()


Websocket().start()
