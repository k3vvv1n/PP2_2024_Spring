def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]==3:
            print("True")
            return 0
    print("False")

nums=list(map(int, input().split()))
has_33(nums)