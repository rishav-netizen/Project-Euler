#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct ArrayHash {
    size_t operator()(const array<int, 10>& arr) const {
        size_t h = 0;
        for (int x : arr) {
            h ^= hash<int>{}(x) + 0x9e3779b9 + (h << 6) + (h >> 2);
        }
        return h;
    }
};

vector<int> primes_between(int lower_limit, int upper_limit)
{
    if (upper_limit <= 1)
        return {};

    vector<bool> is_prime(upper_limit + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i * i <= upper_limit; i++)
    {
        if (is_prime[i])
        {
            for (int j = i * i; j <= upper_limit; j += i)
                is_prime[j] = false;
        }
    }

    vector<int> primes;

    for (int i = lower_limit; i <= upper_limit; i++)
    {
        if (is_prime[i])
            primes.push_back(i);
    }

    return primes;
}

bool isItAp(const vector<int>& numbers)
{
    int d = numbers[1] - numbers[0];

    for (size_t i = 1; i < numbers.size() - 1; i++)
    {
        if (numbers[i + 1] - numbers[i] != d)
            return false;
    }

    return true;
}

unordered_map<array<int, 10>, vector<int>, ArrayHash>
segregator(const vector<int>& primes)
{
    unordered_map<array<int, 10>, vector<int>, ArrayHash> groups;

    for (int number : primes)
    {
        array<int, 10> digit_count{};

        int n = number;

        while (n > 0)
        {
            digit_count[n % 10]++;
            n /= 10;
        }

        groups[digit_count].push_back(number);
    }

    return groups;
}

vector<int> tripletMaker(
    const unordered_map<array<int, 10>, vector<int>, ArrayHash>& groups)
{
    for (const auto& [key, group] : groups)
    {
        if (group.size() < 3)
            continue;

        for (size_t i = 0; i < group.size() - 2; i++)
        {
            for (size_t j = i + 1; j < group.size() - 1; j++)
            {
                for (size_t k = j + 1; k < group.size(); k++)
                {
                    vector<int> triplet = {group[i], group[j], group[k]};

                    if (isItAp(triplet))
                        return triplet;
                }
            }
        }
    }

    return {};
}

string result(const vector<int>& triplet)
{
    string ans;

    for (int number : triplet)
        ans += to_string(number);

    return ans;
}

int main()
{
    vector<int> primes = primes_between(1500, 9999);

    auto groups = segregator(primes);

    vector<int> triplet = tripletMaker(groups);

    cout << result(triplet) << '\n';
}