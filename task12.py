def unique_words(book):
	file1=[]
	count=0
	d={}
	for word in book:
		file1.append(word)		
	
	for words in file1:
		if words not in d:
			d[words]=1
		else:
			d[words]=d[words]+1
	print(d)
	for key in d.items():
		count=count+1
	return count






fin1=open("Book1.txt","r")
fin2=open("Book2.txt","r")
fin3=open("Book3.txt","r")
print(unique_words(fin1))
print(unique_words(fin2))
print(unique_words(fin3))
