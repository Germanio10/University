from envparse import Env

env = Env()


REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default='postgresql+asyncpg://university_user:university_password@0.0.0.0:5432/university'
)
