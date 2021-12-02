"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AvailablePageScreenPredicate import AvailablePageScreenPredicate

from .AvailablePageUserPredicate import AvailablePageUserPredicate

from .AvailablePageRoutePredicate import AvailablePageRoutePredicate


class AvailablePagePredicate(BaseSchema):

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    

