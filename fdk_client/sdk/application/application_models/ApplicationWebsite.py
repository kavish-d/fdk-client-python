"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ApplicationWebsite(BaseSchema):

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    

