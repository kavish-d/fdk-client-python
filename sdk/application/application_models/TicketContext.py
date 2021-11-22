"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class TicketContext(Schema):

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    

