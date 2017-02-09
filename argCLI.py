import sys

print(sys.argv[1],":",sys.argv[2])
i=0
for mot in sys.argv:
	i+=1
	print(i," : ",mot)


