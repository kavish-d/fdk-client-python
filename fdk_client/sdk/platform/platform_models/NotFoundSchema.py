"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class NotFoundSchema(BaseSchema):
    # User swagger.json

    
    message = fields.Str(required=False)
    

