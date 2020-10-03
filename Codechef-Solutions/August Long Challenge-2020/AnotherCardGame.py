tests = int(input())

def solve(C, R):
	c = C//9
	r = R//9
	if not C%9 ==0:
		c += 1
	if not R%9 == 0:
		r += 1
	if c < r:
		return [0, c]
	else:
		return [1, r]
	

for t in range(tests):
	C, R = map(int, input().split())
	ans = solve(C, R)
	print(ans[0], ans[1])



        



