def squares(n):
	
    square_list = []
    
    for i in range(1,n+1):
        square_list.append(2 ** i)
    
    return square_list




putere_maxim = input("Enter a number: ")

print(squares(int(putere_maxim)));