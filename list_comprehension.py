lc_letters = ["a", "b", "c", "d", "e"]
uc_letters = [x.upper() for x in lc_letters]
print(lc_letters)
print(uc_letters)

ages = [1, 34, 5, 7, 3, 57, 356]
print(ages)

old_ages = [x for x in ages if x > 10]
print(old_ages)
