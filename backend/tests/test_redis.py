import os
import sys
from services.redis_services import cache_result, get_cache

cache_result("symptom", "high risk")

print(get_cache("symptom"))