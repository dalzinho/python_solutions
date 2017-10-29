'''
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so
 the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value  for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
 words?
'''




file = open('p042_words.txt').readline()
words = file.split("\",\"")


def calculate_word_value(word):
    return sum([ord(letter) - 96 for letter in word])


def get_max_value():
	longest = 0
	for word in words:
		if len(word) > longest:
			longest = len(word)
	return longest * 26


def get_nth_triangle(n):
	return (n * (n + 1)) / 2


def get_needed_triangles():
	max_needed = get_max_value()
	triangles = []
	n = 1
	while get_nth_triangle(n) <= max_needed:
		triangles.append(get_nth_triangle(n))
		n += 1
	return triangles

def get_answer():
	triangle_words = []
	triangle_numbers = get_needed_triangles()
	for word in words:
		word_value = calculate_word_value(word)
		if word_value in triangle_numbers:
			triangle_words.append(word)
	return len(triangle_words)

print get_answer()