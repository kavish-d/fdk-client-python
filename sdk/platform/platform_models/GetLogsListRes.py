"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .MkpLogsResp import MkpLogsResp

from .Page import Page


class GetLogsListRes(BaseSchema):

    
    items = fields.List(fields.Nested(MkpLogsResp, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

