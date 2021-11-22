"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *














class QNAState(Schema):

    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    modify = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    reply = fields.Boolean(required=False)
    
    vote = fields.Boolean(required=False)
    

