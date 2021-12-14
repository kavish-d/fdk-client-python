"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ConfigPage(BaseSchema):
    # Theme swagger.json

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    

