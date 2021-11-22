"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class Validity(Schema):

    
    priority = fields.Int(required=False)
    

