"""
Legacy import surface for coaching views.

The URLConf still imports `coaching.views`, so this module re-exports the
single maintained implementation from `views_v2`.
"""

from .views_v2 import (  # noqa: F401
    assign_member,
    coach_create,
    coach_delete,
    coach_detail,
    coach_list,
    coach_update,
    remove_member,
)
