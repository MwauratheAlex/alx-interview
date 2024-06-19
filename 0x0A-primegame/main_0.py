#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
x = 3
nums = [4, 5, 1]
print("Winner: {}".format(isWinner(x, nums)))
# print(isWinner(1, [1]), "BEN")  # Expected output: Ben
# print(isWinner(4, [2, 3, 4, 5]), "MARIA")  # Expected output: Maria
# print(isWinner(3, [7, 7, 7]), "None")  # Expected output: None
# print(isWinner(5, [1, 2, 3, 4, 5]), "MARIA")  # Expected output: Maria
# print(isWinner(3, [11, 13, 17]), "MARIA")  # Expected output: Maria
# print(isWinner(4, [6, 7, 8, 9]), "BEN")  # Expected output: Ben
# # Expected output: Maria or Ben (depends on optimal play analysis)
# print(isWinner(2, [100, 200]))
