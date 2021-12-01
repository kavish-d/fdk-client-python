"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class GetShareCartLinkResponse(BaseSchema):

    
    token = fields.Str(required=False)
    
    share_url = fields.Str(required=False)
    

