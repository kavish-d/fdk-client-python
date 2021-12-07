"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class GetShareCartLinkRequest(BaseSchema):

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    

