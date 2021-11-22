"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class Points(Schema):

    
    available = fields.Float(required=False)
    

