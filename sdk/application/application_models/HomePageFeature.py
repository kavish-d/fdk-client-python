"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class HomePageFeature(Schema):

    
    order_processing = fields.Boolean(required=False)
    

