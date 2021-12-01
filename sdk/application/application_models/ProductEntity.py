"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .EntityMeta import EntityMeta




class ProductEntity(BaseSchema):

    
    id = fields.Str(required=False)
    
    meta = fields.Nested(EntityMeta, required=False)
    
    type = fields.Str(required=False)
    

