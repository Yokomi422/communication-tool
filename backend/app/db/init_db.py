from .database import engine
from .models import User, Base

Base.metadata.create_all(bind=engine)
