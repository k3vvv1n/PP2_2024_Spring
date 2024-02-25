import re

def test(pattern, sub, testData, testNumber, expectedResult):
    result = re.sub(pattern, sub, testData)
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")
        
pattern = r"[\s,\.]"
sub = r":"

test(pattern, sub, "Saken Bekon", "test1", "Saken:Bekon")
test(pattern, sub, " arsen, flllfe  aaa", "test2", ":arsen::flllfe::aaa")
test(pattern, sub, "+771 065 75 06, ", "test3", "+771::065:75:06::")