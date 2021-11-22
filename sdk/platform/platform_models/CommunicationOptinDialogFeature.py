"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CommunicationOptinDialogFeature(Schema):

    
    visibility = fields.Boolean(required=False)
    

