"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ActionQuery(Schema):

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    

