"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class RegistrationPageFeature(Schema):

    
    ask_store_address = fields.Boolean(required=False)
    

