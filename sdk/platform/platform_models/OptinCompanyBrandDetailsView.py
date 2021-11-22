"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .CompanyBrandDetail import CompanyBrandDetail


class OptinCompanyBrandDetailsView(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    

