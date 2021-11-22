"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Regular(Schema):

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    

