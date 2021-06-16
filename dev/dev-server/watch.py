import asyncio
from colorama import Fore
from datetime import datetime as dt, timedelta
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from build import Builder
from websocket import Websocket


class EventHandler(FileSystemEventHandler):
    def __init__(self, source_path: str, docs_path: str, websocket: Websocket) -> None:
        self.last_modified = dt.now()
        self.builder = Builder(source_path, docs_path)
        self.websocket = websocket

    def on_any_event(self, event) -> None:
        if dt.now() - self.last_modified < timedelta(seconds=1):
            return

        if event.src_path.split("/")[-1].split(".").count("py") > 1:
            return

        print(f"{Fore.CYAN}wait{Fore.RESET}  - building...")
        self.last_modified = dt.now()
        build_output = self.builder.build()

        try:
            if build_output.status != 0:
                print(f"{Fore.RED}error{Fore.RESET} - build failed")
                print(f"Traceback:\n{build_output.traceback}")
                return
        except AttributeError:
            print(f"{Fore.RED}error{Fore.RESET} - build failed")
            print(
                f"Traceback:\n\nIt seems that the build did not complete. Please try again."
            )

        asyncio.run(self.websocket.reload_clients())
        print(f"{Fore.MAGENTA}event{Fore.RESET} - build successful")


class Watcher:
    def __init__(self, source_path: str, docs_path: str) -> None:
        self.source_path = source_path
        self.docs_path = docs_path
        self.running = False

        self.observer = Observer()
        self.websocket = Websocket()

    async def start(self) -> None:
        self.running = True
        path = Path.joinpath(Path(__file__).resolve().parent, self.source_path)
        event_handler = EventHandler(self.source_path, self.docs_path, self.websocket)

        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.websocket.start)

        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

        while self.running:
            await asyncio.sleep(1)

        await self.websocket.stop()
        self.observer.stop()
        self.observer.join()

    async def stop(self) -> None:
        self.running = False
