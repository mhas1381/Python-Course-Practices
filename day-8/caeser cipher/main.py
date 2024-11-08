alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("'decode' or 'encode':\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text , shift):
    encrypted_message = []
    for position in range(len(text)):
        new_char = text[position]
        encrypted_message.append(new_char)
    print(encrypted_message)

encrypt(text = text , shift = shift)