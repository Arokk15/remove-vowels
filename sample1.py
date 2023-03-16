A="I love you"
A=A.lower()
print(A)
vowels=["a","e","i","o","u"]
sample=[]
sample.extend(A)

for i in range(len(sample)):
    for j in range(len(vowels)):
        if sample[i]==vowels[j]:
            print(sample[i])
            del(sample[i])


print(sample)

            

