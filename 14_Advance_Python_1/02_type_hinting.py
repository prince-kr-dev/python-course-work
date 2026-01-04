#Type Hinting / Type annotation
'''
num : int = 45
name : str = "Prince"


def sum(a:int, b:int) -> int:
    return a + b

print(sum(23,43))
'''



from typing import List, Tuple, Dict

numbers:List[int] = [12,34,64,32]
print(numbers)


person: Tuple[str, int, float] = ("Prince", 23, 72.5)
print(person)



marks: Dict[str, int] = {
    "math": 90,
    "science": 85,
    "english": 88
}

print(marks)