"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class PagePublishRequest(Schema):

    
    publish = fields.Boolean(required=False)
    

