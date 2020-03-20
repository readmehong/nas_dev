from sanic import Sanic
from sanic.response import json
import time
import asyncio

app = Sanic()

@app.route('/hello')
async def test(request):
    return json({'hello': 'world'}) 

@app.route('/wait')
async def test(request):
   # time.sleep(5)
    await asyncio.sleep(5)
    return json({'wait': 'wait'}) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
