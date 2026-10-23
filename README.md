# QA Sentinel — QA Auditor Agent Skill

**Evidence-based quality auditing for software systems, APIs, and user journeys.**

QA Sentinel is a portable instruction protocol for AI coding agents. It helps an agent investigate an application's behavior, discover domain rules, examine available evidence, and produce a prioritized defect report. The protocol is **read-only by default**: it does not fix application code.

> **Status:** agent skill and audit-report templates — not a standalone test runner. Test execution depends on the capabilities, permissions, and environment of the agent using the skill.

## Why it exists

Quality assessment requires more than checking whether a test passes. An auditor also needs to understand business rules, investigate conflicting sources, assess risk, and preserve reproducible evidence. QA Sentinel defines a repeatable audit workflow and report contract for those tasks.

## What is included

| Component | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Canonical agent instructions, modes, safety boundaries, and audit process |
| [AGENTS.md](AGENTS.md) | Repository-level agent entry point |
| [PORTABLE-PROMPT.md](PORTABLE-PROMPT.md) | Portable instructions for agents without native skill support |
| [references/](references/) | Coverage, confidence, defect classification, exit criteria, and testing strategy |
| [templates/](templates/) | Bug tables, audit reports, traceability, and business-rule artifacts |
| [examples/](examples/) | Example reports to illustrate expected structure |
| [scripts/validate-skill.sh](scripts/validate-skill.sh) | Checks required skill files and protocol invariants |

## Operating modes

- **Independent:** investigate business rules directly using available evidence, without relying on another skill.
- **Integrated:** combine an independent investigation with validated external domain artifacts.
- **Hybrid:** use partial or outdated artifacts as supplementary evidence while assessing their limitations.

The canonical protocol defaults to `domain_rules.mode: auto`. External domain discovery is optional, not a prerequisite.

## Quick start

1. Read [SKILL.md](SKILL.md), including its safety and scope restrictions.
2. Make the repository or application under review accessible to your chosen agent.
3. Ask the agent to execute the audit within its authorized environment:

   ```text
   Run the qa-auditor protocol from SKILL.md. Inspect the available
   application flows and business rules. Report defects, priorities,
   limitations, and supporting evidence. Do not modify application code.
   ```

4. Review the artifacts under `qa-audit/`. Treat unexecuted or inaccessible flows as coverage gaps, not as passing tests.

## Expected output

The agent is instructed to produce a `qa-audit/` report package, including:

- `qa-bug-table.md` — prioritized findings, reproductions, and evidence
- `qa-audit-report.md` — scope, execution context, and limitations
- `qa-test-matrix.md` — test coverage by flow and layer
- `qa-traceability-matrix.md` — findings linked to source evidence
- `qa-discovered-rules.json` — discovered business rules
- `qa-evidence-index.md` — the evidence inventory

See [SKILL.md](SKILL.md) and the [templates](templates/) for the full artifact contract.

## Validation

The repository contains a structural validator for required files and key protocol declarations:

```bash
bash scripts/validate-skill.sh
bash tests/test-validate-skill.sh
```

[GitHub Actions](.github/workflows/validate.yml) runs structural validation and negative-path regression checks on pushes and pull requests. **Passing this check does not prove an AI agent's audit accuracy**; behavioral testing still needs to be carried out against the target system.

## Safety

- Do not change production data, credentials, infrastructure, or application code.
- Do not claim completeness for flows that were not inspected or executed.
- Treat documentation, implementation, and agent interpretations as fallible evidence.
- Execute checks only within the permissions granted for the target environment.

## Related work

[Universal Domain Rules Discovery](https://github.com/ghenriquec/universal-domain-rules-discover-skill) explores reusable discovery and traceability of application domain rules. The two projects can complement each other but neither is required to use the other.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and contribution guidance, and [SECURITY.md](SECURITY.md) for handling sensitive audit findings.

## License

See [LICENSE](LICENSE).
