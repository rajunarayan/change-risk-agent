def compute_risk_score(summary, additions):
    score = 0
    reasons = []

    # Code-heavy change
    if summary["code"] >= 3:
        score += 30
        reasons.append("Multiple code files modified")

    # No tests changed
    if summary["test"] == 0:
        score += 20
        reasons.append("No test files updated")

    # Config changes
    if summary["config"] > 0:
        score += 25
        reasons.append("Configuration files modified")

    # Large change size
    if additions > 50:
        score += 25
        reasons.append("Large number of lines added")

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, reasons
