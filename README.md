# Painel de finanças — Ferraz de Vasconcelos (SP)

Painel das finanças do município (código IBGE 3515707) alimentado só por fontes oficiais: SICONFI, Tesouro, CGU, TCE-SP, IBGE e Banco Central. Projeto de estudo da stack GitHub/Codespaces → PySpark/Actions → Cloudflare R2 → Supabase → Next.js/Vercel.

## Estrutura

| Caminho | O que é |
| --- | --- |
| `.devcontainer/` | Ambiente do Codespaces: Python 3.12, Java 17, Node LTS e PySpark |
| `pipeline/` | Código Python reutilizável: configuração e conexões com o R2 (boto3 e Spark) |
| `scripts/` | Scripts avulsos e testes de aceitação das fases |
| `tests/fixtures/siconfi/` | Respostas reais da API do SICONFI, usadas como amostras de teste |
| `docs/` | Notas por fase: glossário, indicadores e conferências |

## Rodando no Codespaces

1. Cadastre os segredos `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` e `R2_BUCKET` em [github.com/settings/codespaces](https://github.com/settings/codespaces), com acesso a este repositório.
2. Crie um codespace na `main`. Na criação, as dependências e os jars do S3A são instalados sozinhos.
3. Teste: `python scripts/teste_r2.py` e `python scripts/teste_spark_r2.py`.

## Fases

- [x] Fase 0 — Finanças públicas: teste de aceitação feito; o glossário vai sendo preenchido ao longo das fases ([notas](docs/fase-0-glossario-e-indicadores.md))
- [ ] Fase 1 — Fundação: GitHub, Codespaces, Cloudflare ([notas](docs/fase-1-fundacao.md))
- [ ] Fase 1.5 — Fatia vertical
- [ ] Fase 2 — Ingestão
- [ ] Fase 3 — Backend (Supabase)
- [ ] Fase 4 — Front-end (Next.js)
- [ ] Fase 5 — Deploy e observabilidade
- [ ] Fase 6 — Integrador

## Próximo passo

Criar o repositório no GitHub, fazer o primeiro push e criar o bucket R2 (ver `docs/fase-1-fundacao.md`).
