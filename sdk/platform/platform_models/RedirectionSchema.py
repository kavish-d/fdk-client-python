"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class RedirectionSchema(Schema):

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    

