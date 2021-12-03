"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class MetaDataListingSortMetaResponse(BaseSchema):

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

