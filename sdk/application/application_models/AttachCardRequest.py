"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class AttachCardRequest(Schema):

    
    nickname = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False)
    
    name_on_card = fields.Str(required=False)
    

