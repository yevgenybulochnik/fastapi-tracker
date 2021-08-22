import re
from typing import Optional, Dict, Any
from pydantic import BaseSettings, PostgresDsn, Field, validator


class Settings(BaseSettings):
    POSTGRES_SERVER: Optional[str]
    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_DB: Optional[str]
    SQLALCHEMY_DATABASE_URI: str = Field(default="sqlite:///./db.sqlite")

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str, values: Dict[str, Any]) -> Any:
        pattern = re.compile(r"POSTGRES_")
        missing_postgres_setting = 0
        for value in values:
            print(value)
            if re.match(pattern, value):
                if not values.get(value):
                    missing_postgres_setting = 1

        if missing_postgres_setting:
            return v
        else:
            return PostgresDsn.build(
                scheme="postgresql",
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_SERVER"),  # type: ignore
                path=f"/{values.get('POSTGRES_DB') or ''}",
            )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
