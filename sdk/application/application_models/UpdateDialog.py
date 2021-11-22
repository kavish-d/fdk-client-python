"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class UpdateDialog(Schema):

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    

