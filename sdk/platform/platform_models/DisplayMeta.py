"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DisplayMetaDict import DisplayMetaDict





from .DisplayMetaDict import DisplayMetaDict

from .DisplayMetaDict import DisplayMetaDict




class DisplayMeta(Schema):

    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    description = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    title = fields.Str(required=False)
    

