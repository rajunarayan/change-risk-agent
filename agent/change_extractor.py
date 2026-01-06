import json
import os


def extract_pr_metadata():
    event_path = os.getenv("GITHUB_EVENT_PATH")

    if not event_path:
        raise RuntimeError("GITHUB_EVENT_PATH not found")

    with open(event_path, "r") as f:
        event_data = json.load(f)

    pull_request = event_data.get("pull_request", {})

    pr_info = {
        "pr_number": pull_request.get("number"),
        "title": pull_request.get("title"),
        "author": pull_request.get("user", {}).get("login"),
        "base_branch": pull_request.get("base", {}).get("ref"),
        "head_branch": pull_request.get("head", {}).get("ref"),
        "changed_files_count": pull_request.get("changed_files"),
        "additions": pull_request.get("additions"),
        "deletions": pull_request.get("deletions"),
        "created_at": pull_request.get("created_at"),
    }

    return pr_info
