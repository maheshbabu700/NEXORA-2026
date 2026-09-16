# AI Usage

## How AI tools were used

AI tools were used during development to help with:

- Understanding the challenge requirements.
- Planning the project structure.
- Writing and improving Python code.
- Understanding Python errors and fixing coding issues.
- Explaining the telemetry data and ranking approach.
- Checking the required `predictions.csv` format.
- Preparing documentation and explanations.

## Human verification

The generated code and suggestions were reviewed and tested manually.

I ran the data loading and ranking pipeline and checked that the expected output was produced.

I also ran the official `validate_submission.py` validator on `predictions.csv`.

The validator confirmed:

`predictions.csv: OK`

with 15 ranked gateways for each of the 8 required weeks.

## One thing AI got wrong

During development, an AI-generated code suggestion used an incorrect telemetry column name.

The actual telemetry data contained:

`rscp_rsrp_bad`

instead of the incorrectly suggested column name.

I checked the actual dataset columns, identified the mismatch, corrected the code, and reran the pipeline successfully.

This showed the importance of verifying AI-generated code against the actual project data rather than accepting suggestions without testing.