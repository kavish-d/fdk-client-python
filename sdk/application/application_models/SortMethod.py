"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class SortMethod(BaseSchema):

    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

