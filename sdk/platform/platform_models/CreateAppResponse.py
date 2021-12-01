"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Application import Application

from .ApplicationInventory import ApplicationInventory


class CreateAppResponse(BaseSchema):

    
    app = fields.Nested(Application, required=False)
    
    configuration = fields.Nested(ApplicationInventory, required=False)
    

