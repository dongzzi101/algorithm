L = int(input())
s = input().strip()

MOD = 1234567891
hash_value = 0
power = 1  # 31^0

for c in s:
    hash_value = (hash_value + (ord(c) - 96) * power) % MOD
    power = (power * 31) % MOD

print(hash_value)
