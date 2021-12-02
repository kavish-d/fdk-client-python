"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class Upload(BaseSchema):

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    

