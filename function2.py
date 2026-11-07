def add(x,y,z):
     return x+y+z

def addition(*nums):
    # total = sum(nums)
    total = 0
    for num in nums:
        total = total + num
    return total
def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")



print(addition(9, 10, 11, 12, 133, 15))
print(addition(90, 100))
# sum = add(x=1, y=2, z=3)
# print(sum)

def some_functions(names, *scores, **details):
    print(names)
    print(scores)
    print(details)


some_functions(names="hellen", scores=[90, 100,99], gender = "Female",course="chem")

save(date='2025-01-22', gender ='Female', color='Black',name='Kim')
save(date ='2026-04-02',gender = "Female",color='Pink',name='Sharon')
# data = {"name": "ken", "gender":"Male"}#[1,2,3
# for _, vin in data.items():
#print(vin)

def cylinder(r, h):
    # Volume of a cylinder
    v = 22/7 * r * r * h

    # Surface area of a cylinder
    sa = 22/7 * r**2 * 2 + 22/7 * r * 2 * h

    return sa, v


print(cylinder(8.6, 12.8))
sum([1,2,3])
# lambda functions


# Division using lambda
divider = lambda x, y: x/y

# Area of a circle using lambda
area_circle = lambda r: 22/7 * r * r

# Calling the functions
print(divider(20, 5))
print(area_circle(7))

# TODO functions as a parameter



