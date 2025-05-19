import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import subprocess

def get_merged_prs():
    cmd = [
        "gh", "pr", "list", "--base", "main", "--state", "merged",
        "--limit", "20", "--json", "number,title"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)

def get_pr_details(pr_number):
    cmd = ["gh", "pr", "view", str(pr_number), "--json", "comments,createdAt"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    pr = json.loads(result.stdout)
    comments = [c["body"] for c in pr.get("comments", [])]
    created_at = pr["createdAt"]
    # Add " UTC" to created_at
    return {
        "comments": comments,
        "created_at": datetime.fromisoformat(created_at.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S") + " UTC"
    }

def main():
    prs = get_merged_prs()
    for pr in prs:
        details = get_pr_details(pr["number"])
        pr["comments"] = details["comments"]
        pr["created_at"] = details["created_at"]

    # Fix tag extraction
    ref = os.environ.get("GITHUB_REF", "")
    tag = ref.split("/")[-1] if ref.startswith("refs/tags/") else ""

    # Use UTC time and append 'UTC'
    now = datetime.utcnow()
    data = {
        "version": tag,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S") + " UTC",
        "prs": prs,
    }

    print(data)  # Debug

    env = Environment(loader=FileSystemLoader(".github/templates"))
    template = env.get_template("release_template.md")
    output = template.render(data)

    with open("release_notes.md", "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()