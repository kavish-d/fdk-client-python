"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class OptinCompanyMetrics(Schema):

    
    store = fields.Int(required=False)
    
    brand = fields.Int(required=False)
    
    company = fields.Str(required=False)
    

