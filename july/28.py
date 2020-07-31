"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
    from collections import Counter
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if tasks is None or len(tasks) == 0:
            return None
        if n == 0:
            return len(tasks) 
        
        count_set = Counter(tasks)
        tasks_dict = dict(count_set)
        most_common_task = count_set.most_common(1)[0] if count_set else None
        
        if most_common_task is None:
            return len(tasks)
        
        num_most_common = most_common_task[1]-1
        idle_units = num_most_common * n
        tasks_dict.pop(most_common_task[0])
        
        for key, value in tasks_dict.items():
            idle_units -= min(value, num_most_common)
            
        if idle_units < 0:
            return len(tasks)
        
        return len(tasks) + idle_units
