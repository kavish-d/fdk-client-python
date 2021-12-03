"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ProductSetDistributionSize(BaseSchema):

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    

