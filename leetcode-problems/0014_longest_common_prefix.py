class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0:
            sorted_str_list = sorted(strs, key=lambda x: len(x))
            max_count = len(sorted_str_list[0])
            temp_list = []
            final_str_list = []
            final_str = ""
            count = 0
            for count in range(0, max_count, 1):
                for word in sorted_str_list:
                    temp_list.append(word[count])
                if temp_list.count(temp_list[0]) == len(temp_list):
                    final_str_list.append(temp_list[0])
                    temp_list = []
                    continue
                else:
                    break

            if len(final_str_list) != 0:
                final_str = final_str.join(final_str_list)
                return final_str
                # print(final_str)
            else:
                return ""
                # print("")
        else:
            return ""
            # print("")

