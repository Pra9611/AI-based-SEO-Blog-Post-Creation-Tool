from fastapi import FastAPI
from scraper import scrape_products
from SEO_keywords import extract_keywords
from blog_generator import generate_blog
from publisher import save_blog

app = FastAPI(title="AI SEO Blog Tool")

@app.get("/generate-blog")
def generate_blog_api():
    products = scrape_products()
    product = products[0]

    text_for_keywords = product["title"]
    keywords = extract_keywords(text_for_keywords)

    blog = generate_blog(product, keywords)
    file = save_blog(blog, product["title"])

    return {
        "product": product,
        "seo_keywords": keywords,
        "blog_file": file,
        "status": "Blog generated successfully"
    }
