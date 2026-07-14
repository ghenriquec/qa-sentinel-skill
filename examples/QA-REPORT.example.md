# QA Auditor Report — Example

## Resumo executivo

- **Modo de operação:** `Híbrido`
- **Status:** `AUDIT_COMPLETE`
- **Recomendação de release:** `REJECT`
- **Confiança:** `Alta`

Foram consolidadas 24 regras únicas. Três defeitos reproduzíveis foram encontrados. Nenhuma correção foi realizada.

## Métricas

| Métrica | Resultado |
|---|---:|
| Regras descobertas pelo QA | 22 |
| Regras importadas | 8 |
| Regras únicas consolidadas | 24 |
| Confirmadas por múltiplas fontes | 17 |
| Conflitantes | 2 |
| Inferidas | 3 |
| Não testadas | 1 |
| Cobertura QA | 95,5% |
| Cobertura importada | 100% |
| Cobertura consolidada | 95,8% |
| Cobertura crítica | 100% |

## Tabela de erros

| ID | Severidade | Prioridade | Tipo | Regra | Área / fluxo | Erro | Passos para reproduzir | Resultado atual | Resultado esperado | Frequência | Impacto | Evidência | Fontes em conflito | Localização provável | Causa | Recomendação | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BUG-001 | S1 | P0 | AUTHORIZATION | BR-004 | Administração / usuários | Usuário comum acessa rota administrativa diretamente | 1. Entrar como usuário comum 2. Abrir `/admin/users` | A página carrega e retorna dados | Servidor deve responder 403 e ocultar dados | Sempre | Exposição de dados e escalada de privilégio | HTTP 200 + screenshot sanitizada | Domínio e documentação concordam; código diverge | Middleware/guard da rota | `Hipótese: validação existe apenas na UI` | Revisar autorização server-side | REPRODUCED |
| BUG-002 | S2 | P1 | DATA_INTEGRITY | BR-011 | Cadastro / salvar | Duplo clique cria dois registros | 1. Preencher formulário 2. Clicar duas vezes em Salvar | Dois registros são persistidos | Apenas uma operação deve ser aceita | Sempre | Duplicidade e retrabalho | IDs de teste 813 e 814 | Nenhuma identificada | Handler/API de criação | `Hipótese: ausência de idempotência` | Avaliar proteção no cliente e servidor | REPRODUCED |
