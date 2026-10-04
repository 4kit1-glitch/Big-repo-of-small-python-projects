# Food Day Questionnaire

Planning notes for a questionnaire about food choices and general health. This directory currently contains the project brief only; the application modules described below have not yet been added.

## Planned Features

- Present a questionnaire and validate responses.
- Provide a login form and store questionnaire records.
- Summarize dietary responses using transparent rules; any health guidance should be clearly labeled as educational rather than medical advice.

## Planned Components

- `app.py`: application entry point and interface.
- `questionnaire.py`: question set and questionnaire flow.
- `loginsys.py`: user login and record handling.
- `processor.py`: input validation and processing.
- `analyse.py` and `base.py`: analysis and basic food rules.
- `questions.json`: questionnaire data.

The original outline also proposed local logs, CSV data, and model experiments. Do not store real health information or credentials in version control. No run command is available until an application entry point is implemented.

## Learning Goals

Object-oriented programming, error handling, regular expressions, file handling, NumPy, and introductory machine-learning concepts.
- numpy
- simple ml concepts
