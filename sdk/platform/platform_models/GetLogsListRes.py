"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .MkpLogsResp import MkpLogsResp

from .Page import Page


class GetLogsListRes(Schema):

    
    items = fields.List(fields.Nested(MkpLogsResp, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

