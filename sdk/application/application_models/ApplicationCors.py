"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ApplicationCors(Schema):

    
    domains = fields.List(fields.Str(required=False), required=False)
    

