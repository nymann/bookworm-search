from pydantic import BaseSettings

from bookworm_search.version import __version__


class Config(BaseSettings):
    title: str
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
