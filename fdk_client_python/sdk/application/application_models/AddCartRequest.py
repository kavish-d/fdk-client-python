"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AddProductCart import AddProductCart


class AddCartRequest(BaseSchema):

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    

