def unique_words(book):
	file1=[]
	count=0
	d={}
	for word in book:
		word=word.strip()
		word=word.split()
		
	
	for words in word:	
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
