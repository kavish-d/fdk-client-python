"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class Custom(Schema):

    
    props = fields.Dict(required=False)
    

