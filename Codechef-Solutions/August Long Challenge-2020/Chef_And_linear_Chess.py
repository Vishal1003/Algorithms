tests = int(input())

def solve(N, K, P):
	P.sort(reverse = True)
	for p in P:
		if K%p == 0:
			return p
	return -1

for t in range(tests):
	N, K = map(int, input().split())
	P = list(map(int, input().split()))
	print(solve(N, K, P))



        



