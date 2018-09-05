from flask import render_template
from server import app
from server.models import *
from server.queries import *

from subprocess import call


@app.route('/api/breweries/all')
def brewery_all():
    breweries = Brewery.query.all()
    return response(200, [brewery.serialize() for brewery in breweries], 1)


@app.route('/api/breweries/<int:id>')
def brewery_one(id):
    brewery = Brewery.query.filter_by(id=id).first()
    return response(200, brewery.serialize(), 1)


@app.route('/api/breweries/country=<string:country>')
def brewery_country(country):
    breweries = Brewery.query.filter_by(country=country).all()
    return response(200, [brewery.serialize() for brewery in breweries], 1)


