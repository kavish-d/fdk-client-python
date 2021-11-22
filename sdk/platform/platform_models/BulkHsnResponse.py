"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class BulkHsnResponse(Schema):

    
    success = fields.Boolean(required=False)
    

