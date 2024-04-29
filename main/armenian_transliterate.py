import logging


logger = logging.getLogger(__name__)

def armenian_latinisation(prompt):
	# For example, you can use Flask to create a route that accepts POST requests with user input

	lst = []
	text = prompt
	wordChars = list(text)

	logger.info(wordChars)

	if wordChars[0] == 'o' and wordChars[1] == 'd' and len(wordChars) == 2:
		wordChars = ['օդ']

	elif wordChars[0] == 'k' and wordChars[1] == 'h':
		wordChars[0] = 'խ'
		del wordChars[1]

	elif (wordChars[0] == "t" and wordChars[1] == 's'):  # 14
		wordChars[0] = "ծ"
		del wordChars[1]

	elif (wordChars[0] == "d" and wordChars[1] == 'z'):  # 17
		wordChars[0] = "ձ"
		del wordChars[1]

	elif (wordChars[0] == "g" and wordChars[1] == 'h'):  # 18
		wordChars[0] = "ղ"
		del wordChars[1]

	elif (wordChars[0] == "s" and wordChars[1] =='h'):  # 24
		wordChars[0] = "շ"
		del wordChars[1]

	elif (wordChars[0] == "c" and wordChars[1] =='h'):  # 26
		wordChars[0] = "չ"
		del wordChars[1]

	elif (wordChars[0] == "e" and wordChars[1] =='v'):  # 38
		wordChars[0] = "և"
		del wordChars[1]

	elif (wordChars[0] == "s" and wordChars[1] != 't'):  # 30
		wordChars[0] = "ս"
		del wordChars[1]

	elif ((wordChars[0] == "v" and wordChars[1] =='o')):  # 25
		wordChars[0] = "ո"
		del wordChars[1]

	elif (wordChars[0] == "T" and wordChars[1] != 's'):  # 9
		wordChars[0] = "Թ"
		del wordChars[1]

	elif (wordChars[0] == 'T' and wordChars[1] == 's'):
		wordChars[0] = 'Ծ'
		del wordChars[1]

	elif (wordChars[0] == "L" and wordChars[1] == 'L'):  # 12
		wordChars[0] = "Լ"
		del wordChars[1]

	elif (wordChars[0] == "K" and wordChars[1] == 'h'):  # 13
		wordChars[0] = "Խ"
		del wordChars[1]

	elif (wordChars[0] == "D" and wordChars[1] == 'z'):  # 17
		wordChars[0] = "Ձ"
		del wordChars[1]

	elif (wordChars[0] == "G" and wordChars[1] == 'h'):  # 18
		wordChars[0] = "Ղ"
		del wordChars[1]

	elif (wordChars[0] == "S" and wordChars[1] =='h'):  # 24
		wordChars[0] = "Շ"
		del wordChars[1]

	elif (wordChars[0] == "C" and wordChars[1] =='h'):  # 19
		wordChars[0] = "Ճ"
		del wordChars[1]

	elif (wordChars[1] == "S" and wordChars[0] != 'T'):  # 30
		wordChars[0] = "Ս"
		del wordChars[1]

	for i in range(len(wordChars)):  # Making an array using the string.

		lst.append(wordChars[i])

	for i in range(len(wordChars)):  # Finding and changing the letters in the array.
		logger.error(wordChars[i])

		# Lower case letters here.

		if (lst[i] == "a"):  # 1
			lst[i] = "ա"

		elif (lst[i] == "b"):  # 2
			lst[i] = "բ"

		elif (lst[i] == "g"):  # 3
			lst[i] = "գ"

		elif (lst[i] == "d"):  # 4
			lst[i] = "դ"

		elif (lst[i] == "e"):  # 5
			lst[i] = "ե"

		elif (lst[i] == "z"):  # 6
			lst[i] = "զ"

		elif (lst[i] == "e"):  # 7
			lst[i] = "է"

		elif (lst[i] == "y"):  # 8
			lst[i] = "ը"

		elif (lst[i] == 'o'):
			lst[i] = 'ո'

		elif (lst[i] == "t"):  # 9
			lst[i] = "թ"

		elif (lst[i] == "j"):  # 10
			lst[i] = "ժ"

		elif (lst[i] == "i"):  # 11
			lst[i] = "ի"

		elif (lst[i] == "l"):  # 12
			lst[i] = "լ"


		elif (lst[i] == "k"):  # 15
			lst[i] = "կ"

		elif (lst[i] == "h"):  # 16
			lst[i] = "հ"


		elif (lst[i] == "m"):  # 21
			lst[i] = "մ"

		elif (lst[i] == "y"):  # 22
			lst[i] = "յ"

		elif (lst[i] == "n"):  # 23
			lst[i] = "ն"

		elif (lst[i] == "u" and lst[i + 1] == ""):  # 35
			lst[i] = "ո"
			lst[i + 1] = "ւ"


		elif (lst[i] == "p"):  # 27
			lst[i] = "պ"

		elif (lst[i] == "j"):  # 28
			lst[i] = "ջ"

		elif (lst[i] == "r"):  # 29
			lst[i] = "ռ"

		elif (lst[i] == "v"):  # 31
			lst[i] = "վ"

		elif (lst[i] == "t"):  # 32
			lst[i] = "տ"

		elif (lst[i] == "r"):  # 33
			lst[i] = "ր"

		elif (lst[i] == "c"):  # 34
			lst[i] = "ց"

		elif (lst[i] == "p"):  # 36
			lst[i] = "փ"

		elif (lst[i] == "q"):  # 37
			lst[i] = "ք"


		elif (lst[i] == "f"):  # 40
			lst[i] = "ֆ"

		# Higher case letters here.

		elif (lst[i] == "A"):  # 1
			lst[i] = "Ա"

		elif (lst[i] == "B"):  # 2
			lst[i] = "Բ"

		elif (lst[i] == "G"):  # 3
			lst[i] = "Գ"

		elif (lst[i] == "D"):  # 4
			lst[i] = "Դ"

		elif (lst[i] == "E"):  # 5
			lst[i] = "Ե"

		elif (lst[i] == "Z"):  # 6
			lst[i] = "Զ"

		elif (lst[i] == "E"):  # 7
			lst[i] = "Է"

		elif (lst[i] == "Y"):  # 8
			lst[i] = "Ը"

		elif (lst[i] == "J"):  # 10
			lst[i] = "Ժ"

		elif (lst[i] == "I"):  # 11
			lst[i] = "Ի"

		elif (lst[i] == "K"):  # 15
			lst[i] = "Կ"

		elif (lst[i] == "H"):  # 16
			lst[i] = "Հ"

		elif (lst[i] == "M"):  # 21
			lst[i] = "Մ"

		elif (lst[i] == "Y"):  # 22
			lst[i] = "Յ"

		elif (lst[i] == "N"):  # 23
			lst[i] = "Ն"


		elif (lst[i] == "Vo"):  # 25
			if (i == 0 or lst[i - 1] == " "):
				lst[i] = "Ո"
			else:
				lst[i] = "O"

		elif (lst[i] == "P"):  # 27
			lst[i] = "Պ"

		elif (lst[i] == "J"):  # 28
			lst[i] = "Ջ"

		elif (lst[i] == "R"):  # 29
			lst[i] = "Ռ"

		elif (lst[i] == "V"):  # 31
			lst[i] = "Վ"

		elif (lst[i] == "T"):  # 32
			lst[i] = "Տ"

		elif (lst[i] == "R"):  # 33
			lst[i] = "Ր"

		elif (lst[i] == "C"):  # 34
			lst[i] = "Ց"

		elif (lst[i] == "P"):  # 36
			lst[i] = "Փ"

		elif (lst[i] == "Q"):  # 37
			lst[i] = "Ք"

		elif (lst[i] == "O"):  # 39
			lst[i] = "Օ"

		elif (lst[i] == "F"):  # 40
			lst[i] = "Ֆ"

	listtostring = ''.join([str(elem) for i, elem in enumerate(lst)])  # Back to a string form.

	# Return the user's input as a string
	return listtostring