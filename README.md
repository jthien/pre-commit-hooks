[![build status](https://github.com/jthien/pre-commit-hooks/actiond/workflows/pre-commit.yml/badge.svg)](https://github.com/jthien/pre-commit-hooks/actiond/workflows/pre-commit.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jthien/pre-commit-hooks/pre-commit.svg)](https://results.pre-commit.ci/latest/github/jthien/pre-commit/main)

Testing of pre-commit checks which can be used with [pre-commit](http://pre-commit.com).

## Usage

```yaml
- repo: https://github.com/jthien/pre-commit-hooks
  rev: v0.0.1
  hooks:
    - id: check_filename
      args:
        - '--allowed_prefix=ops_'
        - '--allowed_prefix=job_'
      files: '^folder/*.py$'
```

### check_filename
Ensures that files are following a specific pattern.

--allowed_prefix PREFIX - Add an allowed prefix for files. Can be repeated multiple times.
