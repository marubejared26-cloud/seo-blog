import markdown
import os

def create_seo_page(filename, title, keywords):
    if not os.path.exists(filename):
        print(f"❌ Error: {filename} not found.")
        return

    # 1. Read your raw writing
    with open(filename, 'r') as f:
        content = f.read()

    # 2. Convert Markdown to HTML
    html_content = markdown.markdown(content)

    # 3. Define the SEO Template
    seo_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="{content[:150].replace('"', "'")}...">
        <meta name="keywords" content="{keywords}">
        <title>{title}</title>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; color: #333; }}
            h1 {{ color: #2c3e50; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        {html_content}
    </body>
    </html>
    """

    # 4. Save the optimized file
    output_name = filename.replace(".md", ".html")
    with open(output_name, 'w') as f:
        f.write(seo_template)
    
    print(f"✅ SEO Optimized file created: {output_name}")

# --- QUICK TEST ---
# This creates a sample file if it doesn't exist
if not os.path.exists("test_blog.md"):
    with open("test_blog.md", "w") as f:
        f.write("# Hello World\nThis is my first SEO blog post written in Termux!")

create_seo_page("test_blog.md", "My Termux Blog", "termux, coding, seo")
