def primes_between(lower_limit: int, upper_limit: int) -> list:
	if upper_limit <= 1:
		return set()

	is_prime = [True] * (upper_limit + 1)
	is_prime[0] = is_prime[1] = False

	for a in range(2, int(upper_limit ** 0.5) + 1):
		if is_prime[a]:
			for multiples in range(a*a, upper_limit + 1, a):
				is_prime[multiples] = False

	primes = []
	for x in range(lower_limit, upper_limit + 1):
		if is_prime[x]:
			primes.append(x)

	return primes

def isItAp(numbers: list) -> bool:
	length = len(numbers)
	d = numbers[1] - numbers[0]
	for i in range(1, length - 1):
		current_d = numbers[i+1] - numbers[i]
		if current_d != d:
			return False
	return True

def segregator() -> dict:
	groups = {}
	for number in primes:
		digit_count = [0] * 10
		for digit in str(number):
			digit_count[int(digit)] += 1
		key = tuple(digit_count)
		groups.setdefault(key, []).append(number)
	
	filtered = {}
	for (key, group) in groups.items():
		if len(group) >= 3:
			filtered[key] = group

	return filtered
	
def tripletMaker() -> list:
	for group in groups.values():
		length = len(group)

		for i in range(length - 2):
			for j in range(i + 1, length - 1):
				for k in range(j + 1, length):
					triplet = [group[i], group[j], group[k]]
					if isItAp(triplet):
						return triplet

def result(triplet: list) -> int:
	str_result = ""
	for number in triplet:
		str_result += str(number)
	return int(str_result)

	# ? Generators in python
	# return "".join(str(number) for number in triplet)

primes = primes_between(1500, 9999)
groups = segregator()
print(result(tripletMaker()))