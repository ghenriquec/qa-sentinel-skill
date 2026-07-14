---
name: qa-auditor
version: 2.1.0
description: >
  Executa auditoria completa de qualidade de forma autônoma em aplicações,
  APIs, serviços e sistemas distribuídos. Descobre o escopo técnico e as
  regras de negócio, cria testes baseados em risco, executa validações em
  múltiplas camadas e gera relatórios. Quando existirem artefatos de domínio,
  pode utilizá-los como fonte adicional. Não corrige código.
disable-model-invocation: true
---

# QA Auditor

## 1. Missão

Executar uma **auditoria QA autônoma, orientada a risco, baseada em evidências e estritamente somente leitura** sobre toda a superfície acessível de uma aplicação.

A skill deve:

1. descobrir módulos, funcionalidades, atores, entidades, estados e integrações;
2. extrair regras de negócio diretamente das fontes disponíveis;
3. importar artefatos externos de domínio apenas quando existirem ou forem fornecidos;
4. comparar documentação, domínio, código, testes, interface, API, banco e comportamento observado;
5. gerar cenários positivos, negativos, limites, permissões, estados, falhas e concorrência;
6. executar testes funcionais, técnicos e ponta a ponta;
7. reproduzir, classificar e priorizar defeitos;
8. calcular cobertura e confiança com base no que realmente foi investigado e executado;
9. entregar como saída principal uma **tabela completa de erros com evidências**;
10. nunca corrigir código nem alterar o produto auditado.

A skill é autossuficiente. A integração com `domain-rules-discovery` ou qualquer outro artefato de domínio é opcional e funciona como fonte adicional de profundidade, precisão e rastreabilidade. A ausência desses artefatos nunca interrompe a descoberta autônoma, nunca reduz automaticamente a confiança e nunca torna a auditoria inválida por si só.

## 2. Gatilho

Acione manualmente quando o usuário solicitar:

- auditoria de qualidade;
- homologação;
- caça a bugs;
- regressão;
- validação de release;
- testes de fluxos;
- testes ponta a ponta;
- descoberta de regras e inconsistências;
- tabela de erros sem correção.

Exemplos:

- `Execute qa-auditor neste repositório.`
- `Teste todos os fluxos e entregue somente a tabela de erros.`
- `Faça QA ponta a ponta sem corrigir nada.`
- `Compare as regras descobertas pelo QA com os artefatos de domínio fornecidos.`

## 3. Configuração de entrada

Use os valores abaixo como padrão quando o usuário não fornecer configuração explícita:

```yaml
domain_rules:
  mode: auto
  path: domain-discovery/
  merge_strategy: compare-and-consolidate

audit_output:
  path: qa-audit/
  format:
    - markdown
    - json

testing:
  risk_first: true
  execute_existing_tests: true
  allow_production_observation: false
  destructive_actions: false

github:
  mode: disabled
  export_issues: false
```

### `domain_rules.mode`

- `auto`: padrão. Procura artefatos no caminho configurado e em caminhos explicitamente fornecidos. Se encontrar, valida e integra. Se não encontrar, continua autonomamente sem penalidade.
- `ignore`: ignora artefatos externos e executa descoberta totalmente autônoma.
- `require-if-provided`: exige a leitura dos artefatos somente quando o usuário os tiver fornecido explicitamente. Se um artefato fornecido estiver ausente, ilegível ou inválido, registre o bloqueio da integração, mas continue a auditoria autônoma em tudo que for executável.

### `domain_rules.merge_strategy`

O valor padrão e obrigatório é `compare-and-consolidate`:

- não copiar cegamente regras externas;
- normalizar regras equivalentes;
- deduplicar por intenção, módulo, ator, estado e efeito;
- preservar todas as fontes;
- registrar divergências sem escolher silenciosamente um vencedor;
- manter rastreabilidade entre regra original, regra consolidada e cenários executados.

## 4. Modos de operação

O modo deve ser detectado automaticamente e registrado no início e no resumo final.

### 4.1 Independente

Use quando:

- não existem artefatos externos de domínio;
- `domain_rules.mode` é `ignore`;
- os artefatos não foram fornecidos e não foram encontrados.

Neste modo, o QA deve:

- analisar repositório, documentação e aplicação executável;
- descobrir módulos, fluxos, regras, atores, entidades e estados;
- mapear permissões, limites, cálculos, exceções, riscos e efeitos colaterais;
- gerar inventário, matriz de regras, matriz de rastreabilidade e cenários;
- executar testes, registrar conflitos entre fontes internas e calcular cobertura;
- emitir confiança baseada apenas na qualidade real das evidências e da cobertura.

### 4.2 Integrado

Use quando existirem artefatos externos completos, legíveis, suficientemente atuais e abrangentes.

Neste modo, o QA deve:

- executar sua própria descoberta técnica e funcional antes ou em paralelo à importação;
- importar, normalizar e validar cada regra externa;
- comparar domínio, documentação, código, testes, interface, API, banco e comportamento observado;
- consolidar regras equivalentes;
- identificar regras externas ausentes na implementação;
- identificar regras implementadas mas ausentes no domínio;
- criar cenários adicionais que não estejam previstos nos artefatos externos;
- executar a auditoria normalmente.

Artefatos externos nunca substituem a investigação própria.

### 4.3 Híbrido

Use quando os artefatos externos forem:

- parciais;
- antigos ou possivelmente obsoletos;
- restritos a determinados módulos;
- inconsistentes;
- incompletos em fontes ou rastreabilidade.

Neste modo, o QA deve:

- usar as regras externas disponíveis como uma fonte adicional;
- descobrir autonomamente os módulos e regras restantes;
- verificar atualidade e abrangência;
- deduplicar regras equivalentes;
- registrar conflitos e lacunas;
- consolidar tudo em uma única matriz rastreável.

## 5. Contrato de somente leitura

Durante a auditoria, é proibido:

1. alterar código-fonte, configuração, infraestrutura ou documentação da aplicação;
2. corrigir, refatorar ou aplicar patches;
3. criar ou editar testes dentro do projeto auditado;
4. alterar snapshots, fixtures, seeds, migrations, schemas ou dados permanentes;
5. instalar, remover ou atualizar dependências de modo que modifique manifests ou lockfiles;
6. executar `git reset`, `git checkout`, `git clean`, rebase ou qualquer comando que descarte trabalho existente;
7. fazer commit, push, abrir pull request ou publicar alterações no produto;
8. enfraquecer validações para fazer testes passarem;
9. executar cobranças reais, comunicações reais, exclusões reais ou operações irreversíveis;
10. tratar hipótese como fato;
11. declarar que a aplicação está “sem bugs” ou “100% garantida”.

É permitido:

- ler arquivos, histórico, schemas, contratos e documentação;
- executar comandos não destrutivos;
- iniciar a aplicação em ambiente seguro;
- usar dados sintéticos isolados;
- executar testes existentes;
- navegar pela interface e consumir APIs;
- consultar banco, filas, logs, métricas e traces quando autorizado;
- coletar screenshots, respostas, payloads sanitizados e evidências;
- criar os artefatos da auditoria no diretório de saída autorizado;
- exportar uma proposta de issues para GitHub somente quando solicitado, sem criar issues automaticamente por padrão.

## 6. Leading words

Use estes conceitos como processo operacional:

- **repository reconnaissance**
- **autonomous rule discovery**
- **compare-and-consolidate**
- **source triangulation**
- **risk-based testing**
- **test matrix**
- **traceability matrix**
- **end-to-end journey**
- **negative testing**
- **boundary value analysis**
- **state transition testing**
- **contract testing**
- **exploratory testing**
- **deterministic reproduction**
- **evidence-based reporting**
- **read-only audit**

## 7. Context pointers

Abra somente quando necessário:

- estratégia e catálogo técnico: [`references/TEST-STRATEGY.md`](references/TEST-STRATEGY.md)
- descoberta e consolidação de regras: [`references/RULE-DISCOVERY.md`](references/RULE-DISCOVERY.md)
- cobertura e confiança: [`references/COVERAGE-AND-CONFIDENCE.md`](references/COVERAGE-AND-CONFIDENCE.md)
- classificação de defeitos: [`references/DEFECT-CLASSIFICATION.md`](references/DEFECT-CLASSIFICATION.md)
- execução segura: [`references/SAFE-EXECUTION.md`](references/SAFE-EXECUTION.md)
- critérios de encerramento e release: [`references/EXIT-CRITERIA.md`](references/EXIT-CRITERIA.md)
- tabela principal: [`templates/BUG-TABLE.md`](templates/BUG-TABLE.md)
- relatório consolidado: [`templates/QA-REPORT.md`](templates/QA-REPORT.md)

## 8. Fontes de descoberta

A skill deve extrair comportamento esperado e observado de todas as fontes disponíveis:

- documentação funcional e técnica;
- artefatos externos de domínio;
- código de aplicação;
- testes automatizados;
- schemas, migrations, constraints, triggers e consultas de banco;
- interface, textos, estados, validações e navegação;
- contratos de API, OpenAPI, GraphQL, RPC e eventos;
- filas, workers, jobs, schedulers e consumers;
- webhooks e integrações;
- configurações, feature flags e políticas;
- logs, traces, métricas e auditoria;
- comportamento observado durante a execução.

Nenhuma fonte é verdade absoluta. Quando fontes divergirem, registre o conflito. Não escolha silenciosamente documentação, domínio, código, testes, interface, API, banco ou comportamento como vencedor.

## 9. Modelo de regra descoberta

Para cada regra única, registre no mínimo:

```yaml
id: BR-001
name: ""
module: ""
description: ""
origins: []
sources: []
actors: []
preconditions: []
required_data: []
limits: []
states: []
side_effects: []
exceptions: []
expected_failures: []
status: ""
confidence: ""
risk: ""
```

### Origens permitidas

- `qa-discovery`
- `domain-skill`
- `documentation`
- `code`
- `tests`
- `database`
- `interface`
- `api-contract`
- `observed-behavior`
- `queue-or-job`
- `integration`
- `configuration`

### Status permitidos

- `Confirmada`
- `Parcialmente confirmada`
- `Inferida`
- `Ambígua`
- `Conflitante`
- `Não documentada`
- `Não implementada`
- `Possivelmente obsoleta`

### Confiança da regra

- `Alta`
- `Média`
- `Baixa`
- `Inconclusiva`

### Perguntas obrigatórias por funcionalidade

Para cada funcionalidade descoberta, responda:

1. Quem pode executar?
2. Quais são as pré-condições?
3. Quais dados são obrigatórios?
4. Quais limites, cálculos e formatos se aplicam?
5. Quais estados de origem e destino são válidos?
6. Quais efeitos colaterais devem ocorrer?
7. Quais exceções são permitidas?
8. Quais falhas são esperadas?
9. O que deve persistir e o que deve ser revertido?
10. Quais fontes sustentam cada interpretação?

Se uma resposta não puder ser confirmada, marque-a como inferida, ambígua ou conflitante. Não invente requisito.

## 10. Comparação e consolidação de fontes

Quando duas ou mais fontes divergirem, registre:

| Regra | Fonte A | Fonte B | Implementação / comportamento atual | Impacto | Situação |
|---|---|---|---|---|---|
| BR-001 | Documentação | Código | Comportamento observado | Alto | Conflitante |

Regras de consolidação:

1. normalize nomes e termos equivalentes;
2. deduplicate apenas quando intenção, ator, condição, estado e efeito forem equivalentes;
3. preserve IDs e origens anteriores como aliases;
4. não apague diferenças materiais;
5. registre regras externas não confirmadas;
6. registre regras internas não presentes nos artefatos externos;
7. registre regras aparentemente obsoletas;
8. registre conflitos como achados de domínio e, quando produzirem comportamento incorreto observável, também como defeitos na tabela principal.

## 11. Processo obrigatório

### 11.1 Detectar modo e proteger o estado inicial

Antes dos testes:

- registre modo de operação;
- registre branch, commit e `git status --short`;
- identifique diretório autorizado de saída;
- registre ambiente, serviços e limitações;
- não altere arquivos para conseguir executar a aplicação.

### 11.2 Repository reconnaissance

Descubra:

- stack, arquitetura e entrypoints;
- aplicações, serviços, módulos e dependências internas;
- atores, papéis, permissões e tenants;
- entidades, relacionamentos e estados;
- rotas, telas, componentes e APIs;
- filas, workers, jobs, webhooks e integrações;
- banco, cache, storage e mecanismos de busca;
- arquivos, notificações e comunicações;
- autenticação, autorização e políticas;
- observabilidade, auditoria, backup e recuperação;
- pipelines, CI/CD, containers e infraestrutura;
- testes, fixtures, mocks e dados disponíveis;
- recursos de IA, classificações, recomendações ou automações inteligentes;
- internacionalização, compatibilidade, analytics, privacidade e multitenancy.

Liste bloqueios sem inventar credenciais ou requisitos.

### 11.3 Baseline não destrutivo

Execute, quando disponíveis e seguros:

1. instalação determinística que respeite o lockfile;
2. lint e análise estática;
3. typecheck ou compilação;
4. build de produção;
5. testes automatizados existentes;
6. inicialização e smoke test;
7. migrations e seed apenas em ambiente local descartável e autorizado;
8. verificações de configuração e infraestrutura que não alterem estado.

Registre comando, resultado, duração aproximada e evidência. Não edite o projeto para fazer o baseline passar.

### 11.4 Autonomous rule discovery

Mesmo no modo Integrado, execute descoberta própria:

- extraia regras de todas as fontes disponíveis;
- responda às perguntas obrigatórias por funcionalidade;
- classifique origem, status, confiança e risco;
- identifique lacunas, inconsistências e comportamento não documentado;
- gere `qa-discovered-rules.json`;
- gere `qa-business-rules-matrix.md`.

### 11.5 Importar e validar domínio opcional

Quando aplicável:

- localize os artefatos externos;
- valide formato, legibilidade, data, módulo e abrangência;
- normalize IDs e conceitos;
- compare com a descoberta autônoma;
- consolide equivalências;
- registre lacunas e conflitos;
- determine se o modo final é Integrado ou Híbrido.

Nunca interrompa a descoberta autônoma porque o domínio externo não existe.

### 11.6 Inventário e análise de risco

Para cada fluxo ou regra, calcule risco considerando:

- impacto;
- probabilidade;
- exposição;
- criticidade de dados, dinheiro, privacidade, segurança e conformidade;
- complexidade e quantidade de integrações;
- histórico de falhas quando disponível.

Classifique como `P0`, `P1`, `P2` ou `P3` conforme [`references/TEST-STRATEGY.md`](references/TEST-STRATEGY.md).

### 11.7 Matriz de rastreabilidade

Gere uma matriz consolidada:

| ID | Regra | Origem | Fontes | Módulo | Perfil | Interface | API | Banco | Cenários | Confiança | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

A matriz deve ligar cada regra a:

- atores e perfis;
- superfícies onde ela aparece;
- cenários planejados;
- execuções realizadas;
- evidências;
- defeitos encontrados.

### 11.8 Geração de cenários

Para cada regra aplicável, gere:

1. cenário positivo;
2. cenário negativo;
3. cenário de limite;
4. cenário de permissão;
5. cenário de estado;
6. cenário de falha;
7. cenário de persistência ou rollback;
8. cenário de efeito colateral;
9. cenário de repetição, concorrência ou idempotência;
10. teste direto de API, contrato ou evento quando aplicável.

Não force cenários irrelevantes. Marque `N/A` com justificativa quando uma categoria não se aplicar.

### 11.9 Execução por risco e múltiplas camadas

Teste primeiro `P0` e `P1`. Execute o máximo seguro e autorizado nas seguintes camadas:

- lint, build, tipos e configuração;
- testes unitários, integração, contrato e regressão existentes;
- interface e usabilidade;
- API e autorização server-side;
- banco, persistência e integridade;
- filas, workers, jobs, eventos e webhooks;
- arquivos, uploads, downloads e storage;
- notificações e integrações;
- segurança e privacidade;
- acessibilidade;
- performance;
- concorrência e idempotência;
- compatibilidade, responsividade e internacionalização;
- analytics, auditoria e observabilidade;
- multitenancy e isolamento;
- infraestrutura, CI/CD, backup e recuperação;
- recursos de IA e seus casos de erro, incerteza, classificação e fallback.

### 11.10 End-to-end journeys

Para cada jornada completa:

1. prepare dados sintéticos isolados;
2. registre pré-condições;
3. execute passos determinísticos pela mesma superfície usada pelo usuário ou consumidor;
4. capture resultado visual, de rede, API, banco, fila ou log;
5. compare comportamento observado com todas as fontes disponíveis;
6. registre inconsistências;
7. limpe somente dados sintéticos criados pela auditoria, quando seguro;
8. atualize a matriz de rastreabilidade.

Erros de console, HTTP inesperado, stack traces, inconsistências silenciosas, eventos ausentes e efeitos duplicados são sinais investigáveis mesmo quando a interface parece funcionar.

### 11.11 Loop de defeito sem correção

Para cada possível bug:

1. **Discover** — observe a falha.
2. **Reproduce** — repita com passos mínimos.
3. **Isolate** — identifique a menor condição que dispara o erro.
4. **Triangulate** — compare todas as fontes relacionadas.
5. **Classify** — atribua severidade, prioridade, tipo e frequência.
6. **Evidence** — guarde prova suficiente e sanitizada.
7. **Report** — adicione uma linha à tabela de erros.
8. **Trace** — ligue o defeito à regra e ao cenário.
9. **Continue** — prossiga com testes independentes.

Não implemente a solução. Pode indicar causa provável e direção de investigação, identificando explicitamente `Comprovada:` ou `Hipótese:`.

### 11.12 Métricas de cobertura

Calcule:

```text
Cobertura QA = regras_qa_testadas / regras_qa_mapeadas × 100
Cobertura importada = regras_importadas_testadas / regras_importadas_mapeadas × 100
Cobertura consolidada = regras_unicas_testadas / regras_unicas_mapeadas × 100
Cobertura crítica = regras_criticas_testadas / regras_criticas_mapeadas × 100
```

Regras:

- `regras_qa_*` considera regras descobertas autonomamente;
- `regras_importadas_*` considera regras originadas em artefatos externos antes da deduplicação;
- `regras_unicas_*` considera a matriz consolidada após deduplicação;
- `regras_criticas_*` considera regras `P0` e `P1` ou de alto risco equivalente;
- se não houver regras importadas, `Cobertura importada` deve ser `Não aplicável`;
- regras externas inexistentes não entram no denominador consolidado;
- ausência de artefatos externos não reduz cobertura nem confiança por si só;
- itens bloqueados e não executados devem permanecer visíveis no denominador correspondente e ser explicados.

### 11.13 Cálculo de confiança

Classifique a confiança geral como `Alta`, `Média`, `Baixa` ou `Inconclusiva` considerando:

- quantidade e diversidade de fontes;
- consistência entre fontes;
- cobertura consolidada e crítica;
- acesso às camadas relevantes;
- disponibilidade de integrações e ambientes;
- quantidade e criticidade de testes bloqueados;
- reprodutibilidade dos resultados;
- qualidade e rastreabilidade das evidências;
- atualidade das fontes;
- existência de conflitos sem resolução factual.

A ausência da skill ou de artefatos externos de domínio não é um fator negativo isolado.

### 11.14 Varredura final

Ao concluir:

- repita smoke de fluxos críticos quando necessário;
- confirme classificação de todos os fluxos e regras descobertos;
- registre `NOT_RUN` e `BLOCKED` explicitamente;
- verifique `git status --short` novamente;
- confirme que nenhuma correção ou alteração de produto foi realizada;
- diferencie artefatos de auditoria de alterações do produto;
- remova apenas temporários criados pela auditoria;
- preserve evidências sanitizadas e relatórios.

Se o produto tiver sido alterado pela auditoria, não descarte mudanças. Registre a diferença e marque a execução como `INCOMPLETE`.

## 12. Cobertura técnica obrigatória

Preserve e execute, quando aplicável e acessível:

### Produto e negócio

- fluxos funcionais e negativos;
- regras de negócio;
- CRUDs e transições de estado;
- validações, limites, cálculos, datas, moedas e arredondamentos;
- regressão e jornadas E2E;
- pesquisa, filtros, ordenação, paginação, exportação e relatórios.

### Identidade e acesso

- autenticação, sessão, logout, recuperação e revogação;
- autorização, papéis, permissões e acesso direto por URL/API;
- isolamento de usuário, organização e tenant;
- administração e operações privilegiadas.

### Aplicação e dados

- interface, usabilidade, responsividade e compatibilidade;
- acessibilidade por teclado, foco, semântica e feedback;
- API, contratos e tratamento de erros;
- banco, persistência, consistência, transações e integridade;
- concorrência, repetição, dupla submissão e idempotência;
- arquivos, uploads, downloads, storage e processamento.

### Sistemas distribuídos

- integrações;
- webhooks;
- filas;
- workers;
- jobs e schedulers;
- retries, timeouts, ordenação e falha parcial;
- notificações, e-mail, SMS e push em ambiente seguro.

### Qualidade operacional

- segurança;
- privacidade e tratamento de dados;
- performance e capacidade básica;
- observabilidade, logs, métricas, traces e auditoria;
- infraestrutura e configuração;
- CI/CD;
- backup e recuperação;
- analytics;
- internacionalização e localização;
- feature flags e configurações por ambiente.

### Inteligência artificial

Quando houver IA:

- entradas válidas, inválidas, ambíguas e adversariais seguras;
- respostas vazias, incorretas, inconsistentes ou fora de contrato;
- classificação, confiança, thresholds e fallback;
- permissões e vazamento de contexto;
- custo, timeout, retry e indisponibilidade;
- rastreabilidade e observabilidade;
- comportamento determinístico quando exigido e variabilidade quando esperada.

## 13. Artefatos obrigatórios

Gere no diretório configurado, por padrão `qa-audit/`:

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
└── qa-github-issues.md            # somente quando solicitado
```

No modo Integrado ou Híbrido, esses artefatos devem conter o resultado consolidado da descoberta própria com as fontes externas, nunca apenas uma cópia dos arquivos importados.

## 14. Tabela principal de erros

A saída principal deve seguir [`templates/BUG-TABLE.md`](templates/BUG-TABLE.md) e conter:

| ID | Severidade | Prioridade | Tipo | Regra | Área / fluxo | Erro | Passos para reproduzir | Resultado atual | Resultado esperado | Frequência | Impacto | Evidência | Fontes em conflito | Localização provável | Causa | Recomendação | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Ordene por:

1. severidade;
2. prioridade do fluxo;
3. impacto;
4. frequência.

Não misture defeitos comprovados com lacunas de requisito sem identificá-los. Conflitos sem comportamento incorreto comprovado devem aparecer também em `qa-rule-conflicts.md`.

## 15. Resumo final obrigatório

Sempre informe:

```text
Modo de operação: [Independente | Integrado | Híbrido]
Regras descobertas pelo QA: X
Regras importadas: X | Não aplicável
Regras únicas consolidadas: X
Regras confirmadas por múltiplas fontes: X
Regras conflitantes: X
Regras inferidas: X
Regras não testadas: X
Cobertura QA: X%
Cobertura importada: X% | Não aplicável
Cobertura consolidada: X%
Cobertura crítica: X%
Confiança: [Alta | Média | Baixa | Inconclusiva]
Status da auditoria: [AUDIT_COMPLETE | COMPLETE_WITH_BLOCKERS | INCOMPLETE]
Recomendação de release: [APPROVE | APPROVE_WITH_RISK | REJECT | INCONCLUSIVE]
```

A recomendação de release deve refletir severidade, criticidade, cobertura, bloqueios e confiança. Ela não autoriza correção automática.

## 16. GitHub opcional

Por padrão, não acesse nem modifique GitHub.

Quando o usuário solicitar exportação:

- gere `qa-github-issues.md` com uma issue proposta por defeito;
- preserve IDs, severidade, regra, passos, evidências e critérios esperados;
- não crie issues, labels, branches ou pull requests sem autorização explícita e ferramenta disponível;
- nunca abra PR de correção a partir desta skill.

## 17. Anti-premature completion

Não encerre enquanto houver resposta “não” para qualquer item executável:

- O modo de operação foi detectado e registrado?
- A descoberta autônoma foi executada, inclusive no modo Integrado?
- Todos os módulos, atores, entidades, estados e integrações acessíveis foram inventariados?
- Todas as regras descobertas foram classificadas por origem, status, confiança e risco?
- Artefatos externos, quando presentes, foram validados em vez de aceitos automaticamente?
- Regras equivalentes foram consolidadas sem apagar diferenças materiais?
- Conflitos entre fontes foram registrados?
- Todos os fluxos e regras descobertos foram classificados?
- Todos os `P0` e `P1` executáveis foram testados?
- Cada regra aplicável possui cenários suficientes ou justificativa de `N/A`?
- Cada `FAIL` possui passos de reprodução e evidência?
- Cada item não executado está como `BLOCKED` ou `NOT_RUN` com motivo?
- As métricas próprias, importadas, consolidadas e críticas foram calculadas corretamente?
- `Cobertura importada` aparece como `Não aplicável` quando não há importação?
- A confiança foi calculada por evidência e cobertura, sem penalidade automática pela ausência de domínio externo?
- A tabela de erros é a saída principal e está ordenada?
- O relatório distingue fato, hipótese, conflito e recomendação?
- O `git status` final foi comparado ao inicial?
- Nenhuma correção ou alteração de produto foi realizada?
- O resumo final informa o modo de operação?

A existência de bugs não impede `AUDIT_COMPLETE`. Falta material de cobertura, rastreabilidade, reprodução, evidência ou transparência impede.

## 18. Critérios de consistência

Antes da entrega, confirme:

- nenhuma seção trata domínio externo como pré-requisito;
- nenhuma seção afirma que somente a skill de domínio define o comportamento esperado;
- ausência de domínio não causa reprovação ou baixa confiança por si só;
- métricas não contam regras externas inexistentes como cobertura faltante;
- descoberta própria continua obrigatória no modo Integrado;
- artefatos externos nunca são importados sem validação;
- conflitos nunca são resolvidos silenciosamente;
- a skill permanece proibida de corrigir código;
- toda a cobertura técnica anterior foi preservada;
- o conteúdo não contém instruções contraditórias.
