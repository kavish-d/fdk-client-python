"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .PhoneSchema import PhoneSchema

from .EmailSchema import EmailSchema


class ContactSchema(Schema):

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    

