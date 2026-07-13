def primes_between(lower_limit: int, upper_limit: int) -> set:
	if upper_limit <= 1:
		return set()

	is_prime = [True] * (upper_limit + 1)
	is_prime[0] = is_prime[1] = False

	for a in range(2, int(upper_limit ** 0.5) + 1):
		if is_prime[a]:
			for multiples in range(a*a, upper_limit + 1, a):
				is_prime[multiples] = False

	primes = set()
	for x in range(lower_limit, upper_limit + 1):
		if is_prime[x]:
			primes.add(x)

	return primes

def isItAp(numbers: list):
	sorted_numbers = sorted(numbers)
	length = len(numbers)
	d = sorted_numbers[1] - sorted_numbers[0]
	for i in range(1, length - 1):
		current_d = sorted_numbers[i+1] - sorted_numbers[i]
		if current_d != d:
			return False
	return True

def segregator() -> set:
	numbers_count_mapping = {}

	for number in primes:
		digit_count = [0] * 10
		str_num = str(number)
		for digit in str_num:
			digit_count[int(digit)] += 1
		numbers_count_mapping[number] = digit_count
	
	segregated_numbers_set = set()
	
	for i in numbers_count_mapping:
		segregated_numbers = set()
		for j in numbers_count_mapping:
			if i != j and numbers_count_mapping[i] == numbers_count_mapping[j]:
				segregated_numbers.add(i)
				segregated_numbers.add(j)
		if len(segregated_numbers) >= 3:
			segregated_numbers_set.add(frozenset(segregated_numbers))

	return segregated_numbers_set
	
def tripletMaker() -> list:
	for group in groups:
		nums = sorted(group)
		length = len(nums)
		for i in range(length - 2):
			for j in range(i + 1, length - 1):
				for k in range(j + 1, length):
					triplet = [nums[i], nums[j], nums[k]]
					if isItAp(triplet):
						return triplet

def result(triplet: list) -> int:
	str_result = ""
	for number in triplet:
		str_result += str(number)
	return int(str_result)

	# ? Generators in python
	# return "".join(str(number) for number in triplet)


# i start from 1500 because the first triplet is known, my triplet function returns the first trip it finds hence rn it gives answer
if __name__ == "__main__":
	primes = primes_between(1500, 9999)
	groups = segregator()
	print(result(tripletMaker()))

