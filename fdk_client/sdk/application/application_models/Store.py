"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class Store(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    

