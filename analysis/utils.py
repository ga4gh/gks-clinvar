"""Module for utility functions.

Assumes you have a `.env` file at the root of the repository and contains
``CLINVAR_API_KEY`` with a valid API key to use the ClinVar Submission API
"""
from os import environ

import requests
from dotenv import load_dotenv

load_dotenv()

CLINVAR_PROD_API = "https://submit.ncbi.nlm.nih.gov/api/v1/submissions"
CLINVAR_TEST_API = "https://submit.ncbi.nlm.nih.gov/apitest/v1/submissions"
HEADERS = {"Content-type": "application/json", "SP-API-KEY": environ["CLINVAR_API_KEY"]}


def _get_submission_url(use_prod: bool = False, dry_run: bool = True) -> str:
    """Get ClinVar Submission API URL

    :param use_prod: Whether or not to use the production API
    :param dry_run: Whether or not to perform a dry run
    :return: URL
    """
    url = CLINVAR_PROD_API if use_prod else CLINVAR_TEST_API
    if dry_run:
        url += "/?dry-run=true"
    return url


def submit(
    submission: list[dict], use_prod: bool = False, dry_run: bool = True
) -> requests.Response:
    """Create submission via ClinVar Submission API

    :param submission: ClinVar submission
    :param use_prod: Whether or not to use the production API
    :param dry_run: Whether or not to perform a dry run
    :return: Response from ClinVar Submission API
    """
    payload = {
        "actions": [
            {"type": "AddData", "targetDb": "clinvar", "data": {"content": submission}}
        ]
    }
    url = _get_submission_url(use_prod, dry_run)
    return requests.post(url, headers=HEADERS, json=payload, timeout=5)


def get_sub_actions(submission_id: str, use_prod: bool = False) -> requests.Response:
    """Get submission status

    :param submission_id: Submission ID retrieved when the submission was created
    :param use_prod: Whether or not to use the production API
    :return: Response from ClinVar Submission API
    """
    url = _get_submission_url(use_prod, dry_run=False)
    return requests.get(f"{url}/{submission_id}/actions/", headers=HEADERS, timeout=5)


if __name__ == "__main__":
    import json
    from pathlib import Path

    root_dir = Path(__file__).resolve().parents[0]

    for source in {"civic", "varcat"}:
        for json_f in Path(root_dir / source).glob("*.json"):
            with json_f.open() as rf:
                sub_data = json.loads(rf.read())
                response = submit(sub_data, use_prod=False, dry_run=True)
                if response.status_code != 204:
                    print(f"{json_f} is invalid: {response.json()}")  # noqa: T201
                else:
                    print(f"{json_f} is valid")  # noqa: T201
