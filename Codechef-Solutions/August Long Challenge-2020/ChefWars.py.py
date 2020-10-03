import math

def solve(H, P):
	while H > 0:
		H = H  - P
		if H <= 0:
			break
		P = math.floor(P/2)

		if P <= 0:
			return 0
	return 1

tests = int(input())

for t in range(tests):
	H, P = map(int, input().split())
	print(solve(H, P))


