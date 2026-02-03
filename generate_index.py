import os

def build_index():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    
    links = ""
    for file in html_files:
        title = file.replace(".html", "").replace("_", " ").title()
        links += f'<li><a href="{file}">{title}</a></li>\n'

    index_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My SEO Blog</title>
        <style>
            body {{ font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
            h1 {{ color: #2563eb; border-bottom: 2px solid #2563eb; padding-bottom: 10px; }}
            ul {{ list-style: none; padding: 0; }}
            li {{ margin: 15px 0; padding: 10px; background: #f3f4f6; border-radius: 8px; }}
            a {{ text-decoration: none; color: #1f2937; font-weight: bold; display: block; }}
            a:hover {{ color: #2563eb; }}
        </style>
    </head>
    <body>
        <h1>Latest Articles</h1>
        <ul>
            {links}
        </ul>
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(index_html)
    print("🏠 Index page updated!")

if __name__ == "__main__":
    build_index()
