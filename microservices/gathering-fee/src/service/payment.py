from typing import List
from service.people import People

class Payments:
    def __init__(self, people: People) -> None:
        self.value: List[list] = self.cal(people)
        
    def cal(self, people: People):
        input: dict = people.get_net_flow_dict()
        res = []
        while input:
            max_person = max(input, key=input.get)
            min_person = min(input, key=input.get)
            
            remain = input[max_person] + input[min_person]
            if remain > 0: # min have paid all, but max not receive enough
                input[max_person] = remain
                res.append([min_person, abs(input[min_person]), max_person])
                del input[min_person]
            elif remain < 0: 
                input[min_person] = remain
                res.append([min_person, abs(input[max_person]), max_person])
                del input[max_person]
            else:
                res.append([min_person, abs(input[max_person]), max_person])
                del input[max_person]
                del input[min_person]
        
        return res
        
        