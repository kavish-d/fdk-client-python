"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class PageContent(Schema):

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

