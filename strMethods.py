#Some string methods
#Returns the string with both leading and trailing whitespaces removed
str1 = "              Hello                "
print("String \"" + str1 + "\" after strip: " + str1.strip())

#Returns a string with first character capitalized
str2 = "hello world"
print("String \"" + str2 + "\" after capitalize: " + str2.capitalize())

#Returs a title cased string
str3 = "hello world"
print("String \"" + str3 + "\" after title: " + str3.title())

#Splits the string
str4 = "Hello World"
fword, lword = str4.split(" ")
print("The split strings are " + fword + " and " + lword) 