import os
from arango import ArangoClient
from arango_orm import Database
from models import Students

import time

time.sleep(5)

host = os.environ.get("ARANGO_NAME")
client = ArangoClient(hosts="http://" + host + ":8529")

passwd = os.environ.get("ARANGO_PASS")
sys_db = client.db("_system", username="root", password=passwd)

if not sys_db.has_database("marks_db"):
    sys_db.create_database("marks_db")

marks_db_client = client.db("marks_db", username="root", password=passwd)
db = Database(marks_db_client)
db.create_all([Students])
