"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class CatalogMasterConfig(BaseSchema):

    
    source_slug = fields.Str(required=False)
    

