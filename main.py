
def simple_function(name: str = "World") -> str:
	"""Return a simple greeting string.

	Args:
		name: Name to include in the greeting. Defaults to "World".

	Returns:
		A greeting string like 'Hello, {name}!'.
	"""
	return f"Hello, {name}!"


if __name__ == '__main__':
	# Example usages
	print(simple_function())
	print(simple_function("Alice"))
