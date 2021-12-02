"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class Links(BaseSchema):

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    

