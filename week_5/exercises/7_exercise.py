import re

def repl_func(match):
    return match.group()[1].upper()

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, repl_func, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")

pattern = r'_.'

test(pattern, "Saken_bekon", "test1" ,"SakenBekon")
test(pattern, "arsen_mriaz", "test2", "arsenMriaz")
test(pattern, "_____2$&$Tima_a4_top, ", "test3", "2$&$TimaA4top")



