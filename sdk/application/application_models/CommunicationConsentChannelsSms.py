"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class CommunicationConsentChannelsSms(Schema):

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

