from rest_framework.throttling import UserRateThrottle

class CategoryThrottle(UserRateThrottle):
    scope = 'category'

class ProductThrottle(UserRateThrottle):
    scope = 'product'

class OrderThrottle(UserRateThrottle):
    scope = 'order'