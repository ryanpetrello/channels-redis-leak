import asyncio
import time

from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def run_sync(func):
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(func)
    event_loop.close()


class Command(BaseCommand):

    def handle(self, *args, **options):
        channel_layer = get_channel_layer()
        i = 0
        while True:
            async_to_sync(channel_layer.group_send)(
                'default',
                {'type': 'internal.message', 'text': 'Hello, World!' * 1024}
            )
            i += 1
            print(i)
