"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CompanyOptIn import CompanyOptIn

from .Page import Page


class GetOptInPlatform(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CompanyOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

