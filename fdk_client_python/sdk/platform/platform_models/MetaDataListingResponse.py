"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .MetaDataListingSortResponse import MetaDataListingSortResponse

from .MetaDataListingFilterResponse import MetaDataListingFilterResponse


class MetaDataListingResponse(BaseSchema):

    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    

