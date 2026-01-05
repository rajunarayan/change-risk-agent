import os
from change_extractor import extract_pr_metadata
from file_changes import get_changed_files, classify_file


def main():
    print("Change Risk Agent started")

    pr_info = extract_pr_metadata()

    repo = os.getenv("GITHUB_REPOSITORY")
    pr_number = pr_info["pr_number"]

    files = get_changed_files(pr_number, repo)

    print("\n--- Changed Files ---")
    summary = {"code": 0, "test": 0, "config": 0}

    for f in files:
        category = classify_file(f["filename"])
        summary[category] += 1

        print(
            f"- {f['filename']} | {category} | +{f['additions']} / -{f['deletions']}"
        )

    print("\n--- Change Summary ---")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
