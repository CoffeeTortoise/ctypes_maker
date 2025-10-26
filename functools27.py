
def wraps(original_func):

	def wrap(func):
		func.__name__ = original_func.__name__
		func.__module__ = original_func.__module__
		func.__doc__ = original_func.__doc__
		return func
	return wrap


def lru_cache(maxsize=128):
	mem = {}

	@wraps(lru_cache)
	def cache(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			key = hash(args) + hash(tuple(kwargs.items()))
			if key in mem:
				return mem[key]
			if len(mem) > maxsize:
				del_keys = list(mem)[:int(maxsize * .3)]
				for k in del_keys:
					del mem[k]
			res = func(*args, **kwargs)
			mem[key] = res
			return res
		return wrapper
	return cache


def cached_method(maxsize=128):
	mem = {}

	@wraps(cached_method)
	def cache(func):

		@wraps(func)
		def wrapper(self, *args, **kwargs):
			key = id(self) + hash(args) + hash(tuple(kwargs.items()))
			if key in mem:
				return mem[key]
			if len(mem) > maxsize:
				del_k = list(mem)[:int(maxsize * .3)]
				for k in del_k:
					del mem[k]
			mem[key] = func(self, *args, **kwargs)
			return mem[key]
		return wrapper
	return cache


def total_ordering(eq=True, ne=True, gt=True, lt=True, ge=True, le=True):

	def create_proxy(cls):

		class Proxy(cls):

			def comparator(self, other, attr):
				if self.__dict__[attr] > other.__dict__[attr]:
					return 1
				elif self.__dict__[attr] == other.__dict__[attr]:
					return 0
				else:
					return -1

			def __eq__(self, other):
				if not eq:
					return cls.__eq__(self, other)
				return isinstance(other, (cls, type(self))) and all(self.comparator(other, item) == 0 for item in self.__dict__ if item in other.__dict__)

			def __ne__(self, other):
				if not ne:
					return cls.__ne__(self, other)
				return not self.__eq__(other)

			def __gt__(self, other):
				if not gt:
					return cls.__gt__(self, other)
				return isinstance(other, (cls, type(self))) and all(self.comparator(other, item) == 1 for item in self.__dict__ if item in other.__dict__)

			def __lt__(self, other):
				if not lt:
					return cls.__lt__(self, other)
				return not self.__gt__(other)

			def __ge__(self, other):
				if not ge:
					return cls.__ge__(self, other)
				return self.__gt__(other) or self.__eq__(other)

			def __le__(self, other):
				if not le:
					return cls.__le__(self, other)
				return self.__lt__(other) or self.__eq__(other)

		return Proxy
	return create_proxy


def frozen_func(func):

	class F:

		def __init__(self, f, *args, **kwargs):
			self.__f = f
			self.__args = args
			self.__kwargs = kwargs

		def __call__(self):
			return self.__f(*self.__args, **self.__kwargs)

	@wraps(func)
	def wrapper(*args, **kwargs):
		return F(func, *args, **kwargs)
	return wrapper


class SingleDispatch:

	def __init__(self):
		self.__funcs = {}

	def register(self, func, type_):
		self.__funcs[type_] = func

	def __call__(self, *args, **kwargs):
		t = type(args[0]) if args else None
		return self.__funcs[t](*args, **kwargs)


def reducer(func, iterable, initial=0):
	for el in iterable:
		initial = func(initial, el)
	return initial


def accumulator(func, iterable, initial=0):
	res = sum(func(el) for el in iterable)
	res += initial
	return res
