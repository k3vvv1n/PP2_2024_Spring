import re


def replace(match):
    return f"{match.group().lower()[0]}_{match.group().upper()[1]}"

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, replace, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")

pattern = r".[A-Z]"

test(pattern, "SakenBekon", "test1" ,"Saken_Bekon")
test(pattern, "arsenMriaz", "test2", "arsen_Mriaz")
test(pattern, "_____2$&$Tima_a4_top, ", "test3", "2$&$TimaA4top")




