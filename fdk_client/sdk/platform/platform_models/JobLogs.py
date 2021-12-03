"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .JobLog import JobLog

from .Page import Page


class JobLogs(BaseSchema):

    
    items = fields.List(fields.Nested(JobLog, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
