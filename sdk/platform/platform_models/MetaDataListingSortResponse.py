"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .MetaDataListingSortMetaResponse import MetaDataListingSortMetaResponse


class MetaDataListingSortResponse(Schema):

    
    data = fields.List(fields.Nested(MetaDataListingSortMetaResponse, required=False), required=False)
    

