"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class OptinCompanyMetrics(BaseSchema):

    
    brand = fields.Int(required=False)
    
    store = fields.Int(required=False)
    
    company = fields.Str(required=False)
    

