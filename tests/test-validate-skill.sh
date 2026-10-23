#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# The validator resolves repository paths relative to itself, so exercise it
# against a disposable copy rather than mutating the checkout under test.
cp -R "$ROOT" "$WORK/fixture"
rm -rf "$WORK/fixture/.git"
VALIDATOR="$WORK/fixture/scripts/validate-skill.sh"

bash "$VALIDATOR" >/dev/null

expect_failure() {
  local label="$1"
  local expected="$2"
  local output
  if output="$(bash "$VALIDATOR" 2>&1)"; then
    echo "FAIL: $label unexpectedly passed validation" >&2
    exit 1
  fi
  if [[ "$output" != *"$expected"* ]]; then
    echo "FAIL: $label returned the wrong diagnostic: $output" >&2
    exit 1
  fi
  echo "PASS: $label"
}

mv "$WORK/fixture/templates/BUG-TABLE.md" "$WORK/BUG-TABLE.bak"
expect_failure "missing mandatory artifact" "Missing or empty: templates/BUG-TABLE.md"
mv "$WORK/BUG-TABLE.bak" "$WORK/fixture/templates/BUG-TABLE.md"

cp "$WORK/fixture/SKILL.md" "$WORK/SKILL.original"
sed -i 's/^version: .*/version: invalid/' "$WORK/fixture/SKILL.md"
expect_failure "invalid semantic version" ""
cp "$WORK/SKILL.original" "$WORK/fixture/SKILL.md"

printf '\npré-requisito de domínio\n' >> "$WORK/fixture/SKILL.md"
expect_failure "forbidden mandatory domain dependency" "Forbidden dependency language found:"
cp "$WORK/SKILL.original" "$WORK/fixture/SKILL.md"

bash "$VALIDATOR" >/dev/null
echo "PASS: structural validator regression suite"
