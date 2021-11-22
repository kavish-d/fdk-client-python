"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CampaignShortLink(Schema):

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    

