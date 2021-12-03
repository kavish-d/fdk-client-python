"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Destination(BaseSchema):

    
    namespace = fields.Str(required=False)
    
    rewrite = fields.Str(required=False)
    
    basepath = fields.Str(required=False)
    
