from asyncio.base_futures import _format_callbacks
from flask import Flask

web = Flask(__name__) # republish web class



# to create first pange how to respond. 
@web.route("/")

def index():
    return "hello flask"

web.run()
