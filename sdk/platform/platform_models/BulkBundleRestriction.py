"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class BulkBundleRestriction(Schema):

    
    multi_store_allowed = fields.Boolean(required=False)
    

