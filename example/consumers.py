from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import connection


class WebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await basic_query()
        await self.accept("fun")


@database_sync_to_async
def basic_query():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1234")
        return cursor.fetchone()[0]
