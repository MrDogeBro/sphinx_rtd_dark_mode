import asyncio
from argparse import ArgumentParser
from colorama import Fore
from pathlib import Path
from signal import signal, SIGINT

from server import Server
from watch import Watcher


class Main:
    async def start(self) -> None:
        print(f"{Fore.CYAN}wait{Fore.RESET}    - starting server...")
        cwd = Path().cwd()

        parser = ArgumentParser()
        parser.add_argument("source_path")
        parser.add_argument("docs_path")
        args = parser.parse_args()

        source_path = Path.joinpath(cwd, args.source_path)
        docs_path = Path.joinpath(cwd, args.docs_path)

        self.watcher = Watcher(str(source_path), str(docs_path))
        self.server = Server()

        signal(SIGINT, self.stop)

        await self.server.start()
        await self.watcher.start()

    def stop(self, signal_received, frame) -> None:
        asyncio.get_running_loop().create_task(self.async_stop())

    async def async_stop(self) -> None:
        await self.server.stop()
        await self.watcher.stop()
        await asyncio.sleep(1)

        exit(0)


if __name__ == "__main__":
    asyncio.run(Main().start())
