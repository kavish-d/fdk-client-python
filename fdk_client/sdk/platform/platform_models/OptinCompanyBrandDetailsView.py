"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CompanyBrandDetail import CompanyBrandDetail

from .Page import Page


class OptinCompanyBrandDetailsView(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

