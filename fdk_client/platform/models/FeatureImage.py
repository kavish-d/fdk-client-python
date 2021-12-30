"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class FeatureImage(BaseSchema):
    # Content swagger.json

    
    secure_url = fields.Str(required=False)
    
