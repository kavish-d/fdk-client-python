"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BuildVersion import BuildVersion




class BuildVersionHistory(BaseSchema):

    
    versions = fields.Nested(BuildVersion, required=False)
    
    latest_available_version_name = fields.Str(required=False)
    
