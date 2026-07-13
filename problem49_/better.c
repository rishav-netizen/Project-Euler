#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define LIMIT 10000
#define MAX_PRIMES 2000
#define MAX_GROUPS 1000
#define MAX_GROUP_SIZE 20

typedef struct
{
    int digits[10];
} DigitKey;

typedef struct
{
    DigitKey key;
    int primes[MAX_GROUP_SIZE];
    int size;
} Group;

bool is_prime[LIMIT];
int primes[MAX_PRIMES];
int primeCount = 0;

Group groups[MAX_GROUPS];
int groupCount = 0;

void sieve(int lower, int upper)
{
    for (int i = 0; i < LIMIT; i++)
        is_prime[i] = true;

    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i * i <= upper; i++)
    {
        if (is_prime[i])
        {
            for (int j = i * i; j <= upper; j += i)
                is_prime[j] = false;
        }
    }

    for (int i = lower; i <= upper; i++)
    {
        if (is_prime[i])
            primes[primeCount++] = i;
    }
}

DigitKey makeKey(int number)
{
    DigitKey key = {0};

    while (number > 0)
    {
        key.digits[number % 10]++;
        number /= 10;
    }

    return key;
}

bool sameKey(DigitKey a, DigitKey b)
{
    for (int i = 0; i < 10; i++)
    {
        if (a.digits[i] != b.digits[i])
            return false;
    }

    return true;
}

void buildGroups()
{
    for (int i = 0; i < primeCount; i++)
    {
        DigitKey key = makeKey(primes[i]);

        int index = -1;

        for (int j = 0; j < groupCount; j++)
        {
            if (sameKey(groups[j].key, key))
            {
                index = j;
                break;
            }
        }

        if (index == -1)
        {
            groups[groupCount].key = key;
            groups[groupCount].size = 0;
            index = groupCount++;
        }

        groups[index].primes[groups[index].size++] = primes[i];
    }
}

bool isAP(int a, int b, int c)
{
    return (b - a) == (c - b);
}

void findSequence()
{
    for (int g = 0; g < groupCount; g++)
    {
        if (groups[g].size < 3)
            continue;

        for (int i = 0; i < groups[g].size - 2; i++)
        {
            for (int j = i + 1; j < groups[g].size - 1; j++)
            {
                for (int k = j + 1; k < groups[g].size; k++)
                {
                    int a = groups[g].primes[i];
                    int b = groups[g].primes[j];
                    int c = groups[g].primes[k];

                    if (isAP(a, b, c))
                    {
                        printf("%d%d%d\n", a, b, c);
                        return;
                    }
                }
            }
        }
    }
}

int main()
{
    sieve(1500, 9999);
    buildGroups();
    findSequence();

    return 0;
}