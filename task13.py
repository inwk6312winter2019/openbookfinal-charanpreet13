def lensort(f):
    n = len(f)
    for i in range(n):
        for j in range(i+1,n):
            if len(f[i]) < len(f[j]):
                temp = f[i]
                f[i] = f[j]
                f[j] = temp
    return f


def unique_words(book):
	file1=[]
	for word in book:
		file1.append(word)
	lensort(file1)

fin1=open("Book1.txt","r")
fin2=open("Book2.txt","r")
fin3=open("Book3.txt","r")
print(unique_words(fin1))
print(unique_words(fin2))
print(unique_words(fin3))
