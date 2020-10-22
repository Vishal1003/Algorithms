class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N
        # print("N: {}\n index: {}\n ans: {}".format(N, index, ans))

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
            # print("ans: {}\n index: {}".format(ans, index))

        return ans