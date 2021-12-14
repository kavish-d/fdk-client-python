"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class Attribution(BaseSchema):
    # Share swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    

