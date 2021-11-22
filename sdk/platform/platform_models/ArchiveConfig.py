"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ArchiveConfig(Schema):

    
    delete = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    archive_dir = fields.Str(required=False)
    

