try:

    fr=open("error_handling\\eywords.txt")

    for line in fr:
        print(line)

except Exception as e:
    print(e)

finally:
    print("db commit")   #clean up processing