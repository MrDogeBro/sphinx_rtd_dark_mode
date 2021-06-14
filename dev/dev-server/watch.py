from datetime import datetime as dt, timedelta
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = dt.now()

    def on_any_event(self, event):
        if dt.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = dt.now()


class Watcher:
    def __init__(self, source_path, docs_path):
        self.source_path = source_path
        self.docs_path = docs_path

        self.observer = Observer()

    def watch(self):
        path = Path.joinpath(Path(__file__).resolve().parent, self.source_path)
        event_handler = EventHandler()

        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        finally:
            self.observer.join()
