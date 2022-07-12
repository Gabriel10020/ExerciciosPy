from time import sleep
for c in range(10, 0, -1):
    print(f'\033[97m {c}')
    sleep(1)
print('\033[93mFogos explodindo!')