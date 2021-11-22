"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class PointsResponse(Schema):

    
    points = fields.Float(required=False)
    

