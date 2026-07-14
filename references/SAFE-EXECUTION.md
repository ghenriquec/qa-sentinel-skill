# Safe Execution

## Ordem de ambientes

1. local descartável;
2. teste isolado;
3. staging autorizado;
4. produção apenas para observação não destrutiva e com autorização explícita.

## Proteção do repositório

- Registre `git status --short` antes e depois.
- Não descarte nem sobrescreva mudanças do usuário.
- Não edite manifests, lockfiles, código, testes, fixtures ou configs.
- Instalações devem respeitar lockfile e não produzir mudanças rastreadas.
- Relatórios e evidências devem ir para um diretório separado e autorizado.

## Dados

- Use contas e dados sintéticos.
- Não copie PII para logs, screenshots ou relatórios.
- Mascare tokens, cookies, chaves e strings de conexão.
- Limpe somente dados criados pela auditoria, quando seguro.

## Integrações

Use sandbox ou mock já existente para:

- pagamentos;
- e-mail, SMS e push;
- assinatura eletrônica;
- serviços fiscais;
- exclusão de conta ou dados;
- webhooks com efeito externo;
- operações com cobrança ou consequência legal.

## Banco

- Não execute migrations destrutivas.
- Use banco local descartável ou ambiente de teste autorizado.
- Não altere schema para destravar a auditoria.
- Não rode testes concorrentes sobre estado compartilhado sem isolamento.
