import markdown
import time  # <--- Make sure this is here!

def create_seo_page(md_file, title, keywords):
    with open(md_file, "r") as f:
        content = markdown.markdown(f.read())

    # This is the template that was giving the error
    seo_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <meta name="keywords" content="{keywords}">
        <style>
            :root {{ --primary: #2563eb; --text: #1f2937; --bg: #f9fafb; }}
            body {{ font-family: sans-serif; line-height: 1.7; max-width: 750px; margin: 40px auto; padding: 0 20px; color: var(--text); background: var(--bg); }}
            h1 {{ font-size: 2.5rem; color: #111827; }}
            .meta {{ font-size: 0.9rem; color: #6b7280; border-bottom: 1px solid #e5e7eb; padding-bottom: 20px; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <div class="meta">Published on {time.strftime('%B %d, %Y')}</div>
        <div class="content">
            {content}
        </div>
    </body>
    </html>
    """
    
    output_file = md_file.replace(".md", ".html")
    with open(output_file, "w") as f:
        f.write(seo_template)
    print(f"✅ SEO Optimized file created: {output_file}")

