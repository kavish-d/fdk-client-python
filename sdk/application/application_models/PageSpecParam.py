"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class PageSpecParam(Schema):

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    

