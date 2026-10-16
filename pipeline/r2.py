"""Cliente boto3 para o Cloudflare R2, que fala a API do S3."""

import boto3
from botocore.config import Config

from pipeline.config import R2Config, r2_config


def cliente(cfg: R2Config | None = None):
    cfg = cfg or r2_config()
    return boto3.client(
        "s3",
        endpoint_url=cfg.endpoint,
        aws_access_key_id=cfg.access_key_id,
        aws_secret_access_key=cfg.secret_access_key,
        region_name="auto",
        # boto3 >= 1.36 envia checksums novos por padrão; o R2 só precisa deles quando exigidos
        config=Config(
            request_checksum_calculation="when_required",
            response_checksum_validation="when_required",
        ),
    )
