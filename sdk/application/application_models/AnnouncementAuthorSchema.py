"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class AnnouncementAuthorSchema(Schema):

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    

