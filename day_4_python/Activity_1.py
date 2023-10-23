unsorted = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
sorted_grades = sorted(unsorted, key = lambda x: x[1])
print(sorted_grades)



cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2]))

even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

nums = [i for i in range(1,101)]
print(nums)

sent = "the quick brown fox jumps over the fence."
print({word:len(word) for word in sent.split()})