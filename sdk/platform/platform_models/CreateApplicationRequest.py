"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .App import App

from .AppInventory import AppInventory

from .AppDomain import AppDomain


class CreateApplicationRequest(Schema):

    
    app = fields.Nested(App, required=False)
    
    configuration = fields.Nested(AppInventory, required=False)
    
    domain = fields.Nested(AppDomain, required=False)
    

