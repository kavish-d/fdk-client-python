"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class AnnouncementAuthorSchema(BaseSchema):
    # Content swagger.json

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    

