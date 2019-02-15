log=open('access.log','r')
logget=open('get.log','a')
logput=open('put.log','a')
logpost=open('post.log','a')
logdelete=open('delete.log','a')
for line in log:
        line=line.strip()
        if 'get '.upper() in line.upper():
                logget.write(line)
        elif 'post '.upper() in line.upper():
                logpost.write(line)
        elif 'PUT '.upper() in line.upper():
                logput.write(line)
        elif 'delete '.upper() in line.upper():
                logdelete.write(line)


