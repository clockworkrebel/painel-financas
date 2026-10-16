"""Baixa o hadoop-aws para o cache do Ivy e confere se a versão casa com o Hadoop do PySpark.

Roda sozinho na criação do codespace (postCreateCommand), para o primeiro job não
esperar o download. Versão errada é a causa mais comum de ClassNotFoundException no S3A.
"""

import sys

from pyspark.sql import SparkSession

from pipeline.spark import HADOOP_VERSAO, PACOTES

spark = (
    SparkSession.builder.appName("baixar-jars")
    .master("local[1]")
    .config("spark.jars.packages", PACOTES)
    .getOrCreate()
)
embutido = spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()
spark.stop()

print(f"Hadoop embutido no PySpark: {embutido} | hadoop-aws configurado: {HADOOP_VERSAO}")
if embutido != HADOOP_VERSAO:
    print(f"ERRO: ajuste HADOOP_VERSAO em pipeline/spark.py para {embutido}")
    sys.exit(1)
print("OK")
