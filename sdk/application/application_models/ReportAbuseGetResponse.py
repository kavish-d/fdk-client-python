"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AbuseReport import AbuseReport

from .Page import Page


class ReportAbuseGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(AbuseReport, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

