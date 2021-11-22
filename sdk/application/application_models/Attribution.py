"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Attribution(Schema):

    
    campaign_cookie_expiry = fields.Str(required=False)
    

