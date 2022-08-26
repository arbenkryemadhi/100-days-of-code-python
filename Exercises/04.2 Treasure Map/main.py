row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

print("Welcome to Treasure Map. Made by Arben KRYEMADHI!")
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

vertical_num = int(position[0])
horizontal_num = int(position[1])

map[horizontal_num - 1][vertical_num - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
