"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .LocationSerializer import LocationSerializer


class BulkLocationSerializer(Schema):

    
    data = fields.List(fields.Nested(LocationSerializer, required=False), required=False)
    

