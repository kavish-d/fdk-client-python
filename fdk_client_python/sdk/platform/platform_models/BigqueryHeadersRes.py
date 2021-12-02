"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BigqueryHeadersResHeaders import BigqueryHeadersResHeaders


class BigqueryHeadersRes(BaseSchema):

    
    headers = fields.List(fields.Nested(BigqueryHeadersResHeaders, required=False), required=False)
    

