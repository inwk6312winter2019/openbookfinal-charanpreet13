import collections
import fileinput

def unique_words():
  
	fin1=open("Book1.txt","r")
	fin2=open("Book2.txt","r")
	fin3=open("Book3.txt","r")
	file1=[]
	file2=[]
	file3=[]
	d1={}
	d2={}
	d3={}
	for word in fin1:
		file1.append(word)
	
	for i in file1:
	
		if i not in d1:
			d1[i]=1
		else:
			d1[i]=d1[i]+1



	for word in fin2:
		file2.append(word)
	for i in file2:
	
		if i not in d2:
			d2[i]=1
		else:
			d2[i]=d2[i]+1

  

	for word in fin2:
		file3.append(word)
	
	for i in file3:
	
		if i not in d3:
			d3[i]=1
		else:
			d3[i]=d3[i]+1

	find_most_common_words(d1)
	find_most_common_words(d2)
	find_most_common_words(d3)
	
	





def find_most_common_words(d1,top=20):
	words = collections.Counter()
	for line in d1:
		words.update(line.lower().split())
	return words.most_common(top)


unique_words()
