"""Teste de aceitação da Fase 1, parte 1: subir, listar, baixar e apagar um arquivo no R2 com boto3."""

from pathlib import Path

from pipeline.config import r2_config
from pipeline.r2 import cliente

ARQUIVO = Path(__file__).parent.parent / "tests/fixtures/siconfi/rgf-2026-q2-anexo01-exec.json"
CHAVE = "teste/rgf-2026-q2-anexo01-exec.json"

cfg = r2_config()
s3 = cliente(cfg)
original = ARQUIVO.read_bytes()

s3.put_object(Bucket=cfg.bucket, Key=CHAVE, Body=original, ContentType="application/json")
print(f"subiu   s3://{cfg.bucket}/{CHAVE} ({len(original):,} bytes)")

listados = [o["Key"] for o in s3.list_objects_v2(Bucket=cfg.bucket, Prefix="teste/").get("Contents", [])]
print(f"listou  {listados}")

baixado = s3.get_object(Bucket=cfg.bucket, Key=CHAVE)["Body"].read()
assert baixado == original, "o arquivo baixado é diferente do enviado"
print("baixou  conteúdo idêntico ao enviado")

s3.delete_object(Bucket=cfg.bucket, Key=CHAVE)
print("apagou  OK")
