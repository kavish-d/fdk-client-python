"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class DeviceMeta(Schema):

    
    app_version = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    

