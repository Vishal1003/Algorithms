"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        paths ---> each tuple(c1, c2)
        """
        c1 = [c[0] for c in paths]
        c2 = [c[1] for c in paths]
        
        for city in c2:
            if city not in c1:
                return city
        