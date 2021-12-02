"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PhoneSchema import PhoneSchema

from .EmailSchema import EmailSchema


class ContactSchema(BaseSchema):

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    

