from change_extractor import extract_pr_metadata


def main():
    print("Change Risk Agent started")

    pr_info = extract_pr_metadata()

    print("\n--- Pull Request Metadata ---")
    for key, value in pr_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
