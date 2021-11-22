"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DeploymentMeta import DeploymentMeta


class OrderingStoreConfig(Schema):

    
    deployment_meta = fields.Nested(DeploymentMeta, required=False)
    

