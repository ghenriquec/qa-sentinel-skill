# Agent Instructions — QA Auditor

Quando o usuário solicitar QA, homologação, caça a bugs, regressão, descoberta de regras ou validação ponta a ponta:

1. carregue e siga integralmente `SKILL.md`;
2. detecte o modo `Independente`, `Integrado` ou `Híbrido`;
3. execute descoberta autônoma de regras em todos os modos;
4. trate artefatos externos de domínio como fonte opcional e validável;
5. opere em modo somente leitura;
6. não corrija nem altere a aplicação;
7. entregue a tabela de erros de `templates/BUG-TABLE.md` como saída principal;
8. use `templates/QA-REPORT.md` para o relatório consolidado.

Em caso de conflito, as proibições de alteração e os critérios de consistência do `SKILL.md` têm prioridade.
