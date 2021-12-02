"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class RedirectionSchema(BaseSchema):

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    

