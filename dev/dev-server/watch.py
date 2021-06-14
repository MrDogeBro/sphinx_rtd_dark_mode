from datetime import datetime, timedelta
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()

        print(event)


class Watcher:
    def __init__(self, source_path, docs_path):
        self.source_path = source_path
        self.docs_path = docs_path

    def watch(self):
        path = Path.joinpath(Path(__file__).resolve().parent, self.source_path)
        event_handler = EventHandler()
        observer = Observer()

        observer.schedule(event_handler, path, recursive=True)
        observer.start()

        try:
            while True:
                sleep(1)
        finally:
            observer.stop()
            observer.join()
