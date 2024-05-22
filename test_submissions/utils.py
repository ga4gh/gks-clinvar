"""Module for utility functions.

Assumes you have a `.env` file at the root of the repository and contains
``CLINVAR_API_KEY`` with a valid API key to use the ClinVar Submission API
"""
from os import environ

import requests
from dotenv import load_dotenv

load_dotenv()

TEST_URL = "https://submit.ncbi.nlm.nih.gov/apitest/v1/submissions"
HEADERS = {"Content-type": "application/json", "SP-API-KEY": environ["CLINVAR_API_KEY"]}


def dry_run_test_api(submission: list[dict]) -> requests.Response:
    """Perform a dry run using ClinVar Submission Test API

    :param submission: ClinVar submission
    :return: Response from ClinVar Submission Test API
    """
    payload = {
        "actions": [
            {"type": "AddData", "targetDb": "clinvar", "data": {"content": submission}}
        ]
    }

    return requests.post(
        f"{TEST_URL}/?dry-run=true", headers=HEADERS, json=payload, timeout=5
    )


def test_api_sub_actions(submission_id: str) -> requests.Response:
    """Get submission status

    :param submission_id: Submission ID retrieved when the submission was created
    :return: Response from ClinVar Submission Test API
    """
    return requests.get(
        f"{TEST_URL}/{submission_id}/actions/", headers=HEADERS, timeout=5
    )


if __name__ == "__main__":
    import json
    from pathlib import Path

    root_dir = Path(__file__).resolve().parents[0]

    for source in {"civic", "varcat"}:
        for json_f in Path(root_dir / source).glob("*.json"):
            with json_f.open() as rf:
                sub_data = json.loads(rf.read())
                response = dry_run_test_api(sub_data)
                if response.status_code != 204:
                    print(f"{json_f} is invalid: {response.json()}")  # noqa: T201
                else:
                    print(f"{json_f} is valid")  # noqa: T201
