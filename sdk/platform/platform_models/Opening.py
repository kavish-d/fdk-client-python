"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Opening(Schema):

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    

