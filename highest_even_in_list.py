def highest_even(li):
    even=[]
    for item in li:
        if item %2 == 0:
            even.append(item)
    return max(even)
print(highest_even([1,2,3,56,3,6,7]));
