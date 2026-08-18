from src.database.session import Base

# Import all models here so Base.metadata knows about every table
from src.database.models import BucketFile  # noqa: F401