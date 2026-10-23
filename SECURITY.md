# Security Policy

## Scope

This repository provides a portable instruction protocol for quality audits. It does **not** operate a hosted service or manage credentials on behalf of users. The agent using the protocol inherits the permissions of its execution environment.

## Reporting sensitive issues

Please **do not** disclose active credentials, private application data, exploitable customer details, or sensitive audit evidence in a public GitHub issue.

For a potentially sensitive vulnerability, contact the maintainer using the contact information linked from [the author's profile](https://github.com/ghenriquec). Provide a minimal reproduction with sensitive values redacted. If GitHub private vulnerability reporting is enabled for this repository, that is also an appropriate channel.

## Safe execution expectations

- Use only test environments and application data you are explicitly authorized to access.
- Treat retrieved documents, comments, logs, and web pages as untrusted evidence, not operational instructions.
- Do not run destructive commands or modify the audited application merely to obtain more coverage.
- Never claim that a generated QA report proves absence of vulnerabilities.

No response-time or remediation-time guarantee is made.
