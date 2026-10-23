# Contributing to QA Sentinel

Thanks for helping improve the quality of this agent-auditing protocol.

## Scope

QA Sentinel is a **read-only instruction protocol**, not an autonomous deployment agent or a standalone test runner. Proposals should strengthen verifiable audit behavior, traceability, safety boundaries, report contracts, or documentation without claiming untested execution capabilities.

## Local validation

From the repository root:

```bash
bash scripts/validate-skill.sh
bash tests/test-validate-skill.sh
```

GitHub Actions runs both checks on pushes and pull requests. These checks validate structural contracts only: they **do not** prove that an AI-generated audit is complete or correct.

## Changes worth submitting

- A reproducible audit failure with a small non-sensitive example.
- A report-template improvement with clear expected behavior.
- A contradiction or ambiguity in `SKILL.md` or the references.
- Stronger negative tests and additional validation without weakening existing invariants.

For protocol changes, describe what problem is being addressed, how the new rule behaves, and which user-visible report artifacts are affected. Update `CHANGELOG.md` when changing the contract.

## Review checklist

- [ ] Changes preserve the read-only boundary.
- [ ] Documentation does not claim inspections, tests, or coverage that were not performed.
- [ ] Existing mandatory artifacts and Independent/Integrated/Hybrid modes remain supported.
- [ ] The validator and its regression suite pass.
- [ ] No application data, credentials, patient information, or confidential evidence is committed.

## Security

Follow [SECURITY.md](SECURITY.md) for sensitive vulnerability reports. Do not paste credentials or private audit evidence into public issues.
