import os
import requests


def post_pr_comment(pr_number, repo, comment_body):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not found")

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "body": comment_body
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
