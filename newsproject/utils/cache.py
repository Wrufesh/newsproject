from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


def invalidate_template_cache(fragment_name, *variables):
    cache_key = make_template_fragment_key(fragment_name, variables)
    cache.delete(cache_key)
