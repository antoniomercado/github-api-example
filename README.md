# Github API Exercise

## Summary 
Write a program that authenticates to the Github API, and queries for open issues with labels from a Github repository.
Return issues with an array of labels. Response should be returned as JSON.
Your program should take a parameter of the repository to query.

## Requirements

- Github personal Access token
- python3+

## Installation

```
$: pip install .
```

## Running the App

### Help Menu
```
$: ./main.py --help
```

### Executing with token as argument
```
$: ./main.py -t [GITHUB_TOKEN] -r example-owner/example-repo
```

### Executing with token as environment variable
```
$: export GITHUB_TOKEN="changeme"
$: ./main.py -r example-owner/example-repo
```

## Running the App with Docker

```
$: docker build -t github-api-example .
```
```
$: docker run -it github-api-example -r example-owner/example-repo
```