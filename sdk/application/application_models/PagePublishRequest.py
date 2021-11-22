"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class PagePublishRequest(Schema):

    
    publish = fields.Boolean(required=False)
    

