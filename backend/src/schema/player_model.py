import os

from pydantic import BaseModel, EmailStr, field_validator


class PlayerModel(BaseModel):
    """Acts as the data contract between the frontend and the backend.

    It defines the JSON structure used to exchange player information,
    ensuring data consistency and validation during API requests and responses."""

    id_player: int | None = None
    username: str
    password: str
    elo: int
    email: EmailStr
    pokemon_fan: bool

    @field_validator("password")
    @classmethod
    def check_password_length(cls, v: str) -> str:
<<<<<<< HEAD
        min_len = os.environ["PASSWORD_MIN_LENGTH"]
        if len(v) < min_len:
            raise ValueError(
                "Password must be at least " + os.environ["PASSWORD_MIN_LENGTH"] + "characters long"
            )
=======
        min_len = int(os.getenv("PASSWORD_MIN_LENGTH", 12))
        if len(v) < min_len:
            raise ValueError(f"Password must be at least {min_len} characters long")
>>>>>>> origin/corentin-tp2
        return v


class PlayerReadModel(BaseModel):
    id_player: int
    username: str
    elo: int | None
    email: EmailStr
    pokemon_fan: bool | None


class PlayerLoginModel(BaseModel):
    username: str
    password: str
