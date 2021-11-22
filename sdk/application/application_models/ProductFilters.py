"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductFiltersKey import ProductFiltersKey

from .ProductFiltersValue import ProductFiltersValue


class ProductFilters(Schema):

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    

