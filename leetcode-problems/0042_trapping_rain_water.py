class Solution:
    def trap(self, height):
        size = len(height)
        if size < 3:
            return 0

        total_water = 0
        i, j = 0, len(height) - 1
        l_max, r_max = height[0], height[-1]

        while i <= j:
            l_max, r_max = max(l_max, height[i]), max(r_max, height[j])

            if l_max <= r_max:
                total_water += (l_max - height[i])
                i += 1
            else:
                total_water += (r_max - height[j])
                j -= 1

        return total_water


if __name__ == "__main__":
    sol = Solution()
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = sol.trap(h)
    print(result)
