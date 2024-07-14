from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def helper(employees: List['Employee'], id: int):
            graph={}
            vals={}
            for e in employees:
                if e.id not in graph:
                    graph[e.id]=[]
                    graph[e.id].extend(e.subordinates)
                    vals[e.id]=e.importance
            def dfs(node):
                res=0
                for ele in graph[node]:
                    res+=vals[ele]+dfs(ele)
                return res
            return vals[id]+dfs(id)
        return helper(employees,id)
def test_getImportance():
    # Specific test case
    # Employees: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])
    employees = [e1, e2, e3]
    id = 1
    
    solution = Solution()
    result = solution.getImportance(employees, id)
    print("Total importance for employee id", id, ":", result)

# Run the minimal test
test_getImportance()
