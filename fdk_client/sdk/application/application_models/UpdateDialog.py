"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class UpdateDialog(BaseSchema):

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    
