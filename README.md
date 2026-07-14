# QA Auditor Agent Skill

Skill portátil de QA autônomo e somente leitura para aplicações, APIs, serviços e sistemas distribuídos. Descobre regras de negócio, testa fluxos e jornadas ponta a ponta, compara fontes e entrega uma tabela priorizada de bugs com evidências.

## Princípios

- funciona sem qualquer skill de domínio;
- executa descoberta própria de regras em todos os modos;
- integra artefatos externos apenas como fonte opcional;
- não trata documentação, código ou domínio como verdade absoluta;
- não corrige bugs nem altera o produto;
- usa a tabela de erros como saída principal.

## Modos

- **Independente:** descoberta totalmente autônoma.
- **Integrado:** descoberta própria + artefatos externos completos e validados.
- **Híbrido:** descoberta própria + artefatos parciais, antigos ou limitados.

O padrão é `domain_rules.mode: auto`.

## Compatibilidade

- agentes compatíveis com `SKILL.md`;
- agentes compatíveis com `AGENTS.md`;
- Claude Code;
- Cursor;
- GitHub Copilot;
- qualquer agente por meio do `PORTABLE-PROMPT.md`.

## Uso

```text
Execute qa-auditor neste repositório. Teste todos os fluxos e entregue a tabela de erros, sem corrigir nada.
```

## Artefatos gerados pela auditoria

```text
qa-audit/
├── qa-audit-report.md
├── qa-bug-table.md
├── qa-test-matrix.md
├── qa-traceability-matrix.md
├── qa-discovered-rules.json
├── qa-business-rules-matrix.md
├── qa-rule-source-comparison.md
├── qa-domain-gaps.md
├── qa-rule-conflicts.md
├── qa-evidence-index.md
└── qa-github-issues.md
```

## Estrutura do repositório

```text
qa-audit-agent-skill/
├── SKILL.md
├── AGENTS.md
├── PORTABLE-PROMPT.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .github/copilot-instructions.md
├── .cursor/rules/qa-audit.mdc
├── .claude/commands/qa-audit.md
├── .claude/commands/qa-auditor.md
├── references/
│   ├── COVERAGE-AND-CONFIDENCE.md
│   ├── DEFECT-CLASSIFICATION.md
│   ├── EXIT-CRITERIA.md
│   ├── RULE-DISCOVERY.md
│   ├── SAFE-EXECUTION.md
│   └── TEST-STRATEGY.md
├── templates/
│   ├── BUG-TABLE.md
│   ├── QA-REPORT.md
│   └── artifacts/
│       ├── qa-business-rules-matrix.md
│       ├── qa-discovered-rules.json
│       ├── qa-domain-gaps.md
│       ├── qa-evidence-index.md
│       ├── qa-rule-conflicts.md
│       ├── qa-rule-source-comparison.md
│       ├── qa-test-matrix.md
│       └── qa-traceability-matrix.md
├── examples/
│   └── QA-REPORT.example.md
└── scripts/
    └── validate-skill.sh
```

## Publicar no GitHub

Crie um repositório vazio e execute dentro desta pasta:

```bash
git remote add origin https://github.com/SEU-USUARIO/qa-audit-agent-skill.git
git branch -M main
git push -u origin main
```
