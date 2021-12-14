"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class Seller(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

