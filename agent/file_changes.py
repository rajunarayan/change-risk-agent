import os
import requests


def get_changed_files(pr_number, repo_full_name):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not found")

    url = f"https://api.github.com/repos/{repo_full_name}/pulls/{pr_number}/files"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    files = response.json()

    return [
        {
            "filename": f["filename"],
            "status": f["status"],
            "additions": f["additions"],
            "deletions": f["deletions"]
        }
        for f in files
    ]


def classify_file(filename):
    if "test" in filename.lower():
        return "test"
    if filename.endswith((".yml", ".yaml", ".env", ".json")):
        return "config"
    return "code"
