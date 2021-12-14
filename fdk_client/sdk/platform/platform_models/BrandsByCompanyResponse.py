"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CompanyBrandInfo import CompanyBrandInfo


class BrandsByCompanyResponse(BaseSchema):
    # Configuration swagger.json

    
    brands = fields.Nested(CompanyBrandInfo, required=False)
    

