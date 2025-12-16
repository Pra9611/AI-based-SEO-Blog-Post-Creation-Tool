import requests
import base64

def post_to_wordpress(title, content):
    WP_URL = "https://yourwebsite.com/wp-json/wp/v2/posts"
    USERNAME = "admin"
    PASSWORD = "application_password"

    token = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    headers = {
        "Authorization": f"Basic {token}"
    }

    post = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    response = requests.post(WP_URL, headers=headers, json=post)
    return response.json()
