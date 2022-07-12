from functools import wraps


def cache_decor(func):
    @wraps(func)  # использован стандартый модуль wraps для автозаполнения: __name__; __doc__
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())

        if cache_key not in wrapper.cache:
            print('Added new item')
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper


@cache_decor
def multiplier(x: int):
    """Multiplier multiplies some stuff (power 2)."""
    return x ** 2


# --------------------- Main ---------------------
if __name__ == '__main__':
    print(multiplier(5))
    print(multiplier(6))
    print(multiplier(6))
    print(multiplier(7))

    print('\n--------------------- Some info ---------------------')
    print(multiplier.__name__)
    print(multiplier.__doc__)
