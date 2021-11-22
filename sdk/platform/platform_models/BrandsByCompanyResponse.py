"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CompanyBrandInfo import CompanyBrandInfo


class BrandsByCompanyResponse(Schema):

    
    brands = fields.Nested(CompanyBrandInfo, required=False)
    

