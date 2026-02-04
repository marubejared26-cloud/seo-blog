import os

def generate():
    print("🔍 Scanning for posts to update index...")
    posts = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

    with open("index.html", "w") as f:
        f.write("<html><body><h1>My Termux Blog Index</h1><ul>")
        for post in posts:
            f.write(f'<li><a href="{post}">{post}</a></li>')
        f.write("</ul></body></html>")

    print("✅ index.html has been updated!")
