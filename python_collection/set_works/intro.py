st={}
print(type(st)) #class dictionary

st={10,20,30,20,30,40} #unordered,duplictes not allowed,can modify,indexing not supported
print(type(st))
print(st)

#methods
st.add(100) #add value to set
print(st)

set_a={10,20,30,40}
set_b={10,20,100,300,400}

union_set=set_a.union(set_b)   #union
print("union set=",union_set)

intersection_set=set_a.intersection(set_b)  #intersection
print("intersection set=",intersection_set)

diff_set=set_a.difference(set_b)   #difference
print("difference set=",diff_set)

set_1={10,20,30,40,50}
set_2={10,40,20}

print(set_1.issuperset(set_2))   #issuperset
print(set_2.issubset(set_1))     #issubset

note="hene"
magazine="chicken"                 
print(set(note).issubset(magazine))

