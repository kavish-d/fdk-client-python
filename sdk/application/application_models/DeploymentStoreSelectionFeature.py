"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class DeploymentStoreSelectionFeature(BaseSchema):

    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

