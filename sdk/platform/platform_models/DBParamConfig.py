"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class DBParamConfig(Schema):

    
    params = fields.Dict(required=False)
    

