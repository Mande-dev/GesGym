"""
Legacy import surface for RH views.

The URLConf still imports `rh.views`, so this module re-exports the single
maintained implementation from `views_v2`.
"""

from .views_v2 import (  # noqa: F401
    attendance_bulk,
    attendance_create,
    attendance_list,
    employee_create,
    employee_delete,
    employee_detail,
    employee_list,
    employee_update,
    payroll_dashboard,
    process_payment,
)
