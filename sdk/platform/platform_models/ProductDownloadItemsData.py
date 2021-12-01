"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ProductDownloadItemsData(BaseSchema):

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    templates = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

