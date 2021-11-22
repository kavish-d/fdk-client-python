"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class HasPasswordSuccess(Schema):

    
    result = fields.Boolean(required=False)
    

