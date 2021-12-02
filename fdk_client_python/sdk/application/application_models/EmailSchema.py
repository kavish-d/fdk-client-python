"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .EmailProperties import EmailProperties


class EmailSchema(BaseSchema):

    
    active = fields.Boolean(required=False)
    
    email = fields.List(fields.Nested(EmailProperties, required=False), required=False)
    

