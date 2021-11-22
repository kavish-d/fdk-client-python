"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .BigqueryHeadersResHeaders import BigqueryHeadersResHeaders


class BigqueryHeadersRes(Schema):

    
    headers = fields.List(fields.Nested(BigqueryHeadersResHeaders, required=False), required=False)
    

