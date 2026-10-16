# Fase 1 — Fundação

15/10/2026 · Leo Souza

Entregável: repositório com ambiente reproduzível no Codespaces e bucket R2 com chave de acesso. O domínio ficou para antes da Fase 1.5.

## Progresso da fase (12 h)

### GitHub (4 h)

- [ ] Configurar a identidade do git com o e-mail privado do GitHub (o repositório é público e os commits mostram o e-mail):
  1. Em [github.com/settings/emails](https://github.com/settings/emails), marque "Keep my email addresses private" e copie o endereço `...@users.noreply.github.com`.
  2. `git config --global user.name "Leo Souza"`
  3. `git config --global user.email "<endereço noreply>"`
- [ ] Criar o repositório **público** `painel-financas` em [github.com/new](https://github.com/new), vazio (sem README, .gitignore ou licença).
- [ ] Primeiro commit e push, de dentro de `painel-financas/`:
  ```
  git add -A
  git commit -m "Estrutura inicial: devcontainer, conexão com o R2 e notas da Fase 0"
  git remote add origin https://github.com/<usuario>/painel-financas.git
  git push -u origin main
  ```
  Sem o `gh` instalado, o push pede um token: crie um em Settings → Developer settings → Personal access tokens (fine-grained, só este repositório, permissão "Contents: read and write").
- [ ] Proteger a `main`: Settings → Rules → Rulesets → New branch ruleset, alvo `main`, marcando "Require a pull request before merging" (0 aprovações, porque não dá para aprovar o próprio PR) e "Block force pushes".
- [ ] Criar um Project (board) com uma issue por fase do plano.
- [ ] A partir daqui, todo trabalho entra por branch e PR.

### Cloudflare R2 (4 h; o domínio fica para depois)

- [ ] Criar a conta na Cloudflare e ativar o R2. Ele pede cartão mesmo no plano gratuito, mas só cobra o que passar de 10 GB/mês.
- [ ] Criar o bucket `painel-financas` (localização automática).
- [ ] R2 → Manage API tokens → Create API token: permissão **Object Read & Write**, aplicada **só a este bucket**. Anote o Access Key ID e o Secret Access Key (o segredo aparece uma única vez) e o Account ID.
- [ ] Ler na documentação a diferença entre o endpoint S3 da conta e o domínio público do bucket (o painel usa só o primeiro).

### Codespaces (4 h)

- [ ] Em [github.com/settings/codespaces](https://github.com/settings/codespaces):
  - cadastrar os segredos `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` e `R2_BUCKET`, com acesso ao repositório `painel-financas`;
  - colocar o timeout de inatividade em 15 minutos e a retenção de codespaces parados em poucos dias.
- [ ] Criar um codespace na `main` (máquina de 2 núcleos) e esperar o `postCreateCommand` terminar. Ele deve imprimir "Hadoop embutido no PySpark: 3.4.1 | hadoop-aws configurado: 3.4.1" e "OK".
- [ ] Ler o `devcontainer.json` linha por linha e entender cada chave.

## Teste de aceitação

- [ ] Apagar o codespace, recriar e rodar sem instalar nada à mão:
  ```
  pyspark --version
  node -v
  java -version
  ```
- [ ] `python scripts/teste_r2.py`: sobe, lista, baixa e apaga um arquivo no bucket.
- [ ] `python scripts/teste_spark_r2.py`: grava e lê Parquet em `s3a://`, mostrando a DTP em 42,77% e os limites de 54 / 51,3 / 48,6%.
- [ ] Testar o acesso por script ao portal do TCE-SP (o plano pede isso na Fase 1): dá para baixar os conjuntos de dados ou ele bloqueia?

## Desvios do plano

- **Jars do S3A:** o plano cita `aws-java-sdk-bundle`, mas ele é do Hadoop 3.3. O PySpark 4.0 traz o Hadoop 3.4.1, cujo `hadoop-aws` usa o AWS SDK v2 (`software.amazon.awssdk:bundle`). Basta declarar o `hadoop-aws` em `spark.jars.packages`, e o Ivy baixa o SDK certo como dependência. A conferência de versão está em `scripts/baixar_jars.py`.
- **Domínio:** adiado; precisa estar resolvido antes da Fase 1.5.

## Glossário da fase

Para preencher com suas palavras, como o da Fase 0.

| Termo | Definição | Onde aparece |
| --- | --- | --- |
| Branch / pull request | | GitHub |
| Ruleset (proteção de branch) | | GitHub |
| Secret do Codespaces vs. secret do Actions | | GitHub |
| Dev container | | `.devcontainer/devcontainer.json` |
| Feature (dev container) | | `devcontainer.json` |
| `postCreateCommand` | | `devcontainer.json` |
| Core-hour | | cota do Codespaces |
| Bucket / objeto / chave | | R2 |
| API compatível com S3 | | R2, boto3 |
| Endpoint | | `pipeline/config.py` |
| Path-style vs. virtual-hosted | | `pipeline/spark.py` |
| S3A | | `pipeline/spark.py` |
| JAR / Maven / Ivy | | `spark.jars.packages` |
| Parquet | | `scripts/teste_spark_r2.py` |
| Taxa de saída (egress) | | preços do R2 |
