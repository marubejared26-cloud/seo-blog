import os
import re

def generate():
    print("🔍 Extracting titles and updating index...")
    posts = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    
    links = []
    for post in posts:
        with open(post, 'r') as f:
            content = f.read()
            # Use regex to find whatever is between <title> tags
            match = re.search(r'<title>(.*?)</title>', content)
            title = match.group(1) if match else post
            links.append((post, title))

    with open("index.html", "w") as f:
        f.write("<html><head><style>body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:0 20px;line-height:1.6;color:#333;}</style></head>")
        f.write("<body><h1>My Termux Blog</h1><hr><ul>")
        for file, title in links:
            f.write(f'<li><a href="{file}" style="text-decoration:none;color:#007bff;font-weight:bold;">{title}</a></li>')
        f.write("</ul></body></html>")
            
    print("✅ Professional index.html created!")

