dict={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
key=input("Enter a key ")
try:
    x=dict[key]
    print "This key is in the dictionary"

except KeyError or NameError:
    print "This key is not in the dictionary"
