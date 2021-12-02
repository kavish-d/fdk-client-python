"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class KeyValue(BaseSchema):

    
    key = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

