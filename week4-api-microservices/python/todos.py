import os
import uuid
from dotenv import load_dotenv
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import connection
from connection import session

load_dotenv()
session.default_timeout = 60
connection.register_connection("session", session=session, default=True)


class Todos(Model):
    __keyspace__ = os.environ.get("ASTRA_DB_KEYSPACE")
    __table_name__ = "todoitems"
    user_id = columns.Text(primary_key=True, required=True)
    item_id = columns.TimeUUID(
        primary_key=True, clustering_order="DESC", default=uuid.uuid1)
    title = columns.Text(required=True)
    completed = columns.Boolean(default=False)
    offset = columns.Integer()


sync_table(Todos)
