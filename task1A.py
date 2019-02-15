def unique_words(book):
	file1=[]
	for word in book:
		word=word.strip()
		word=word.split()
		print(word)
	d={}
	for i in word:
	
		if i not in d:
			d[i]=1
		else:
			d[i]=d[i]+1
	
	for key,value in d.items():
		if value==1:
			print(key)
		else:
			pass
	return d






fin1=open("Book1.txt","r")
fin2=open("Book2.txt","r")
fin3=open("Book3.txt","r")
print(unique_words(fin1))
print(unique_words(fin2))
print(unique_words(fin3))
