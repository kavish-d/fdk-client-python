"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .AddProductCart import AddProductCart


class AddCartRequest(Schema):

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    

