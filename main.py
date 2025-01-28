from time import sleep

from microdot_asyncio import Microdot, Response, send_file
# from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket

from get_data import DataGetter

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

data_getter = DataGetter()

# root route
@app.route('/')
async def index(request):
    # return render_template('index.html)
    with open('/templates/index.html', 'r') as file:
        out = file.read()
    return out


@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
#         data = await ws.receive()
        sleep(.1)
        await ws.send(str(data_getter.get_data()))

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass
