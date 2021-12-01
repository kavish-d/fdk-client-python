"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class FyndRewardsCredentials(BaseSchema):

    
    public_key = fields.Str(required=False)
    

