a = 0
a = ['0','2','','3','0']
b = set([])
vocabSet = set([])
for document in a:
    vocabSet = vocabSet | set(document)
    print(vocabSet)
a=set('boy')
b=set(['y', 'b', 'o','o'])
c=set({"k1":'v1','k2':'v2'})
d={'k1','k2','k2'}
e={('k1', 'k2','k2')}
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
e = e | set('c')
print(e,type(e))