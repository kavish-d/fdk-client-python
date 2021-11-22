"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class GetShareCartLinkRequest(Schema):

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

