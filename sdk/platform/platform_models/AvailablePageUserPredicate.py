"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AvailablePageUserPredicate(Schema):

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    

