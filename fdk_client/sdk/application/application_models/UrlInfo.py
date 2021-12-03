"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class UrlInfo(BaseSchema):

    
    original = fields.Str(required=False)
    
    short = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    

