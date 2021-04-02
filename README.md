# Python REST API

## How to run locally

To run the API just execute this in terminal:

```bash
uvicorn app_fast:app --reload
```

## Run tests with code coverage

First setup CWD:

```bash
CWD="$(pwd)"
```

```bash
pytest -v --cov=$CWD --cov-report html
````
