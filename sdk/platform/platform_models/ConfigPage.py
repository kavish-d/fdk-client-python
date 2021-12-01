"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ConfigPage(BaseSchema):

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    

