"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class UnauthenticatedSchema(Schema):

    
    authenticated = fields.Boolean(required=False)
    

