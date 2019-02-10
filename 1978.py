N = int(input())
nums = input().split()
count = 0
for i in range(N): 
    j = 2        
    while int(nums[i]) >= j :
         if int(nums[i]) % j == 0 and int(nums[i]) != j:
             break
         elif int(nums[i]) % j == 0 and int(nums[i]) == j:
            count += 1
            break
         else : 
             j += 1

         if int(nums[i]) < j :
             break
print(count)
