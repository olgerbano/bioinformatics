word = input("enter word: ")

ascii_list = [];
suma = 0;
for i in range(len(word)):
	ascii_list.append(ord(word[i]));
	suma+= ord(word[i]);
print(ascii_list);
print(suma);
