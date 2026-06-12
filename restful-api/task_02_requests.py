import csv
import requests


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        formatted_posts = []
        for post in posts:
            data = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            formatted_posts.append(data)
        fieldnames = ["id", "title", "body"]
        with open("posts.csv", mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(formatted_posts)
