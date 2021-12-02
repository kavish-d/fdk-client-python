"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class MetaDataListingSortMetaResponse(BaseSchema):

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

