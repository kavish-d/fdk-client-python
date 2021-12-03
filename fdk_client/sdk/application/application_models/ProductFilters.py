"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductFiltersValue import ProductFiltersValue

from .ProductFiltersKey import ProductFiltersKey


class ProductFilters(BaseSchema):

    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    
    key = fields.Nested(ProductFiltersKey, required=False)
    
