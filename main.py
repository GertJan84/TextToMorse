MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}


def encode(message):
    message_list_uppercase = [message[letter].upper() for letter in range(len(message))]
    encoded_message = [MORSE_CODE_DICT[message_list_uppercase[run]] for run in range(len(message_list_uppercase))]

    output = ""
    for run in range(len(encoded_message)):
        output += f"{encoded_message[run]} "

    return output


def decode(message):
    encoded_message = message.split(" ")

    decoded_message = []
    for run in range(len(encoded_message)):
        for (key, value) in MORSE_CODE_DICT.items():
            if value == encoded_message[run]:
                decoded_message.append(key)

    output = ""
    for run in range(len(decoded_message)):
        output += decoded_message[run]

    return output.lower()


choice = input("Do you want to encode or decode a message: ").lower()

if choice == 'decode':
    message = input(f'What message do you want to {choice}: ')
    print(decode(message))
elif choice == 'encode':
    message = input(f'What message do you want to {choice}: ')
    print(encode(message))
else:
    print(f'"{choice}" is not one of the options')

