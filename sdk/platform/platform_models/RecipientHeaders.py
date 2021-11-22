"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class RecipientHeaders(Schema):

    
    email = fields.Str(required=False)
    

