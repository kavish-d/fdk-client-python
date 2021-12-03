"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .AppCatalogConfiguration import AppCatalogConfiguration


class GetAppCatalogConfiguration(BaseSchema):

    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(AppCatalogConfiguration, required=False)
    
