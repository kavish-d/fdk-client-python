"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class UpdateResponse(BaseSchema):
    # Feedback swagger.json

    
    count = fields.Int(required=False)
    

