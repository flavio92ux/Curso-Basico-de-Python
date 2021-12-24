nums = [1, 2, 3]
print(type(nums))

nums.append(3)
nums.append(4)
nums.append(500)
print(len(nums))

nums[3] = 100 #substitui o elemento de indice 3 (quarto elemento) para 100
nums.insert(0, -200) #insere -200 no indice 0 deslocando sem substituir

print(nums[-1]) #pega o ultimo elemento

print(nums)