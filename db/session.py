from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import settings

########################################
# BLOCK FOR COMMON INTERACTION WITH DB #
########################################


# create async engine for iteraction with db
engine = create_async_engine(settings.REAL_DATABASE_URL, echo=True,
                             future=True)

# create session for the interaction with db
async_session = sessionmaker(engine, expire_on_commit=False,
                             class_=AsyncSession)
