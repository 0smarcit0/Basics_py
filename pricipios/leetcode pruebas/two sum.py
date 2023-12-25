

lista =[]

nums=[1,2]
target=3
for i in range(len(nums)):
            
    if nums[i] + nums[i]+1 == target:
                
        lista.append(nums.index(i))
        lista.append(nums.index(i))
        

print(lista)
                
                


