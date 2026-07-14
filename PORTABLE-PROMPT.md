# Portable invocation prompt

Use em agentes que não suportam skills nativamente:

```text
Leia e siga integralmente ./SKILL.md.

Execute uma auditoria QA autônoma em modo somente leitura. Detecte automaticamente o modo Independente, Integrado ou Híbrido. Descubra módulos, atores, entidades, estados, fluxos e regras de negócio diretamente do repositório, documentação, código, testes, banco, interface, contratos, filas, jobs, webhooks, integrações e comportamento observado.

Quando existirem artefatos externos de domínio, trate-os apenas como fonte adicional: leia, valide, compare, deduplique e consolide. Nunca os trate como verdade absoluta e nunca interrompa a auditoria por sua ausência. Mesmo no modo integrado, execute descoberta própria.

Construa matrizes de risco e rastreabilidade, gere cenários positivos, negativos, de limite, permissão, estado, falha, persistência, efeito colateral, concorrência/idempotência e API quando aplicável. Teste os fluxos funcionais e ponta a ponta, reproduza defeitos e entregue uma tabela priorizada com evidências.

NÃO corrija bugs. NÃO altere código, testes, configurações, dependências, migrations, fixtures, snapshots ou lockfiles. NÃO faça commit, push ou pull request.

Calcule Cobertura QA, Cobertura importada, Cobertura consolidada e Cobertura crítica. Quando não houver regras importadas, informe “Não aplicável” sem reduzir cobertura ou confiança. A confiança deve refletir evidências, cobertura, acesso às camadas, bloqueios e reprodutibilidade — nunca a ausência isolada de uma skill de domínio.

A saída principal deve ser a tabela de erros. Marque tudo que não puder ser testado como BLOCKED ou NOT_RUN e explique o motivo.
```
