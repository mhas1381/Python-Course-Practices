alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
app_run = True


def caesar(plain_text, shift_amount, cipher_direction):
    cipher = []
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter not in alphabet:
            cipher.append(letter)
        else:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher.append(alphabet[new_position])
    print(f"The {cipher_direction}d code is : {"".join(cipher)}")


while app_run:
    direction = input("'encode' or 'decode':\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    user_choice = input("Do you want to use again? Y/N\n").lower()
    if user_choice == "n":
        print("Good bye")
        app_run = False
