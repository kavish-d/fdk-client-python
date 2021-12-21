"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class TeaserTag(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    

