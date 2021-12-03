"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ArchiveConfig(BaseSchema):

    
    delete = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    archive_dir = fields.Str(required=False)
    

