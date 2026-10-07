from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import Engine
from sqlalchemy.engine.create import create_engine

class SQLAlchemyConfig(BaseSettings):
    dialect: Literal["oracle", "postgres"]
    host: str
    port: int
    username: str
    password: str
    name: str

    def __post_init__(self):
        if not all([self.port, self.username, self.password, self.host, self.dialect]):
            raise ValueError("All configuration parameters must be provided.")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="SQLALCHEMY_",
    )

    def _connection_factory(self) -> str:
        if self.dialect == "oracle":
            return f"oracle+cx_oracle://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
        elif self.dialect == "postgres":
            return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
        else:
            raise RuntimeError(f"Unknown engine {self.dialect}")

    def create_engine(self) -> Engine:
        try:
            connection_string = self._connection_factory()
            return create_engine(connection_string, echo=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create {self.dialect} engine: {e}")