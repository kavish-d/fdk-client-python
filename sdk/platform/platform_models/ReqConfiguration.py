"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ReqConfiguration(Schema):

    
    concurrency = fields.Int(required=False)
    

