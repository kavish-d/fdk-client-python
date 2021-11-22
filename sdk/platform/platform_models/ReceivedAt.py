"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ReceivedAt(Schema):

    
    value = fields.Str(required=False)
    

