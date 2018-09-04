from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import validates
from server import db

class Brewery(db.Model):
    """ A Model that houses information on artists. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Artist. """

    name = Column(TEXT, nullable=False)
    """ The unique name of a given Artist. Every Artist must have
    a non-empty name. """

    address = Column(TEXT)
    """ The date of birth associated with a given Artist. """

    phone = Column(TEXT)
    """ The date of death associated with a given Artist. """

    country = Column(TEXT)
    """ The nationality associated with a given Artist. """

    state = Column(TEXT)
    """ The country associated with a given Artist. """

    def __init__(self, name, address='',phone='',country='',state=''):
        self.name = name
        self.phone =phone
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
                                self.phone,
                                self.country,
                                self.state)

    def serialize(self):
        """ Return JSON representation of artist. """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "country": self.country,
            "state": self.state,
        }