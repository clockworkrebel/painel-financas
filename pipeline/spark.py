"""SparkSession com o conector S3A apontado para o R2.

O hadoop-aws precisa ter exatamente a versão do Hadoop embutido no PySpark.
O PySpark 4.0.x traz o Hadoop 3.4.1. Ao trocar a versão do PySpark, rode
`python scripts/baixar_jars.py --checar` para conferir.
"""

from pyspark.sql import SparkSession

from pipeline.config import R2Config, r2_config

HADOOP_VERSAO = "3.4.1"
# O hadoop-aws 3.4 usa o AWS SDK v2 ("bundle"), que o Ivy baixa como dependência.
PACOTES = f"org.apache.hadoop:hadoop-aws:{HADOOP_VERSAO}"


def sessao(nome: str = "painel-financas", r2: bool = True, cfg: R2Config | None = None) -> SparkSession:
    builder = SparkSession.builder.appName(nome).master("local[*]")
    if r2:
        cfg = cfg or r2_config()
        builder = (
            builder.config("spark.jars.packages", PACOTES)
            .config("spark.hadoop.fs.s3a.endpoint", cfg.endpoint)
            .config("spark.hadoop.fs.s3a.endpoint.region", "auto")
            .config("spark.hadoop.fs.s3a.path.style.access", "true")
            .config("spark.hadoop.fs.s3a.access.key", cfg.access_key_id)
            .config("spark.hadoop.fs.s3a.secret.key", cfg.secret_access_key)
        )
    return builder.getOrCreate()
