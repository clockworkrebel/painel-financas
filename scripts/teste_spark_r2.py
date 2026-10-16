"""Teste de aceitação da Fase 1, parte 2: gravar e ler Parquet no R2 pelo conector S3A do Spark.

Usa o RGF Anexo 01 real de Ferraz e mostra a despesa com pessoal e os limites em % da RCL ajustada (DTP de 42,77%).
"""

import json
from pathlib import Path

from pyspark.sql import functions as F

from pipeline.config import r2_config
from pipeline.spark import sessao

ARQUIVO = Path(__file__).parent.parent / "tests/fixtures/siconfi/rgf-2026-q2-anexo01-exec.json"

cfg = r2_config()
caminho = f"s3a://{cfg.bucket}/teste/rgf_anexo01.parquet"
spark = sessao("teste-spark-r2")

itens = json.loads(ARQUIVO.read_text())["items"]
# A API devolve valor ora int, ora float; padroniza para o Spark inferir um tipo só
itens = [{**i, "valor": float(i["valor"])} for i in itens]
df = spark.createDataFrame(itens)
df.write.mode("overwrite").parquet(caminho)
print(f"gravou  {caminho} ({df.count()} linhas)")

lido = spark.read.parquet(caminho)
assert lido.count() == len(itens), "o número de linhas lidas é diferente do gravado"
print(f"leu     {lido.count()} linhas")

# DTP e limites em % da RCL ajustada, como o RGF publica
(
    lido.filter(F.col("coluna") == "% sobre a RCL Ajustada")
    .select("conta", "coluna", "valor")
    .show(truncate=False)
)
spark.stop()
