"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class FreshchatRestoreIdRequestSchema(BaseSchema):
    # User swagger.json

    
    freshchat_restore_id = fields.Str(required=False)
    

