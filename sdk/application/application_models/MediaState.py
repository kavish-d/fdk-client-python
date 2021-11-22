"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class MediaState(Schema):

    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    

