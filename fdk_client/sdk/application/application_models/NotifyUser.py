"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class NotifyUser(BaseSchema):
    # Lead swagger.json

    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    

