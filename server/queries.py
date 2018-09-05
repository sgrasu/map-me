import decimal
from math import ceil
from flask import request, jsonify
from server import app
from server.models import *

ITEMS_PER_PAGE = 16


def response(status, data, pages):
    ret = {"status": status, "pages": pages, "data": data}
    return jsonify(ret)


"""
########## Query Routes ##########
"""


@app.route("/query_brewery")
def url_query_brewery():
    breweries, page_count = query_brewery(request.args.to_dict())
    serialized_models = list(map(lambda x: x.serialize(), breweries))
    return response(200, serialized_models, page_count)
