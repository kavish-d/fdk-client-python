"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class RegistrationPageFeature(BaseSchema):

    
    ask_store_address = fields.Boolean(required=False)
    

