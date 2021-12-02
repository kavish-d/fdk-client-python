"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .PhoneProperties import PhoneProperties


class PhoneSchema(BaseSchema):

    
    active = fields.Boolean(required=False)
    
    phone = fields.List(fields.Nested(PhoneProperties, required=False), required=False)
    

