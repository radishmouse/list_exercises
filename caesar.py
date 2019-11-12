alphabet = list("abcdefghijklmnopqrstuvwxyz")
rotate_by = 13

sentence = "lbh zhfg hayrnea jung lbh unir yrnearq"

# letter = "a"
result = ""
for letter in sentence:
    # find the position of "a" in the list
    # then add 13 to it
    try:
        position = alphabet.index(letter)
        new_position = (position + rotate_by) % 26
        new_letter = alphabet[new_position]
        # print(new_letter)
        result += new_letter
    except ValueError:
        # print(letter)
        result += letter
print(result)
