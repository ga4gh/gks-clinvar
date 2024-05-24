# Analysis

Analysis for ClinVar Submission Test API.

## General

* The Submission API is limited in the amount of information that can be
submitted compared to spreadsheet submission.
  * For example, `Variant: variation identifiers, alternate designations, URL` are found
    in the spreadsheet submission, but cannot be submitted via Submission API.

### Validation

The [validation notebook](./validation.ipynb) contains invalid submissions to evaluate
how the ClinVar Submission API handles validation. Submissions fail when JSON Schema
validation fails. The ClinVar Submission API does not appear to do data validation.

JSON Schema validation errors are formatted as:

```json
{
  "message": "Validation failed, see errors for detailed description",
  "errors": [
    {
      "message": ERROR_MESSAGE,
      "code": null,
      "identifier": null
    },
    ...
  ]
}
```

We have not run into instances where code and identifier are not null.

## CIViC

The [civic](./civic/) directory contains CIViC evidence items and assertions that were
transformed to the ClinVar Submission Test API JSON Schema.

[create_civic_therapy_submissions.ipynb](./create_civic_therapy_submissions.ipynb) was
used to programmatically generate CIViC evidence item submissions for a single therapy,
combination therapy, and batch containing a mix of single and combination therapies.
To run, the notebook assumes you have a `.env` file at the root of the repository and
contains `CLINVAR_API_KEY` with a valid API key to use the ClinVar Submission API.

Since there are currently no GKS models for prognostic/ diagnostic evidence and
assertions, these were manually created submissions from <https://civicdb.org>.

### CIViC data we can't put into ClinVar

* We can't represent substitute therapy groups nicely
  * The solution that CIViC team uses is creating duplicate submissions for each therapy
* Drug DB identifiers
  * We can use our normalized label, but it would be nice to be able to use our
    normalized concept identifier to prevent ambiguity

### What CIViC data we can put in ClinVar, but doesn't work with GKS

* `clinicalImpactClassificationDescription`
  * CIViC does not provide a mapping to AMP/ASCO/CAP and instead only provides a CIViC
    level for evidence items. We have an internal mapping to get the associated
    AMP/ASCO/CAP tier which relies on the indication information in the `extensions`. We
    need a way to represent these nicely and not have to rely on the `extensions` field.

### GKS lacking classes for CIViC data

* Prognostic / Diagnostic profiles
* CIViC assertions

## VarCat

The [varcat](./varcat/) directory contains VarCat overall assessments that were
transformed to the ClinVar Test API JSON Schema.

A batch submission was manually created using the following VarCat resources:

* `GET assertions/variation_assertions/{id}`:
  * variation, disease, gene
* `POST assertions/overall_assessment_summary/{id}`:
  * classification information
* UI:
  * Total score

### What VarCat data we can't put into ClinVar

* We can't represent structured evidence codes at the moment, so we had to stick this in
  information in the `comment`.

### GKS lacking classes for VarCat

* At the moment, we don't use GKS oncogenicity profiles in VarCat so this was not
  determined during the analysis.
