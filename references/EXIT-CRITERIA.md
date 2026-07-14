# Exit Criteria and Release Recommendation

## AUDIT_COMPLETE

Permitido quando:

- o modo de operação foi registrado;
- a descoberta autônoma foi concluída;
- todos os fluxos e regras descobertos foram classificados;
- todos os P0/P1 executáveis foram testados;
- cada falha confirmada possui reprodução e evidência;
- itens não executados têm motivo explícito;
- conflitos e lacunas foram registrados;
- as quatro métricas de cobertura foram calculadas corretamente;
- a confiança foi justificada;
- a tabela de erros foi priorizada;
- riscos residuais foram registrados;
- o produto terminou sem alterações causadas pela auditoria.

A existência de S0/S1 não impede `AUDIT_COMPLETE`; ela influencia a recomendação de release.

## COMPLETE_WITH_BLOCKERS

Use quando a auditoria executou tudo que era seguro e possível, mas parte material ficou bloqueada por:

- credencial autorizada ausente;
- ambiente ou serviço indisponível;
- dados indispensáveis ausentes;
- integração inacessível;
- operação que exigiria risco ou efeito irreversível;
- artefato explicitamente fornecido no modo `require-if-provided` que não pôde ser lido.

A ausência normal de artefatos externos no modo `auto` não é bloqueio.

## INCOMPLETE

Use quando:

- P0/P1 executável não foi testado sem justificativa;
- uma falha foi relatada sem reprodução ou evidência suficiente;
- descoberta autônoma não foi executada;
- não foi possível distinguir alterações do produto;
- a execução foi interrompida antes das matrizes e do relatório;
- houve alteração indevida na aplicação.

## Recomendação de release

- `APPROVE`: cobertura crítica suficiente, sem defeitos bloqueadores conhecidos e confiança adequada.
- `APPROVE_WITH_RISK`: riscos conhecidos são limitados, aceitos e claramente documentados.
- `REJECT`: defeitos S0/S1, quebra de regra crítica ou risco de dados, segurança, dinheiro ou conformidade.
- `INCONCLUSIVE`: cobertura, acesso ou evidência insuficiente para recomendar.

## Linguagem obrigatória

Use:

- “Não foram encontrados novos defeitos no escopo executado.”
- “Todos os fluxos P0/P1 executáveis abaixo foram avaliados.”
- “Os itens abaixo permaneceram bloqueados ou não executados.”

Não use:

- “A aplicação está sem bugs.”
- “Tudo está 100% garantido.”
- “Não existem falhas.”
