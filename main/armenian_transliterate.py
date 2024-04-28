import logging


logger = logging.getLogger(__name__)

def armenian_latinisation(prompt):
	# For example, you can use Flask to create a route that accepts POST requests with user input

	lst = []
	text = prompt
	wordChars = list(text)

	for i in range(len(wordChars)):  # Making an array using the string.

		lst.append(wordChars[i])


	for i in range(len(wordChars)):  # Finding and changing the letters in the array.


		if (lst[i] == "o" and lst[i+1] == 'd'):  # 39
			lst[i] = "օ"
		# Lower case letters here.

		elif (lst[i] == "a"):  # 1
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

		elif (lst[i] == "t"):  # 9
			lst[i] = "թ"

		elif (lst[i] == "j"):  # 10
			lst[i] = "ժ"

		elif (lst[i] == "i"):  # 11
			lst[i] = "ի"

		elif (lst[i] == "l"):  # 12
			lst[i] = "լ"

		elif (lst[i] == "kh"):  # 13
			lst[i] = "խ"

		elif (lst[i] == "ts"):  # 14
			lst[i] = "ծ"

		elif (lst[i] == "k"):  # 15
			lst[i] = "կ"

		elif (lst[i] == "h"):  # 16
			lst[i] = "հ"

		elif (lst[i] == "dz"):  # 17
			lst[i] = "ձ"

		elif (lst[i] == "gh"):  # 18
			lst[i] = "ղ"

		elif (lst[i] == "ch"):  # 19
			lst[i] = "ճ"

		elif (lst[i] == "m"):  # 21
			lst[i] = "մ"

		elif (lst[i] == "y"):  # 22
			lst[i] = "յ"

		elif (lst[i] == "n"):  # 23
			lst[i] = "ն"

		elif (lst[i] == "sh"):  # 24
			lst[i] = "շ"

		elif (lst[i] == "u" and lst[i + 1] == ""):  # 35
			lst[i] = "ո"
			lst[i + 1] = "ւ"

		elif (lst[i] == "vo" or lst[i] == 'o'):  # 25
			lst[i] = "ո"

		elif (lst[i] == "ch"):  # 26
			lst[i] = "չ"

		elif (lst[i] == "p"):  # 27
			lst[i] = "պ"

		elif (lst[i] == "j"):  # 28
			lst[i] = "ջ"

		elif (lst[i] == "r"):  # 29
			lst[i] = "ռ"

		elif (lst[i] == "s" and lst[i-1]!='t'):  # 30
			lst[i] = "ս"

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

		elif (lst[i] == "ev"):  # 38
			lst[i] = "և"

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

		elif (lst[i] == "T" and lst[i+1] != 's'):  # 9
			lst[i] = "Թ"

		elif (lst[i] == 'T' and lst[i+1] == 's'):
			lst[i] = 'Ծ'

		elif (lst[i] == "J"):  # 10
			lst[i] = "Ժ"

		elif (lst[i] == "I"):  # 11
			lst[i] = "Ի"

		elif (lst[i] == "L" and lst[i+1] == 'L'):  # 12
			lst[i] = "Լ"

		elif (lst[i] == "K" and lst[i+1] == 'h'):  # 13
			lst[i] = "Խ"

		elif (lst[i] == "K"):  # 15
			lst[i] = "Կ"

		elif (lst[i] == "H"):  # 16
			lst[i] = "Հ"

		elif (lst[i] == "D" and lst[i+1] =='z'):  # 17
			lst[i] = "Ձ"

		elif (lst[i] == "G" and lst[i+1]=='h'):  # 18
			lst[i] = "Ղ"

		elif (lst[i] == "Ch"):  # 19
			lst[i] = "Ճ"

		elif (lst[i] == "M"):  # 21
			lst[i] = "Մ"

		elif (lst[i] == "Y"):  # 22
			lst[i] = "Յ"

		elif (lst[i] == "N"):  # 23
			lst[i] = "Ն"

		elif (lst[i] == "Sh"):  # 24
			lst[i] = "Շ"

		elif (lst[i] == "Vo"):  # 25
			if (i == 0 or lst[i - 1] == " "):
				lst[i] = "Ո"
			else:
				lst[i] = "O"

		elif (lst[i] == "Ch"):  # 26
			lst[i] = "Չ"

		elif (lst[i] == "P"):  # 27
			lst[i] = "Պ"

		elif (lst[i] == "J"):  # 28
			lst[i] = "Ջ"

		elif (lst[i] == "R"):  # 29
			lst[i] = "Ռ"

		elif (lst[i] == "S" and lst[i-1]!='T'):  # 30
			lst[i] = "Ս"

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