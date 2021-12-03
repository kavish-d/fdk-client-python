"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .BrandBannerSerializer import BrandBannerSerializer














class CreateUpdateBrandRequestSerializer(BaseSchema):

    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    brand_tier = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
