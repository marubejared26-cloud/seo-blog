import subprocess # New import to run terminal commands

class SEOHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"✨ New content detected: {event.src_path}")
            
            # 1. Run the SEO conversion
            create_seo_page(event.src_path, "Automated Post", "seo, termux, micro-saas")
            
            # 2. Automatically Push to GitHub
            try:
                # Add the new HTML file
                subprocess.run(["git", "add", "."], check=True)
                # Commit the change
                subprocess.run(["git", "commit", "-m", "Auto-update SEO content"], check=True)
                # Push to the web
                subprocess.run(["git", "push"], check=True)
                print("🚀 Website successfully updated and live!")
            except Exception as e:
                print(f"❌ Upload failed: {e}")

