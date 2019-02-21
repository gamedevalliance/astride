"""
The MIT License (MIT)

Copyright (c) 2015 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import json
import uuid
import asyncio
import os
import logging

log = logging.getLogger()


# TODO : A proper database should be used instead of a dumb json file
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
            with open('userdata/' + self.name, 'r', encoding='utf-8') as f:
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
                tmp, ensure_ascii=False,
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
