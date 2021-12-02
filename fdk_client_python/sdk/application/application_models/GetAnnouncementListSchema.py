"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AdminAnnouncementSchema import AdminAnnouncementSchema

from .Page import Page


class GetAnnouncementListSchema(BaseSchema):

    
    items = fields.List(fields.Nested(AdminAnnouncementSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

