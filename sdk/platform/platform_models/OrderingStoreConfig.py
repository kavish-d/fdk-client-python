"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DeploymentMeta import DeploymentMeta


class OrderingStoreConfig(BaseSchema):

    
    deployment_meta = fields.Nested(DeploymentMeta, required=False)
    

