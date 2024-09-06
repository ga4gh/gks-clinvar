# CIViC Test Submissions

This directory contains CIViC evidence items and assertions that were transformed to
ClinVar Submission Test API JSON Schema.

[create_civic_therapy_submissions.ipynb](./create_civic_therapy_submissions.ipynb) was
used to programmatically generate CIViC evidence item submissions for a single therapy,
combination therapy, and batch containing a mix of single and combination therapies.
To run, the notebook assumes you have a `.env` file at the root of the repository and
contains `CLINVAR_API_KEY` with a valid API key to use the ClinVar Submission API.

Since there are currently no GKS models for prognostic/ diagnostic evidence and
assertions, these were manually created submissions from <https://civicdb.org>.

More information about the ClinVar Submission API:\
GitHub repo: <https://github.com/ncbi/clinvar/tree/master/submission_api_schema>\
Test endpoint: <https://submit.ncbi.nlm.nih.gov/apitest/v1/submissions>\
Submission API documentation: <https://www.ncbi.nlm.nih.gov/clinvar/docs/api_http/>
