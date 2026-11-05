#store lots data
#data structures
#list,sets,tuples,dictionary
people = ["jack", "Jnae" ,"Hussein", "Marium"]
scores = [87,45, 53, 91, 29, 55, 71, 81]
print(people[0])
print(people[-1])
people.append("Sharon")
print(people)
scores.append(44)
print(scores)
people.sort()
print(people)
scores.sort(reverse=True)
print(scores)
print(sum(scores))
print(sum(scores) //len(scores))
scores.sort()
# slicing
print(scores)
print(scores[-2:])
print(scores[:2])
print(scores[0:3])

# set it removes duplicates
numbers = {87, 67, 88,90, 44}
print(numbers)
# tuple() immutable data data that cant be changed by coding
days = {"monday", "Tuesday", "Friday"}
# dictionary
# has key and value
person1 = {"name": "Sharon", "City": "Marsabit", "Age": 19}
print(person1)
# data structures and algorihms
print(sum(numbers))
watu = [{"name": "Sila", "Age": 22},
        {"name": "Hin", "Age":44},
        {"name": "Cila", "Age":19}
        ]
print(watu[1]["name"])
