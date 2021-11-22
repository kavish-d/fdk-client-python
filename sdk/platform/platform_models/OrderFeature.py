"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class OrderFeature(Schema):

    
    buy_again = fields.Boolean(required=False)
    

