import json
import uuid
import asyncio
import os
import logging

log = logging.getLogger()


class JSONAsset:

    def __init__(self, name, **options):
        self.name = name
        self.object_hook = options.pop('object_hook', None)
        self.encoder = options.pop('encoder', None)
        self.loop = options.pop('loop', asyncio.get_event_loop())
        self.lock = asyncio.Lock()
        if options.pop('defer_load', False):
            self.loop.create_task(self.load())
        else:
            self.load_from_file()

    def __contains__(self, item):
        return item in self._content

    def __getitem__(self, item):
        return self._content[item]

    def __len__(self):
        return len(self._content)

    def content(self):
        return self._content

    def load_from_file(self):
        try:
            with open('userdata/' + self.name, 'r') as f:
                self._content = json.load(f, object_hook=self.object_hook)
        except FileNotFoundError:
            self._content = {}

    async def load(self):
        with await self.lock:
            await self.loop.run_in_executor(None, self.load_from_file)

    def _dump(self):
        temp = 'userdata/{}-{}.tmp'.format(uuid.uuid4(), self.name)
        with open(temp, 'w', encoding='utf-8') as tmp:
            json.dump(
                self._content.copy(),
                tmp, ensure_ascii=True,
                cls=self.encoder,
                separators=(',', ':'))

        os.replace(temp, 'userdata/' + self.name)

    async def save(self):
        with await self.lock:
            await self.loop.run_in_executor(None, self._dump)

    def get(self, key, *args):
        return self._content.get(key, *args)

    async def put(self, key, value, *args):
        self._content[key] = value
        await self.save()

    async def remove(self, key):
        del self._content[key]
        await self.save()
