"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Rule import Rule

from .State import State

from .Validity import Validity

from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule

from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .Identifier import Identifier

from .Restrictions import Restrictions

from .CouponAuthor import CouponAuthor

from .Ownership import Ownership






class CouponUpdate(Schema):

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    

