from typing import Any
from .interfaces import StrategizedProperty, PropComparator
from .. import util
from .relationships import RelationshipProperty as RelationshipProperty

class ColumnProperty(StrategizedProperty):
    strategy_wildcard_key: str = ...
    columns: Any = ...
    group: Any = ...
    deferred: Any = ...
    instrument: Any = ...
    comparator_factory: Any = ...
    descriptor: Any = ...
    extension: Any = ...
    active_history: Any = ...
    expire_on_flush: Any = ...
    info: Any = ...
    doc: Any = ...
    strategy_key: Any = ...
    def __init__(self, *columns, **kwargs) -> None: ...
    @property
    def expression(self): ...
    def instrument_class(self, mapper): ...
    def do_init(self): ...
    def copy(self): ...
    def merge(self, session, source_state, source_dict, dest_state, dest_dict, load,
              _recursive, _resolve_conflict_map): ...
    class Comparator(util.MemoizedSlots, PropComparator):
        def _memoized_method___clause_element__(self): ...
        def operate(self, op, *other, **kwargs): ...
        def reverse_operate(self, op, other, **kwargs): ...
