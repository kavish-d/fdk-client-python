"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class DeleteCardsResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

