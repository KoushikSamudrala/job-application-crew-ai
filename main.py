"""CLI entry point for the Job Application Crew AI."""

import argparse
from config import validate_env
from crew import run_crew


def parse_args():
    parser = argparse.ArgumentParser(
        description="Job Application Crew AI — tailor your resume and prep for interviews."
    )
    parser.add_argument(
        "--job-url",
        required=True,
        help="URL of the job posting to analyze.",
    )
    parser.add_argument(
        "--github-url",
        required=True,
        help="Your GitHub profile URL.",
    )
    parser.add_argument(
        "--writeup",
        required=True,
        help="A short personal summary about yourself (in quotes).",
    )
    return parser.parse_args()


def main():
    validate_env()
    args = parse_args()

    print("\n🚀 Starting Job Application Crew...\n")
    print(f"  📌 Job Posting : {args.job_url}")
    print(f"  👤 GitHub URL  : {args.github_url}")
    print(f"  📝 Writeup     : {args.writeup[:80]}...\n")

    result = run_crew(
        job_posting_url=args.job_url,
        github_url=args.github_url,
        personal_writeup=args.writeup,
    )

    print("\n✅ Crew finished! Check the outputs/ folder for:")
    print("   - outputs/tailored_resume.md")
    print("   - outputs/interview_materials.md")
    return result


if __name__ == "__main__":
    main()
