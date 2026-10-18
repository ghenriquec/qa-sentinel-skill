#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "SKILL.md"
  "AGENTS.md"
  "PORTABLE-PROMPT.md"
  "README.md"
  "references/COVERAGE-AND-CONFIDENCE.md"
  "references/DEFECT-CLASSIFICATION.md"
  "references/EXIT-CRITERIA.md"
  "references/RULE-DISCOVERY.md"
  "references/SAFE-EXECUTION.md"
  "references/TEST-STRATEGY.md"
  "templates/BUG-TABLE.md"
  "templates/QA-REPORT.md"
  "templates/artifacts/qa-business-rules-matrix.md"
  "templates/artifacts/qa-discovered-rules.json"
  "templates/artifacts/qa-domain-gaps.md"
  "templates/artifacts/qa-evidence-index.md"
  "templates/artifacts/qa-rule-conflicts.md"
  "templates/artifacts/qa-rule-source-comparison.md"
  "templates/artifacts/qa-test-matrix.md"
  "templates/artifacts/qa-traceability-matrix.md"
)

for file in "${required[@]}"; do
  [[ -s "$ROOT/$file" ]] || { echo "Missing or empty: $file" >&2; exit 1; }
done

grep -q "name: qa-auditor" "$ROOT/SKILL.md"
grep -Eq "^version: [0-9]+\\.[0-9]+\\.[0-9]+$" "$ROOT/SKILL.md"
grep -q "disable-model-invocation: true" "$ROOT/SKILL.md"
grep -q "Independente" "$ROOT/SKILL.md"
grep -q "Integrado" "$ROOT/SKILL.md"
grep -q "Híbrido" "$ROOT/SKILL.md"
grep -q "mode: auto" "$ROOT/SKILL.md"
grep -q "compare-and-consolidate" "$ROOT/SKILL.md"
grep -q "Cobertura importada" "$ROOT/SKILL.md"
grep -q "Não aplicável" "$ROOT/SKILL.md"
grep -qi "não corrige\|não corrigir\|não implemente" "$ROOT/SKILL.md"
grep -q "Tabela de erros" "$ROOT/templates/BUG-TABLE.md"
grep -q "Modo de operação" "$ROOT/templates/QA-REPORT.md"

for forbidden in \
  "dependência recomendada" \
  "pré-requisito de domínio" \
  "antes de iniciar, deve existir" \
  "sem a skill de domínio a cobertura é necessariamente incompleta"; do
  if grep -Fqi "$forbidden" "$ROOT/SKILL.md"; then
    echo "Forbidden dependency language found: $forbidden" >&2
    exit 1
  fi
done

echo "QA Auditor v2.1.0 structure and architecture are valid."
