"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .CompanyOptIn import CompanyOptIn


class GetOptInPlatform(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyOptIn, required=False), required=False)
    

