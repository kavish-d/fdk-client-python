"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .MetaDataListingFilterMetaResponse import MetaDataListingFilterMetaResponse


class MetaDataListingFilterResponse(Schema):

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponse, required=False), required=False)
    

