from pydantic import BaseSettings


class Settings(BaseSettings):
    model_file: str
    tokenizer_file: str

    class Config:
        env_file = ".env"
