#!/usr/bin/python3
"""
Module for fetching and processing posts from a REST API.

This module provides functions to fetch posts from the JSONPlaceholder
API and either print them or save them to a CSV file.
"""
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print their titles.

    Retrieves all posts from the JSONPlaceholder API and prints the
    HTTP status code of the response. If successful, prints the title
    of each post.

    Args:
        None

    Returns:
        None
    """
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save them to a CSV file.

    Retrieves all posts from the JSONPlaceholder API and saves the
    post ID, title, and body to a CSV file named 'posts.csv'.

    Args:
        None

    Returns:
        None
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })


"""
Module for fetching and processing posts from a REST API.

This module provides functions to fetch posts from the JSONPlaceholder
API and either print them or save them to a CSV file.
"""

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print their titles.

    Retrieves all posts from the JSONPlaceholder API and prints the
    HTTP status code of the response. If successful, prints the title
    of each post.

    Args:
        None

    Returns:
        None
    """
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save them to a CSV file.

    Retrieves all posts from the JSONPlaceholder API and saves the
    post ID, title, and body to a CSV file named 'posts.csv'.

    Args:
        None

    Returns:
        None
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
