import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from seo_tool import create_seo_page

class SEOHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # We check for .md files and ignore temporary/hidden files
        if event.src_path.endswith(".md") and not event.src_path.startswith("./."):
            print(f"✨ New content detected: {event.src_path}")
            
            # 1. Run the SEO conversion
            # We use the filename as a temporary title
            title = os.path.basename(event.src_path).replace(".md", "").replace("_", " ").title()
            create_seo_page(event.src_path, title, "automation, termux, seo")
            
            # 2. Automatically Push to GitHub
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", f"Auto-update: {title}"], check=True)
                subprocess.run(["git", "push"], check=True)
                print("🚀 Website successfully updated and live!")
            except Exception as e:
                print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    path = "." 
    event_handler = SEOHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("🚀 SEO Watcher is active... Save a .md file here to auto-publish!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



