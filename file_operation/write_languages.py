languages=["python","java","javascript","c#","c++"]

fw=open("file_operation\\languages.txt","w")

for l in languages:

    fw.write(l+"\n")

print("write completed........")