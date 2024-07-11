import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class BotFileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print("Changes detected. Reloading bot...")
            subprocess.run(["python", "/app/main/bot.py"])


def main():
    path = '/app/main'  # Adjust this path as needed
    event_handler = BotFileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Bot watcher is running...")
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("Bot watcher stopped.")


if __name__ == "__main__":
    main()
