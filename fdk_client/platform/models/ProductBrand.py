"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Media1 import Media1



from .Action import Action


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    

