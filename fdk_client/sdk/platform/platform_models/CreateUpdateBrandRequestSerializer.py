"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema















from .BrandBannerSerializer import BrandBannerSerializer






class CreateUpdateBrandRequestSerializer(BaseSchema):

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    brand_tier = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    _locale_language = fields.Dict(required=False)
    

