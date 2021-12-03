"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .CopyFileTask import CopyFileTask


class BulkResponse(BaseSchema):

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    
