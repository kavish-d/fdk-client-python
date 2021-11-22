"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class GetShareCartLinkResponse(Schema):

    
    token = fields.Str(required=False)
    
    share_url = fields.Str(required=False)
    

