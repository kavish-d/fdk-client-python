"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .MetaDataListingFilterMetaResponse import MetaDataListingFilterMetaResponse


class MetaDataListingFilterResponse(BaseSchema):

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponse, required=False), required=False)
    

