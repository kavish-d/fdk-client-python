"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AppInventoryCompanies import AppInventoryCompanies

from .Page import Page


class CompaniesResponse(Schema):

    
    items = fields.Nested(AppInventoryCompanies, required=False)
    
    page = fields.Nested(Page, required=False)
    

