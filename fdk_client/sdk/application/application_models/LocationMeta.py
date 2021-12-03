"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Location import Location

from .Location import Location


class LocationMeta(BaseSchema):

    
    demand = fields.Nested(Location, required=False)
    
    supply = fields.Nested(Location, required=False)
    
