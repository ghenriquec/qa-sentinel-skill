## Purpose

Explain the problem this change addresses, and link to a reproducible non-sensitive example if applicable.

## Changes

Summarize protocol, template, validation, or documentation changes.

## Verification

- [ ] `bash scripts/validate-skill.sh`
- [ ] `bash tests/test-validate-skill.sh`
- [ ] `python -m unittest discover -s tests -p "test_validate_audit.py" -v`
- [ ] Any changed report artifact contract has been documented
- [ ] Read-only auditing and evidence-handling safeguards are preserved
- [ ] No credentials or private audit evidence are included

## Limitations

State what this change does *not* prove (for example, a passing structural validator does not establish that an agent audit is complete).
