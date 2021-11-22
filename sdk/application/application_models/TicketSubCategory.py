"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class TicketSubCategory(Schema):

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

