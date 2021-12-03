"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .MetaDataListingFilterResponse import MetaDataListingFilterResponse

from .MetaDataListingSortResponse import MetaDataListingSortResponse


class MetaDataListingResponse(BaseSchema):

    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    

