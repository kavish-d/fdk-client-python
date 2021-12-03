"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class Facebook(BaseSchema):

    
    app_id = fields.Str(required=False)
    
