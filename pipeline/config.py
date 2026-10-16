"""Configuração lida do ambiente: segredos do Codespaces, do Actions ou um .env local."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class R2Config:
    account_id: str
    access_key_id: str
    secret_access_key: str
    bucket: str

    @property
    def endpoint(self) -> str:
        return f"https://{self.account_id}.r2.cloudflarestorage.com"


def r2_config() -> R2Config:
    nomes = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET"]
    faltando = [n for n in nomes if not os.environ.get(n)]
    if faltando:
        raise RuntimeError(
            "Variáveis ausentes: " + ", ".join(faltando)
            + ". No Codespaces, cadastre-as em github.com/settings/codespaces e recrie o codespace."
        )
    return R2Config(*(os.environ[n] for n in nomes))
