"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class MediaState(BaseSchema):

    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    

