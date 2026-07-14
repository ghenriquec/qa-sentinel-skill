# Test Strategy

## Modelo de risco

Pontue cada fluxo ou regra de 1 a 5:

- **Impacto:** dano ao usuário, negócio, dados, dinheiro, privacidade, segurança ou conformidade.
- **Probabilidade:** chance de falha considerando complexidade, mudanças e histórico.
- **Exposição:** frequência e quantidade de usuários, tenants ou processos atingidos.

`Risk Score = Impacto × Probabilidade × Exposição`

- **P0 — 75–125:** testar primeiro e em profundidade.
- **P1 — 40–74:** crítico; exige E2E, negative testing e evidência forte.
- **P2 — 15–39:** relevante; testar combinações principais.
- **P3 — 1–14:** smoke ou exploratório.

## Categorias de cenário por regra

- `POSITIVE`
- `NEGATIVE`
- `BOUNDARY`
- `PERMISSION`
- `STATE`
- `FAILURE`
- `PERSISTENCE`
- `SIDE_EFFECT`
- `CONCURRENCY`
- `API_DIRECT`

Use `N/A` com justificativa quando uma categoria não se aplicar.

## Catálogo de cobertura

### Funcional e negócio

- CRUD e transições de estado;
- regras, cálculos, limites e exceções;
- validações e mensagens;
- refresh, retorno e deep link;
- busca, filtros, ordenação e paginação;
- uploads, downloads e exportação;
- datas, timezone, locale, moeda e arredondamento;
- analytics e eventos de produto.

### Identidade, privacidade e multitenancy

- login válido e inválido;
- sessão, expiração, logout e revogação;
- recuperação de acesso;
- acesso direto por URL/API;
- IDOR e troca de identificadores;
- isolamento entre tenant, organização, equipe e usuário;
- papéis administrativos;
- exposição de PII, segredo ou contexto entre usuários.

### Dados e consistência

- nulos, duplicados, limites e integridade referencial;
- transações e rollback observável;
- concorrência e dupla submissão;
- idempotência;
- consistência entre UI, API, eventos e persistência;
- backup, restore e recuperação quando acessível e seguro.

### Integrações e sistemas distribuídos

- sucesso, erro conhecido e resposta malformada;
- timeout e indisponibilidade;
- retry e circuit breaker;
- webhook duplicado, fora de ordem ou inválido;
- filas, workers, jobs e schedulers;
- falha parcial, compensação e recuperação;
- arquivos e notificações.

### Interface, acessibilidade e compatibilidade

- loading, empty, error, success e disabled;
- teclado, foco, modal, contraste e nomes acessíveis;
- desktop, tablet e mobile;
- navegadores e runtimes suportados;
- internacionalização e localização;
- feedback de ações assíncronas;
- proteção contra duplo clique.

### Segurança

- autorização server-side;
- entradas maliciosas não destrutivas;
- exposição de segredo, token, PII ou stack trace;
- upload e path traversal em ambiente seguro;
- cookies, CORS, CSP e headers conforme arquitetura;
- rate limit e abuso básico quando aplicável.

### Performance e confiabilidade

- N+1 evidente;
- payload excessivo;
- degradação em volume de teste;
- vazamento evidente de conexão ou memória;
- bloqueio desnecessário de operações assíncronas;
- retries explosivos e duplicidade de efeitos.

### Operação e entrega

- configuração por ambiente;
- feature flags;
- CI/CD e checks de release;
- infraestrutura declarativa;
- logs, métricas, traces e auditoria;
- health checks e readiness;
- recuperação após falha.

### Inteligência artificial

- entradas válidas, inválidas e ambíguas;
- respostas vazias, fora de contrato ou inconsistentes;
- classificação, confidence score, thresholds e fallback;
- timeout, custo, retry e indisponibilidade;
- vazamento de contexto e permissões;
- observabilidade, rastreabilidade e variabilidade.

## Heurísticas

Use quando adequado:

- CRUD;
- SFDIPOT;
- boundary value analysis;
- equivalence partitioning;
- state transition testing;
- decision table testing;
- pairwise testing;
- error guessing;
- contract testing;
- fault injection segura.
