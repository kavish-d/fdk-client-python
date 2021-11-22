"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ProductFiltersValue import ProductFiltersValue

from .ProductFiltersKey import ProductFiltersKey


class ProductFilters(Schema):

    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    
    key = fields.Nested(ProductFiltersKey, required=False)
    

