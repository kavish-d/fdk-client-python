"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class AnnouncementsResponseSchema(Schema):

    
    announcements = fields.Dict(required=False)
    
    refresh_rate = fields.Int(required=False)
    
    refresh_pages = fields.List(fields.Str(required=False), required=False)
    

