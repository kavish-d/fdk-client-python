"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CommunicationOptinDialogFeature(Schema):

    
    visibility = fields.Boolean(required=False)
    

