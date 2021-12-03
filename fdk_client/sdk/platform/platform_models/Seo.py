"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Seo(BaseSchema):

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
