"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AvailablePageScreenPredicate import AvailablePageScreenPredicate

from .AvailablePageUserPredicate import AvailablePageUserPredicate

from .AvailablePageRoutePredicate import AvailablePageRoutePredicate


class AvailablePagePredicate(Schema):

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    

