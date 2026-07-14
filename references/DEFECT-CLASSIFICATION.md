# Defect Classification

## Severidade

### S0 — Crítica

- perda ou corrupção ampla de dados;
- exposição crítica de segurança ou privacidade;
- operação financeira incorreta e irreversível;
- indisponibilidade geral;
- ação destrutiva sem recuperação.

### S1 — Alta

- fluxo P0/P1 indisponível;
- bypass de autorização;
- inconsistência relevante de dados;
- regressão em função central;
- falha sem workaround aceitável;
- integração crítica com efeito incorreto.

### S2 — Média

- função importante degradada;
- workaround existe;
- validação incorreta que afeta parte dos usuários;
- falha relevante de acessibilidade, responsividade ou performance.

### S3 — Baixa

- problema cosmético;
- inconsistência textual;
- comportamento raro e de baixo impacto;
- melhoria de usabilidade sem quebra funcional.

## Tipos

- `FUNCTIONAL`
- `BUSINESS_RULE`
- `AUTHENTICATION`
- `AUTHORIZATION`
- `SECURITY`
- `PRIVACY`
- `DATA_INTEGRITY`
- `MULTITENANCY`
- `API_CONTRACT`
- `INTEGRATION`
- `WEBHOOK`
- `QUEUE_OR_JOB`
- `FILE_PROCESSING`
- `NOTIFICATION`
- `PERFORMANCE`
- `ACCESSIBILITY`
- `RESPONSIVE_UI`
- `COMPATIBILITY`
- `INTERNATIONALIZATION`
- `USABILITY`
- `ANALYTICS`
- `OBSERVABILITY`
- `BACKUP_OR_RECOVERY`
- `INFRASTRUCTURE`
- `CI_CD`
- `BUILD_OR_CONFIGURATION`
- `TEST_INFRASTRUCTURE`
- `AI_BEHAVIOR`

## Estados

- `REPRODUCED`
- `INTERMITTENT`
- `NOT_REPRODUCED`
- `BLOCKED`
- `EXPECTED_BEHAVIOR`
- `REQUIREMENT_GAP`
- `SOURCE_CONFLICT`
- `DUPLICATE`

## Registro obrigatório

Cada erro confirmado deve conter:

- ID único;
- regra relacionada;
- severidade;
- prioridade do fluxo;
- tipo;
- área/fluxo;
- ambiente e commit;
- pré-condições;
- passos mínimos para reproduzir;
- resultado atual;
- resultado esperado;
- frequência;
- impacto;
- evidência;
- fontes em conflito;
- localização provável;
- causa provável ou causa comprovada;
- recomendação de investigação;
- status.

Não use `REPRODUCED` sem repetir a falha. Não apresente hipótese como causa comprovada. Um conflito de fonte sem falha observável deve ser registrado em `qa-rule-conflicts.md`, e não forçado como bug.
