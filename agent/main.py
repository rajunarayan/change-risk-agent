import os
from change_extractor import extract_pr_metadata
from file_changes import get_changed_files, classify_file
from risk_engine import compute_risk_score
from llm_reasoner import get_llm_risk_insights
from pr_commenter import post_pr_comment





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

    total_additions = sum(f["additions"] for f in files)

    score, level, reasons = compute_risk_score(summary, total_additions)

    print("\n--- Risk Assessment ---")
    print(f"Risk Score: {score}")
    print(f"Risk Level: {level}")

    print("\nReasons:")
    for r in reasons:
        print(f"- {r}")

    print("\n--- LLM Semantic Risk Insights ---")

    llm_insights = get_llm_risk_insights(pr_info, files, summary)
    print(llm_insights)
        
    repo = os.getenv("GITHUB_REPOSITORY")

    comment = f"""
    ⚠️ **Change Risk Assessment**

    **Risk Score:** {score}  
    **Risk Level:** {level}

    ### Deterministic Risk Signals
    """
    for r in reasons:
        comment += f"- {r}\n"

    comment += "\n### LLM Semantic Risk Insights\n"
    comment += llm_insights

    post_pr_comment(pr_number, repo, comment)

    print("\nPR comment posted successfully.")



if __name__ == "__main__":
    main()
