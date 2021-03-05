# print('Hello World')
# # this will return Hello World in the console like our first lesson
#
# # We can also simply use the following:
# print('Hello World')
# # The console will return 'Hello World' to us. The same will go for the following:
# print("Hello World")
#
# # Problems: Sentences with 's, 're can mess that up
# print('He's a good guy')
# # This brings out a Syntax error. To get past this, you need to use a \
# print('He\'s a good guy')
# \ tells python that 's is part of the sentence, not the end of the string
# This can be got around as well by using "" vs ''


# String Formatting
# method that allows you to embed strings with non-stings and alows you to display data in the ways you want
numbers = [4, 5, 6]
strings = "Numbers:{0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
# To assign a string to the three numbers you do "Sting:{Index}{index} etc.format() to assign it to such
#.format(list[index])
print(strings)
# Our consol will show "Numbers: 4,5,6

a = "{x}/{y}".format(x=100, y=300)
print(a)


# String Functions