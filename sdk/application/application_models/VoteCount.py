"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class VoteCount(Schema):

    
    downvote = fields.Int(required=False)
    
    upvote = fields.Int(required=False)
    

