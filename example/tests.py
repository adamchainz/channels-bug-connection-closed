from channels.testing import WebsocketCommunicator
from django.test import TestCase

from example.consumers import WebsocketConsumer


class ExampleConsumerTests(TestCase):
    async def test_websocket(self):
        communicator = WebsocketCommunicator(WebsocketConsumer.as_asgi(), "/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        self.assertEqual(subprotocol, "fun")
