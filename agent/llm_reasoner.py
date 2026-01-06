import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_llm_risk_insights(pr_info, files, summary):
    prompt = f"""
You are a senior software reliability engineer.

Analyze this pull request for semantic deployment risks.

PR Title: {pr_info['title']}
Author: {pr_info['author']}
Files Changed: {[f['filename'] for f in files]}
Change Summary: {summary}

Respond with:
- Additional risk insights (if any)
- Patterns that may cause production issues
- Concise bullet points only
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You analyze deployment risks."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
