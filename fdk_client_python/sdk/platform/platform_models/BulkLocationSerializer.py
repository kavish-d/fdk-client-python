"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .LocationSerializer import LocationSerializer


class BulkLocationSerializer(BaseSchema):

    
    data = fields.List(fields.Nested(LocationSerializer, required=False), required=False)
    

