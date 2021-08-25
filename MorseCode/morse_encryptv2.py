# import time

# start = time.perf_counter()


def encode_morse(txt):
    word = list(txt)
    alphabet = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": " ",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
    clear_message = []
    for i in range(0, len(word)):
        for key in alphabet:
            if word[i] == key:
                clear_message.append(alphabet[key])
    return clear_message


text_m = input("Podaj wiadomość do zaszyfrowania, napisz ją wielkimi literami: ")

for item in encode_morse(text_m):
    print(item, end=" ")

# for key in a:
#     print(key, " ", a[key])
# end = time.perf_counter()

# print("Wydajnosc: ", end - start)
© 2021 GitHub, Inc.
