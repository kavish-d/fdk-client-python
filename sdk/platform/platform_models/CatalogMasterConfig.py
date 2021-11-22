"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CatalogMasterConfig(Schema):

    
    source_slug = fields.Str(required=False)
    

