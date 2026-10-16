# Fase 0 — Glossário e indicadores

13/10/2026 · Leo Souza · rascunho do README do painel

Exemplos com dados reais de Ferraz de Vasconcelos (IBGE 3515707): RREO do 4º bimestre de 2026 (jan–ago, entregue em 30/09/2026) e RGF do 2º quadrimestre de 2026 do Poder Executivo, baixados da API do SICONFI em 13/10/2026 e salvos em `tests/fixtures/siconfi/`.

## Progresso da fase (12 h)

- [ ] Ciclo orçamentário: PPA, LDO, LOA (1 h)
- [ ] Receita: classificação e principais fontes (2 h)
- [ ] Despesa: classificações e estágios (2 h)
- [ ] Limites legais e RCL (2 h)
- [ ] MDF: anexos 01 do RREO e do RGF a fundo, demais anexos por cima (4 h)
- [x] Teste de aceitação (1 h)

## Glossário

Os termos estão na ordem do estudo. As definições de cada termo serão escritas por você, com suas palavras, à medida que estudar.

### Ciclo orçamentário

| Termo | Definição | Onde aparece |
| --- | --- | --- |
| PPA | | |
| LDO | | |
| LOA | | |
| Previsão inicial / atualizada | | RREO 01, receitas |
| Dotação inicial / atualizada | | RREO 01, despesas |
| Créditos adicionais | | RREO 01 |
| Superávit financeiro | | RREO 01 |

### Receita

| Termo | Definição | Onde aparece |
| --- | --- | --- |
| Receita corrente / de capital | | RREO 01 |
| Receita própria (IPTU, ISS, ITBI, taxas) | | RREO 01, "Impostos, taxas e contribuições de melhoria" |
| FPM | | RREO 03 |
| Cota-parte do ICMS | | RREO 03 |
| Fundeb | | RREO 03 e 08 |
| Receita intraorçamentária | | RREO 01 |
| Receita Corrente Líquida (RCL) | | RREO 03, RGF 01 |
| RCL ajustada | | RGF 01 |

### Despesa

| Termo | Definição | Onde aparece |
| --- | --- | --- |
| Classificação institucional (órgão) | | |
| Classificação funcional (função/subfunção) | | RREO 02 |
| Classificação programática (programa) | | |
| Natureza da despesa (categoria, grupo, elemento) | | RREO 01 |
| Empenho | | RREO 01 |
| Liquidação | | RREO 01 |
| Pagamento | | RREO 01 |
| Restos a pagar processados / não processados | | RREO 07 |
| Despesa com pessoal (DTP) | | RGF 01 |
| Dívida consolidada líquida (DCL) | | RGF 02 |

## Indicadores do painel

Para cada indicador: fórmula, anexo de origem e valor de Ferraz quando os dois anexos baixados permitem calcular. "A baixar" = depende de outro anexo.

| # | Indicador | Fórmula | Origem | Ferraz (jan–ago/2026) |
| --- | --- | --- | --- | --- |
| 1 | Execução da receita | receita realizada ÷ previsão atualizada | RREO 01 | 60,94% (R$ 507,5 mi de R$ 832,7 mi) |
| 2 | Dependência de transferências | transferências correntes ÷ receitas correntes | RREO 01 | 71,95% |
| 3 | Autonomia tributária | impostos, taxas e contrib. de melhoria ÷ receitas correntes | RREO 01 | 19,89% |
| 4 | Despesa empenhada | empenhado ÷ dotação atualizada | RREO 01 | 74,01% |
| 5 | Despesa liquidada | liquidado ÷ dotação atualizada | RREO 01 | 47,00% |
| 6 | Despesa paga | pago ÷ dotação atualizada | RREO 01 | 45,86% |
| 7 | Resultado orçamentário | receita realizada − despesa liquidada | RREO 01 (linha "Superávit XIII") | +R$ 43,08 mi |
| 8 | Investimento | despesas de capital liquidadas ÷ despesa liquidada | RREO 01 | 7,65% |
| 9 | Despesa com pessoal (Executivo) | DTP ÷ RCL ajustada; limite 54%, prudencial 51,3%, alerta 48,6% | RGF 01 | 42,77% (R$ 314,9 mi ÷ R$ 736,4 mi) |
| 10 | Endividamento | DCL ÷ RCL ajustada para endividamento; limite 120%, alerta 108% | RGF 02 | −11,13% (DCL de −R$ 83,7 mi) |
| 11 | Educação (MDE) | despesa em MDE ÷ receita de impostos e transferências; mínimo 25% no ano | RREO 14 (resumo do 08) | 24,45% até o bimestre |
| 12 | Fundeb na remuneração | parcela do Fundeb paga a profissionais da educação básica; mínimo 70% no ano | RREO 14 (resumo do 08) | 86,19% |
| 13 | Saúde (ASPS) | despesa em ASPS ÷ receita de impostos e transferências; mínimo 15% no ano | RREO 14 (resumo do 12) | 15,17% até o bimestre |
| 14 | Restos a pagar | RP inscritos, pagos, cancelados e saldo | RREO 07 (resumo no 14) | R$ 51,1 mi inscritos, R$ 32,6 mi pagos, R$ 17,9 mi a pagar |
| 15 | Resultado primário | receitas primárias − despesas primárias (sem RPPS) | RREO 06 (resumo no 14) | +R$ 17,0 mi |
| 16 | Valores per capita | indicador em R$ ÷ população IBGE | qualquer + IBGE | a calcular |

Os indicadores 1 a 9 já batem com os totais do próprio relatório; o 9 confere com o percentual que o RGF publica (42,77%). Os indicadores 10 a 15 foram lidos diretamente dos percentuais publicados nos anexos.

## Primeiras descobertas nos dados

- **Os limites da LRF usam a RCL ajustada, não a RCL.** A RCL de Ferraz é R$ 761,9 mi e a ajustada é R$ 736,4 mi; o percentual oficial de pessoal (42,77%) usa a ajustada. Com a RCL cheia daria 41,34%: um erro que o painel não pode cometer. O entregável da Fase 1.5 no plano já foi corrigido para "despesa com pessoal ÷ RCL ajustada".
- **Empenho bem acima da liquidação (74% vs. 47%) é normal no meio do ano**: prefeituras empenham por estimativa o contrato do ano inteiro (empenho global ou estimativo). Comparar empenhado com receita realizada daria um falso déficit de R$ 224 mi; por isso o resultado usa a despesa liquidada.
- **O "Superávit financeiro utilizado para créditos adicionais" (R$ 112,2 mi) aparece entre as receitas, mas não é arrecadação do ano**: é saldo de anos anteriores usado para abrir créditos. Não pode entrar na soma da receita do painel.
- **O RREO repete o mesmo total em várias linhas** (subtotal, total, total com déficit). Na camada prata, escolher uma linha por conceito e documentar qual.
- **O RGF do 1º quadrimestre foi entregue duas vezes** (29/05 e 09/06): exemplo real de retificação para a Fase 2.
- **O RGF do 2º quadrimestre aparece duas vezes no extrato de entregas, ambas em 30/09**, provavelmente uma do Executivo e outra do Legislativo. Confirmar ao estudar o extrato de entregas.

- **Os Anexos 08 (educação) e 12 (saúde) não vêm na API para Ferraz.** Eles não aparecem nem no 4º bimestre de 2026 nem no 6º de 2025: municípios preenchem esses dados no SIOPE (educação) e no SIOPS (saúde), e o SICONFI só guarda o resumo no Anexo 14. Para o painel: percentuais pelo Anexo 14; detalhe, se for preciso, direto do SIOPE/SIOPS (boa candidata à "fonte nova" do integrador).
- **Existem três RCLs diferentes.** RCL de R$ 761,9 mi; ajustada para pessoal, R$ 736,4 mi; ajustada para endividamento, R$ 751,9 mi. Cada limite usa a sua; a tabela de indicadores precisa guardar qual RCL entrou em cada cálculo.
- **A dívida consolidada líquida é negativa (−R$ 83,7 mi):** a dívida bruta (R$ 323,3 mi) é menor que as deduções, principalmente o caixa disponível (R$ 271,3 mi). Não é erro, é a fórmula da LRF. O gráfico do painel precisa aceitar valores abaixo de zero e explicar isso em nota.
- **Educação está em 24,45%, abaixo dos 25%, mas o mínimo vale para o ano fechado.** No meio do ano isso não é descumprimento. Mostrar a regra "apurado até o bimestre / mínimo anual" para não gerar alarme falso; vale acompanhar no 5º e 6º bimestres.
- **Complementação VAAT na educação infantil aparece com 3,37% aplicado contra 50% indicado.** Não entendi essa regra ainda, então fica como "verificar" no estudo do MDF antes de ir para o painel.
- **O RREO de 2026 tem anexos diferentes do de 2025** (2025 trazia 04, 09 e 11; 2026, até agora, 13). Isso varia por bimestre e por ano: a ingestão deve buscar o relatório inteiro e listar os anexos, nunca supor uma lista fixa.

## Teste de aceitação ✅

Feito em 13/10/2026. Comparação do RREO Anexo 01 (balanço orçamentário) do SICONFI com o PDF publicado pela prefeitura.

- **Período usado: 2º bimestre de 2026 (janeiro a abril).** O 4º bimestre ainda não estava no site da prefeitura. O PDF mais recente fica na pasta de uploads de julho, mas é do 2º bimestre, emitido em 09/06/2026 pelo sistema CN-SIFPM.
- **Fonte externa:** [página de RREO da prefeitura](https://ferrazdevasconcelos.sp.gov.br/web/transparencia-fiscal/rreo-relatorio-resumido-da-execucao-orcamentaria/); cópia em `docs/fontes-prefeitura/rreo-2026-b2-balanco-orcamentario.pdf`.
- **Dado do SICONFI:** `tests/fixtures/siconfi/rreo-2026-b2-anexo01.json`.

| Linha | Coluna | SICONFI | Prefeitura | Confere |
| --- | --- | ---: | ---: | :---: |
| Receitas (exceto intra) | Previsão inicial | 760.867.000,00 | 760.867.000,00 | ✅ |
| Receitas (exceto intra) | Previsão atualizada | 761.708.798,96 | 761.708.798,96 | ✅ |
| Receitas (exceto intra) | No bimestre | 137.285.833,30 | 137.285.833,30 | ✅ |
| Receitas (exceto intra) | Até o bimestre | 244.560.752,92 | 244.560.752,92 | ✅ |
| Receitas (exceto intra) | Saldo | 517.148.046,04 | 517.148.046,04 | ✅ |
| Despesas (exceto intra) | Dotação inicial | 760.867.000,00 | 760.867.000,00 | ✅ |
| Despesas (exceto intra) | Dotação atualizada | 938.773.810,48 | 938.773.810,48 | ✅ |
| Despesas (exceto intra) | Empenhadas no bimestre | 120.683.361,00 | 120.683.361,00 | ✅ |
| Despesas (exceto intra) | Empenhadas até o bimestre | 492.859.618,37 | 492.859.618,37 | ✅ |
| Despesas (exceto intra) | Liquidadas no bimestre | 144.168.374,69 | 144.168.374,69 | ✅ |
| Despesas (exceto intra) | Liquidadas até o bimestre | 238.797.353,63 | 238.797.353,63 | ✅ |
| Despesas (exceto intra) | Pagas até o bimestre | 212.800.806,58 | 212.800.806,58 | ✅ |

Os 12 valores batem ao centavo.

O que o teste mostrou:

- **A prefeitura publica com atraso em relação ao SICONFI.** Em 13/10 o SICONFI já tinha o 4º bimestre, entregue em 30/09, e o site da prefeitura parava no 2º. Para o painel, o SICONFI é a fonte mais atual; o PDF da prefeitura serve como conferência.
- **O nome da pasta de upload não diz o período.** Um arquivo em `uploads/2026/07/` era do 2º bimestre. Um scraper do site precisaria ler o "Período de referência" de dentro do PDF.
- **O TCE-SP não serve para conferir 2026 ainda:** os conjuntos de dados de receitas e despesas vão só até 2025.
- **Pendente:** repetir a conferência do 4º bimestre quando a prefeitura publicar.

## Referências

- Manual de Demonstrativos Fiscais (MDF), Tesouro Nacional, edição vigente para 2026
- [API do SICONFI](https://apidatalake.tesouro.gov.br/docs/siconfi/)
- Lei Complementar 101/2000 (LRF), arts. 18 a 23 (pessoal) e Resolução do Senado 40/2001 (dívida)
