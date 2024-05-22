# VarCat Test Submissions

This directory contains VarCat overall assessments that were transformed to ClinVar Test API JSON Schema.

A batch submission was manually created using:

* `GET assertions/variation_assertions/{id}`:
  * variation, disease, gene
* `POST assertions/overall_assessment_summary/{id}`:
  * classification information
* UI:
  * Total score

More information about the ClinVar Submission API:\
GitHub repo: <https://github.com/ncbi/clinvar/tree/master/submission_api_schema>\
Test endpoint: <https://submit.ncbi.nlm.nih.gov/apitest/v1/submissions>\
Submission API documentation: <https://www.ncbi.nlm.nih.gov/clinvar/docs/api_http/>
