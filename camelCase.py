def display_banner():
    """Display program name in banner"""
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n{stars} \n{msg} \n{stars} \n')

def camel_case(sentence):
    split_sentence = sentence.split()

    i = 0
    while i < len(split_sentence):
        if i == 0:
            split_sentence[i] = split_sentence[i].lower()
            i += 1
        else:
            split_sentence[i] = split_sentence[i].capitalize()
            i += 1

    s = ''

    s = s.join(split_sentence)

    return s

def main():
    display_banner()
    print('Enter a sentence to convert to camelCase!')
    sentence = input('Enter a sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()