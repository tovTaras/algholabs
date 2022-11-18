ICQ = 256
primal_num = 101


def search_for_patterns(text, pattern, primal_num=101):
    text_length = len(text)
    pattern_length = len(pattern)
    text_hash = 0
    pattern_hash = 0
    hash_num = 1
    for i in range(pattern_length-1):
        hash_num = (hash_num * ICQ) % primal_num

    for i in range(pattern_length):
        pattern_hash = (ICQ * pattern_hash + ord(pattern[i])) % primal_num
        text_hash = (ICQ * text_hash + ord(text[i])) % primal_num


    j = 0
    positions = list()
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            for j in range(pattern_length):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1
            if j == pattern_length:
                positions.append(i)
        if i < text_length - pattern_length:
            text_hash = (ICQ * (text_hash - ord(text[i]) * hash_num) + ord(text[i + pattern_length])) % primal_num
    return positions


if __name__ == '__main__':
    text = "123"
    pattern = "0"
    primal_num = 101
    result = search_for_patterns(text, pattern)
    print(result)

