"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class AttributeMasterDetails(BaseSchema):

    
    display_type = fields.Str(required=False)
    

