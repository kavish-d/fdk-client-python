"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class FollowPostResponse(Schema):

    
    id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

