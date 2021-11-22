"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .Card import Card




class ListCardsResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    message = fields.Str(required=False)
    

