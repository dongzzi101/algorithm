N, M = map(int, input().split())

site_and_password = {}

for _ in range(N):
    site, password = input().split()
    site_and_password[site] = password

sites = []

for _ in range(M):
    sites.append(input())

for site in sites:
    print(site_and_password[site])





