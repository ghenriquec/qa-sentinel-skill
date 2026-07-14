# Rule Discovery and Consolidation

## Objetivo

Descobrir regras de negócio autonomamente e consolidar fontes externas opcionais sem tratar nenhuma como verdade absoluta.

## Sinais de regra

Procure por:

- guards, policies, roles e permissions;
- validações, schemas e mensagens de erro;
- branches condicionais e state machines;
- cálculos, arredondamentos e limites;
- constraints, índices únicos, triggers e transactions;
- contratos de API e códigos de resposta;
- feature flags e configuração por ambiente;
- testes que expressem comportamento esperado;
- textos e estados da interface;
- retries, idempotency keys e deduplicação;
- eventos emitidos, notificações e efeitos colaterais;
- comportamento observado.

## Deduplicação

Considere duas regras equivalentes apenas quando coincidirem materialmente em:

- intenção;
- ator;
- pré-condição;
- dados;
- estado inicial e final;
- efeito esperado;
- falha esperada.

Preserve aliases de IDs e todas as fontes.

## Conflitos

Não resolva por preferência. Registre:

- fontes divergentes;
- comportamento observado;
- impacto;
- cenário que expõe a divergência;
- evidência;
- situação atual.

## Lacunas

Registre separadamente:

- regra externa sem implementação observável;
- implementação sem documentação ou domínio;
- interface incompatível com API;
- teste incompatível com comportamento;
- banco incompatível com contrato;
- regra possivelmente obsoleta.
