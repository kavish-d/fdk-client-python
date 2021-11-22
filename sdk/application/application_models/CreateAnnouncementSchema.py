"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .AdminAnnouncementSchema import AdminAnnouncementSchema


class CreateAnnouncementSchema(Schema):

    
    message = fields.Str(required=False)
    
    data = fields.Nested(AdminAnnouncementSchema, required=False)
    

