def save_blog(blog_content, title):
    filename = title.replace(" ", "_") + ".html"
    WP_URL = "https://yourwebsite.com/wp-json/wp/v2/posts"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(blog_content)
    return filename

