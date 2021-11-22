"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class InsertResponse(Schema):

    
    count = fields.Int(required=False)
    

