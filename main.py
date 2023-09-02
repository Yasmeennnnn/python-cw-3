favorite_animal =['dog','cat','monkey','rabbit']
print(favorite_animal)
print(f'the second element in the list is {favorite_animal[1]}')
favorite_animal.remove('monkey')
print(favorite_animal)

favorite_animal.append('beard')#['dog','cat','monkey','rabbit']
print(favorite_animal)
for animal in favorite_animal:
    print (f'i love{animal}')

    numbers=[1,2,3,4,5]
    numbers_sum=0
    for number in number :
        numbers_sum=(numbers_sum+number)

        print(numbers_sum)