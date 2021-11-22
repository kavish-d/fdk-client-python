"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ProductSizeDeleteDataResponse import ProductSizeDeleteDataResponse




class ProductSizeDeleteResponse(Schema):

    
    data = fields.Nested(ProductSizeDeleteDataResponse, required=False)
    
    success = fields.Boolean(required=False)
    

