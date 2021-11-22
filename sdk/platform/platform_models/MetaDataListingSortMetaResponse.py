"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class MetaDataListingSortMetaResponse(Schema):

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

