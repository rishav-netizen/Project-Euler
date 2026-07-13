from array import array
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"

    for n in range(2, isqrt(limit) + 1):
        if is_prime[n]:
            start = n * n
            is_prime[start:limit + 1:n] = b"\x00" * (((limit - start) // n) + 1)

    return [n for n in range(2, limit + 1) if is_prime[n]]


def first_consecutive_numbers(
    limit: int,
    consecutive_count: int,
    segment_size: int = 1_000_000,
) -> list[int] | None:
    primes = primes_upto(isqrt(limit))
    run_length = 0

    for low in range(2, limit + 1, segment_size):
        high = min(low + segment_size - 1, limit)
        size = high - low + 1
        factor_counts = bytearray(size)
        remaining = array("I", range(low, high + 1))

        for prime in primes:
            if prime * prime > high:
                break

            start = ((low + prime - 1) // prime) * prime
            for multiple in range(start, high + 1, prime):
                index = multiple - low
                value = remaining[index]
                if value % prime == 0:
                    factor_counts[index] += 1
                    while value % prime == 0:
                        value //= prime
                    remaining[index] = value

        for index, count in enumerate(factor_counts):
            if remaining[index] > 1:
                count += 1

            if count == consecutive_count:
                run_length += 1
                if run_length == consecutive_count:
                    end = low + index
                    return list(range(end - consecutive_count + 1, end + 1))
            else:
                run_length = 0

    return None


if __name__ == "__main__":
    limit = 130_000_000
    consecutive_count = 5

    result = first_consecutive_numbers(limit, consecutive_count)
    if result is not None:
        print(result)
