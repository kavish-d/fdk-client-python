"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class PageSpec(Schema):

    
    specifications = fields.List(fields.Dict(required=False), required=False)
    

