from database.model import ArangoDB
from config import ARANGODB_DATABASE_URL, ARANGODB_DATABASE_NAME, ARANGODB_USERNAME, ARANGODB_PASSWORD

database: ArangoDB = ArangoDB(
    hosts=ARANGODB_DATABASE_URL, database=ARANGODB_DATABASE_NAME, username=ARANGODB_USERNAME, password=ARANGODB_PASSWORD
)
