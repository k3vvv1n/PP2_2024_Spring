def grams_to_ounces(grams):
    ounces = 0.03527396 * grams
    return ounces

grams = int(input())
print("in ounces =", grams_to_ounces(grams))
