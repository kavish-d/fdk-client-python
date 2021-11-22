"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CartMetaMissingResponse(Schema):

    
    errors = fields.List(fields.Str(required=False), required=False)
    

