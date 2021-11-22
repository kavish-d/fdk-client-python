"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .MetaDataListingFilterResponse import MetaDataListingFilterResponse

from .MetaDataListingSortResponse import MetaDataListingSortResponse


class MetaDataListingResponse(Schema):

    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    

