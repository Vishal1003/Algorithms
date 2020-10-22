class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_list = list()
        table_f_dict = {}
        for order in orders:
            table_no = order[1]
            food_item = order[2]
            if not food_item in food_list:
                food_list.append(food_item)
                
            table_f_dict.setdefault(table_no, list()).append(food_item)
            
        sorted_food_list = sorted(food_list)
        
        ans = []
        ans.append(['Table'] + sorted_food_list)
        
        temp_list = []
        d_keys = list(table_f_dict.keys())
        
        sorted_d_key = sorted(d_keys, key=lambda x: int(x))
        for table in sorted_d_key:
            temp_list.append(table)
            f_list = table_f_dict[table]
            for f in sorted_food_list:
                if f in f_list:
                    cnt_str = str(f_list.count(f))
                    temp_list.append(cnt_str)
                else:
                    temp_list.append('0')
            
            ans.append(temp_list)
            temp_list = []
                    
        return ans