"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AdminAnnouncementSchema import AdminAnnouncementSchema

from .Page import Page


class GetAnnouncementListSchema(Schema):

    
    items = fields.List(fields.Nested(AdminAnnouncementSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

