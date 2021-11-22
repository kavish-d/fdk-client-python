"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .CopyFileTask import CopyFileTask


class BulkResponse(Schema):

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    

