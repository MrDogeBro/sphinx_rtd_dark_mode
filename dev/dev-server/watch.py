from datetime import datetime as dt, timedelta
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from build import Builder


class EventHandler(FileSystemEventHandler):
    def __init__(self, source_path: str, docs_path: str) -> None:
        self.last_modified = dt.now()
        self.builder = Builder(source_path, docs_path)

    def on_any_event(self, event) -> None:
        if dt.now() - self.last_modified < timedelta(seconds=1):
            return

        if event.src_path.split("/")[-1].split(".").count("py") > 1:
            return

        self.last_modified = dt.now()
        build_output = self.builder.build()


class Watcher:
    def __init__(self, source_path: str, docs_path: str) -> None:
        self.source_path = source_path
        self.docs_path = docs_path

        self.observer = Observer()

    def watch(self) -> None:
        path = Path.joinpath(Path(__file__).resolve().parent, self.source_path)
        event_handler = EventHandler(self.source_path, self.docs_path)

        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        finally:
            self.observer.join()
