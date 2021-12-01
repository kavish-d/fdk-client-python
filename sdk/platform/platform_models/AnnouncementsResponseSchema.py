"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class AnnouncementsResponseSchema(BaseSchema):

    
    announcements = fields.Dict(required=False)
    
    refresh_rate = fields.Int(required=False)
    
    refresh_pages = fields.List(fields.Str(required=False), required=False)
    

