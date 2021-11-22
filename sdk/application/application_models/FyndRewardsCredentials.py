"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class FyndRewardsCredentials(Schema):

    
    public_key = fields.Str(required=False)
    

