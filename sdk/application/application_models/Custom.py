"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Custom(Schema):

    
    props = fields.Dict(required=False)
    

