"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .MoengageCredentials import MoengageCredentials




class Moengage(BaseSchema):

    
    credentials = fields.Nested(MoengageCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

