#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import asyncio
import geojson
from aiohttp import web
from geo_data import load_geo_json

geobla = {}

@asyncio.coroutine
def geodata(request):
    dump = geojson.dumps(geobla)
    return web.Response(body=dump.encode('utf-8'))

@asyncio.coroutine
def hello(request):
    return web.HTTPFound("/static/index.html")
    
app = web.Application()

### Routes ###################
app.router.add_static('/static/', 'static')
app.router.add_route('GET', '/geodata/', geodata)
app.router.add_route('GET', '/', hello)

geobla = load_geo_json('dbdata/Final/Geodata/Streckennetz/WGS84/GeoJSON/Streckennetz_WGS84.geojson')

### Run the event loop #######
loop = asyncio.get_event_loop()
f = loop.create_server(app.make_handler(), '0.0.0.0', 8080)
srv = loop.run_until_complete(f)

print('serving on', srv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
