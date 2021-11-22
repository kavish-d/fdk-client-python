"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ProductSizeStores(Schema):

    
    count = fields.Int(required=False)
    

