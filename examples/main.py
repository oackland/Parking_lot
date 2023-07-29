import app


def add_numbers (x, y):
	result = x + y
	return result


app.print_ascii_art (app.text_to_convert)

# Call the function and store the result in a variable
sum_result = add_numbers (4, 7)

print ()
print (f' this is the sum', sum_result)
