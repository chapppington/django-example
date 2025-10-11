from ninja import Router

from core.api.v1.customers.handlers import router as customers_router
from core.api.v1.products.handlers import router as products_router
from core.api.v1.reviews.handlers import router as reviews_router


router = Router(tags=["v1"])

products_router.add_router("/", reviews_router)
router.add_router("products/", products_router)
router.add_router("customers/", customers_router)
