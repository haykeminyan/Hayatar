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


	for index, _ in enumerate(wordChars[:-1]):
		logger.error(wordChars[index])
		if wordChars[index] == 'T' and wordChars[index+1] == '’':
			wordChars[index] = 'Թ'
			wordChars[index+1] = ''

		elif (wordChars[index] == 't' and wordChars[index+1] == 'z' and wordChars[index+2]=='’'):
			wordChars[index] = 'ծ'
			wordChars[index + 1] = ''
			wordChars[index+2] = ''

		elif (wordChars[index] == "T" and wordChars[index+1] != 's'):  # 9
			wordChars[index] = "Թ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == 'T' and wordChars[index+1] == 's'):
			wordChars[index] = 'Ծ'
			wordChars[index + 1] = ''

		elif (wordChars[index] == 'z' and wordChars[index+1] == '’'):
			wordChars[index] = 'ծ'
			wordChars[index + 1] = ''

		elif (wordChars[index] == 'Z' and wordChars[index+1] == '’'):
			wordChars[index] = 'Ծ'
			wordChars[index + 1] = ''

		elif (wordChars[index] == 't' and wordChars[index+1] == 'z'):
			wordChars[index] = 'ծ'
			wordChars[index + 1] = ''

		elif (wordChars[index] == 'T' and wordChars[index+1] == 'z'):
			wordChars[index] = 'Ծ'
			wordChars[index + 1] = ''

		elif wordChars[index] == 'R' and wordChars[index+1] == '’':
			wordChars[index] = 'Ր'
			wordChars[index+1] = ''

		elif wordChars[index] == 'r' and wordChars[index+1] == '’':
			wordChars[index] = 'ր'
			wordChars[index+1] = ''

		elif wordChars[index] == 'O' and wordChars[index+1] == 'o':
			wordChars[index] = 'Ու'
			wordChars[index+1] = ''

		elif wordChars[index] == 'G' and wordChars[index+1] == 'h':
			wordChars[index] = 'Ղ'
			wordChars[index+1] = ''

		elif wordChars[index] == 'G' and wordChars[index+1] == 'h':
			wordChars[index] = 'ղ'
			wordChars[index+1] = ''

		elif wordChars[index] == 'o' and wordChars[index+1] == 'o':
			wordChars[index] = 'ու'
			wordChars[index+1] = ''

		elif wordChars[index] == 't' and wordChars[index+1] == '’':
			wordChars[index] = 'թ'
			wordChars[index+1] = ''

		elif (wordChars[index] == "t" and wordChars[index+1] == 's'):  # 14
			wordChars[index] = "ծ"
			wordChars[index+1] = ''

		elif wordChars[index] == 't':
			wordChars[index] = 'տ'

		elif wordChars[index] == 'r':
			wordChars[index] = 'ռ'

		elif wordChars[index] == 'R':
			wordChars[index] = 'Ռ'

		elif wordChars[index] == 'T':
			wordChars[index] = 'S'

		elif wordChars[index] == 'Y':
			wordChars[index] = 'Յ'

		elif wordChars[index] == 'y':
			wordChars[index] = 'յ'

		elif wordChars[index] == 'Z' and wordChars[index+1] == 'H':
			wordChars[index] = 'Ժ'
			wordChars[index+1] = ''

		elif wordChars[index] == 'z' and wordChars[index+1] == 'h':
			wordChars[index] = 'ժ'
			wordChars[index+1] = ''

		elif wordChars[index] == 'Z' and wordChars[index+1] == 'h':
			wordChars[index] = 'Ժ'
			wordChars[index+1] = ''

		elif wordChars[index] == '@':
			wordChars[index] = 'ը'


		elif wordChars[index] == 'k' and wordChars[index+1] == 'h':
			wordChars[index] = 'խ'
			wordChars[index+1] = ''


		elif (wordChars[index] == "d" and wordChars[index+1] == 'z'):  # 17
			wordChars[index] = "ձ"
			wordChars[index+1] = ''

		elif (wordChars[index] == "g" and wordChars[index+1] == 'h'):  # 18
			wordChars[index] = "ղ"
			wordChars[index+1] = ''

		elif (wordChars[index] == "s" and wordChars[index+1] =='h'):  # 24
			wordChars[index] = "շ"
			wordChars[index+1] = ''

		elif (wordChars[index] == "c" and wordChars[index+1] =='h'):  # 26
			wordChars[index] = "չ"
			wordChars[index+1] = ''

		elif (wordChars[index] == "e" and wordChars[index+1] =='v'):  # 38
			wordChars[index] = "և"
			wordChars[index + 1] = ''


		elif (wordChars[index] == "s" and wordChars[index+1] != 't'):  # 30
			wordChars[index] = "ս"
			wordChars[index + 1] = ''

		elif ((wordChars[index] == "v" and wordChars[index+1] =='o')):  # 25
			wordChars[index] = "ո"
			wordChars[index + 1] = ''


		elif (wordChars[index] == "L" and wordChars[index+1] == 'L'):  # 12
			wordChars[index] = "Լ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == "K" and wordChars[index+1] == 'h'):  # 13
			wordChars[index] = "Խ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == "D" and wordChars[index+1] == 'z'):  # 17
			wordChars[index] = "Ձ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == "G" and wordChars[index+1] == 'h'):  # 18
			wordChars[index] = "Ղ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == "S" and wordChars[index+1] =='h'):  # 24
			wordChars[index] = "Շ"
			wordChars[index + 1] = ''

		elif (wordChars[index] == "C" and wordChars[index+1] =='h'):  # 19
			wordChars[index] = "Ճ"
			wordChars[index + 1] = ''

		elif (wordChars[index+1] == "S" and wordChars[index] != 'T'):  # 30
			wordChars[index] = "Ս"
			wordChars[index + 1] = ''

	wordChars = [i for i in wordChars if i]

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

		elif (lst[i] == "u"):  # 35
			lst[i] = "ո"

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