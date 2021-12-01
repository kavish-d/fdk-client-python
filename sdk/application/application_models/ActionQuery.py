"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class ActionQuery(BaseSchema):

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    

