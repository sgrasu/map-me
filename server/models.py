from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import validates
from server import db

class Brewery(db.Model):
    """ A Model that houses information on artists. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a brewery. """

    name = Column(TEXT, nullable=False)
    """ The unique name of a given brewery, every brewery must
        have a non-null name. """

    address = Column(TEXT)
    """ The address associated with a brewery """

    telephone = Column(TEXT)
    """ The telephone number of a brewery. """

    country = Column(TEXT)
    """ The country the brewery is located in. """

    state = Column(TEXT)
    """ The state associated with the brewery, if applicable. """
    
    latitude = Column(Numeric)
    """ the latitude of the brewery's address """

    longitude = Column(Numeric)
    """ the longitude of the brewery's address """



    def __init__(self, name, address='',telephone='',country='',state='', latitude=None, longitude = None):
        self.name = name
        self.telephone =telephone
        self.address = address
        self.country = country
        self.state = state
    @validates('name', include_removes=True)
    def __validates_name(self, key, name, is_remove):
        """ Validate the Artist.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and name != '', \
            "A brewery must have a name"
        return name

    def __repr__(self):
        """ Return a formatted String representation
        of a given Artist. """
        return "<Artist: {}> {} ({}:{}), {} [Country:{}".format(self.id,
                                self.name,
                                self.address,
                                self.telephone,
                                self.country,
                                self.state)

    def serialize(self):
        """ Return JSON representation of artist. """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "telephone": self.telephone,
            "country": self.country,
            "state": self.state,
            "latitude": self.latitude,
            "longitude": self.longitude
        }