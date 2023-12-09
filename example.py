def sum_before():
    return 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

#リファクタリング後
def sum_after():
	result = 0
	for i in range(1, 11):
		result += i
	return result

print(sum_before())

print(sum_after())