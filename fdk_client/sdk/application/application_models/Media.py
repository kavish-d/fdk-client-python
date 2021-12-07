"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Meta import Meta






class Media(BaseSchema):

    
    meta = fields.Nested(Meta, required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

