# Tabela de erros

Esta é a saída principal da auditoria. Ordene por severidade, prioridade, impacto e frequência.

| ID | Severidade | Prioridade | Tipo | Regra | Área / fluxo | Erro | Passos para reproduzir | Resultado atual | Resultado esperado | Frequência | Impacto | Evidência | Fontes em conflito | Localização provável | Causa | Recomendação | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BUG-001 | S1 | P0 | FUNCTIONAL | BR-001 | Ex.: Checkout | Descrição objetiva | 1. ... 2. ... | ... | ... | Sempre | ... | screenshot/log/trace | Documentação × código | arquivo, rota ou componente | `Comprovada: ...` ou `Hipótese: ...` | Direção de investigação, sem implementar | REPRODUCED |

## Regras

- Uma linha por defeito distinto.
- Não agrupe sintomas com causas diferentes.
- Use passos mínimos e numerados.
- Vincule o defeito à regra quando existir.
- Evidência deve ser verificável e sanitizada.
- `Fontes em conflito` deve listar divergências relevantes ou `Nenhuma identificada`.
- `Causa` deve indicar `Comprovada:` ou `Hipótese:`.
- `Recomendação` não autoriza alteração de código.
- Itens `BLOCKED`, `REQUIREMENT_GAP`, `NOT_REPRODUCED` e conflitos sem bug observável podem ficar em tabelas específicas do relatório.
