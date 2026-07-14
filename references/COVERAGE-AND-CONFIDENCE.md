# Coverage and Confidence

## Métricas

```text
Cobertura QA = regras_qa_testadas / regras_qa_mapeadas × 100
Cobertura importada = regras_importadas_testadas / regras_importadas_mapeadas × 100
Cobertura consolidada = regras_unicas_testadas / regras_unicas_mapeadas × 100
Cobertura crítica = regras_criticas_testadas / regras_criticas_mapeadas × 100
```

Se o denominador importado for zero, use `Não aplicável`.

## Regra testada

Uma regra conta como testada somente quando:

- ao menos um cenário relevante foi executado;
- o resultado foi registrado;
- existe evidência suficiente;
- bloqueios não foram tratados como execução.

## Confiança

### Alta

- cobertura crítica alta;
- múltiplas fontes consistentes;
- principais camadas acessíveis;
- poucos bloqueios materiais;
- falhas reproduzíveis;
- evidências fortes e rastreáveis.

### Média

- boa cobertura, mas com lacunas limitadas;
- parte das integrações indisponível;
- algumas regras inferidas ou conflitantes;
- evidência suficiente para as conclusões centrais.

### Baixa

- cobertura materialmente incompleta;
- camadas críticas inacessíveis;
- muitos bloqueios;
- regras importantes ambíguas;
- evidências fracas ou pouco reproduzíveis.

### Inconclusiva

- não há base suficiente para sustentar uma recomendação de release;
- ambiente ou produto não pôde ser executado de modo material;
- evidências contraditórias não puderam ser investigadas.

A inexistência de artefatos externos de domínio não reduz confiança por si só.
