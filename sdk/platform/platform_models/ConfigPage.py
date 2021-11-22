"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ConfigPage(Schema):

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    

