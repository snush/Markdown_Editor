def plain(text):
    line = input('Text: ')
    text.append(line)
    return text


def bold(text):
    line = input('Text: ')
    text.append(f'**{line}**')
    return text


def italic(text):
    line = input('Text: ')
    text.append(f'*{line}*')
    return text


def header(text):
    level = int(input('Level: '))
    while level < 1 or level > 6:
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    line = input('Text: ')
    text.append(f'{"#" * level} {line}\n')
    return text


def link(text):
    label = input('Label: ')
    link = input('URL: ')
    text.append(f'[{label}]({link})')
    return text


def inline_code(text):
    line = input('Text: ')
    text.append(f'`{line}`')
    return text


def new_line(text):
    text.append('\n')
    return text


def ordered_and_unordered_lists(text):
    rows = int(input('Number of rows: '))
    while rows <= 0:
        print('The number of rows should be greater than zero')
        rows = int(input('Number of rows: '))
    for row in range(rows):
        line = input(f'Row #{row + 1}: ')
        if command == 'ordered-list':
            text.append(f'{row + 1}. {line}\n')
        else:
            text.append(f'* {line}\n')
    return text


formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
text = []

command = input('Choose a formatter: ')
while command != '!done':
    if command == '!help':
        print('Available formatters: plain bold italic header link inline-code new-line\nSpecial commands: !help !done')
    elif command not in formatters:
        print('Unknown formatting type or command')
    elif command == 'plain':
        plain(text)
    elif command == 'bold':
        bold(text)
    elif command == 'italic':
        italic(text)
    elif command == 'header':
        header(text)
    elif command == 'link':
        link(text)
    elif command == 'inline-code':
        inline_code(text)
    elif command == 'new-line':
        new_line(text)
    elif command == 'ordered-list' or command == 'unordered-list':
        ordered_and_unordered_lists(text)
    print(''.join(text))
    command = input('Choose a formatter: ')

with open('output.md', 'w') as final_result:
    final_result.write(''.join(text))
    
