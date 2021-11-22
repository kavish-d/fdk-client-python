"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class RegistrationPageFeature(Schema):

    
    ask_store_address = fields.Boolean(required=False)
    

