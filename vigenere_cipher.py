#Written by Elvin Latifi

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_nums = list(zip(alphabet, list(range(1, 27))))

def encode(message, key):
    num_list = list(range(1, len(key)+1))
    key_chars = [char for char in key]
    num_key_pairs = list(zip(num_list, key_chars))
    i = 0
    lim = len(key) - 1
    key_places = []
    for char in key_chars:
        for pair in alphabet_nums:
            if char == pair[0]:
                key_places.append(pair[1]-1)
    encoded_message = ""
    for char in message:
        found = False
        for pair in alphabet_nums:
            if char == pair[0]:
                found = True
                char_num = pair[1] + key_places[i]      
                if char_num > 26:
                    char_num = char_num - 26
                for pair in alphabet_nums:
                    if char_num == pair[1]:
                        encoded_message += pair[0]
        if found == False:
            encoded_message += char
            continue
        i += 1
        if i > lim:
            i = 0
    return encoded_message

def decode(message, key):
    num_list = list(range(1, len(key)+1))
    key_chars = [char for char in key]
    num_key_pairs = list(zip(num_list, key_chars))
    i = 0
    lim = len(key) - 1
    key_places = []
    for char in key_chars:
        for pair in alphabet_nums:
            if char == pair[0]:
                key_places.append(pair[1]-1)
    decoded_message = ""
    for char in message:
        found = False
        for pair in alphabet_nums:
            if char == pair[0]:
                found = True
                char_num = pair[1] - key_places[i]      
                if char_num < 1:
                    char_num = char_num + 26
                for pair in alphabet_nums:
                    if char_num == pair[1]:
                        decoded_message += pair[0]
        if found == False:
            decoded_message += char
            continue
        i += 1
        if i > lim:
            i = 0
    return decoded_message
