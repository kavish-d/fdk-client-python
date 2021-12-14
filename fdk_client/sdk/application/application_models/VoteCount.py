"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class VoteCount(BaseSchema):
    # Feedback swagger.json

    
    downvote = fields.Int(required=False)
    
    upvote = fields.Int(required=False)
    

