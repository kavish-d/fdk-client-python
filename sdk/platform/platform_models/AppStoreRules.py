"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AppStoreRules(Schema):

    
    companies = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    

