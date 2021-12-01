"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class PromiseFormatted(BaseSchema):

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

