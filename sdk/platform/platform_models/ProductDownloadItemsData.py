"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ProductDownloadItemsData(Schema):

    
    type = fields.Str(required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    
    templates = fields.List(fields.Str(required=False), required=False)
    

