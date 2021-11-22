"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class AnnouncementPageSchema(Schema):

    
    page_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

