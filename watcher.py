import build_index
import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from seo_tool import create_seo_page

class SEOHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Everything inside the function must be indented 8 spaces total
        if event.src_path.endswith(".md") and not os.path.basename(event.src_path).startswith('.'):
            print(f"✨ New content detected: {event.src_path}")
            
            title = os.path.basename(event.src_path).replace('.md', '').replace('_', ' ').title()
            create_seo_page(event.src_path, title, "automated-update")

            # Rebuild the index page
            build_index.generate()

            # Git Commands
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", f"Auto-update: {title}"], check=True)
                subprocess.run(["git", "push"], check=True)
                print("🚀 Website successfully updated!")
            except Exception as e:
                print(f"❌ Upload failed: {e}")

# This part tells the script how to stay alive and watch the folder
if __name__ == "__main__":
    path = "."
    event_handler = SEOHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("👀 Watcher is active... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

