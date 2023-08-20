from aiohttp import web
from plugins.malik.extra import YTILK


class malik(object):
      ytilk = YTILK


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

routes = web.RouteTableDef()
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("movies_house3")
