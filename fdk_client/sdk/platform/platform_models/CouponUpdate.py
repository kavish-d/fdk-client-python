"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Identifier import Identifier

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .State import State





from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta

from .RuleDefinition import RuleDefinition

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .Validation import Validation

from .Rule import Rule


class CouponUpdate(BaseSchema):

    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
