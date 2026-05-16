"""
Legacy import surface for product views.

The URLConf still imports `products.views`, so this module re-exports the
single maintained implementation from `views_v2`.
"""

from .views_v2 import (  # noqa: F401
    product_create,
    product_delete,
    product_detail,
    product_list,
    product_update,
    stock_dashboard,
    stock_movement_create,
    stock_movement_list,
)
