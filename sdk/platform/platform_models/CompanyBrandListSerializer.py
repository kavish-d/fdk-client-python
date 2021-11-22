"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CompanyBrandSerializer import CompanyBrandSerializer

from .Page import Page


class CompanyBrandListSerializer(Schema):

    
    items = fields.List(fields.Nested(CompanyBrandSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

