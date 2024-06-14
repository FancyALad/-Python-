studentid={}
studentscore={}
course=set()
while True:
    a=input()
    if a=='END':
        break
    words=a.split()
    if words[-1].isnumeric():
        score=studentscore.get(words[0])
        if score==None:
            score={}
        score[words[1]]=words[2]
        studentscore[words[0]]=score
        course.add(words[1])
    else:
        studentid[words[0]]=' '.join(words[1:])
#print(studentid,studentscore)#测试
print('学号,姓名',end='')
coursename=list(course)
for name in coursename:
    print(','+name,end='')
print(',平均分')
stdid=list(studentid.keys())
stdid.sort()
#print(stdid)#测试
for i in stdid:
    sum=0;cnt=0
    print(i+','+studentid[i],end='')
    score=studentscore[i]
    for name in coursename:
        if score[name]:
            print(','+score[name],end='')
            cnt+=1
            sum+=int(score[name])
    print(','+str(sum/cnt))


'''
3180102346 张三
3180102346 Python 80
3180102346 OOP 80
3180102346 军事学 80
3180102346 微积分 80
3180102345 John Hoppkings
3180102345 Python 78
3180102345 OOP 82
3180102345 军事学 90
3180102345 微积分 83
END
'''#测试用例
