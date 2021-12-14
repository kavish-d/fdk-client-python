"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .LandingPageSchema import LandingPageSchema




class LandingPage(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(LandingPageSchema, required=False)
    
    success = fields.Boolean(required=False)
    

