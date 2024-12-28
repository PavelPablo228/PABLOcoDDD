open(r"...txt", 'w', encoding='cp1251').write('Hello\n')

encoding = [
'utf-8',
'cp500',
'utf-16',
'GBK',
'windows-1251',
'ASCII',
'US-ASCII',
'Big5'
]

correct_encoding = ''

for enc in encoding:
    try:
        open(r"...txt", encoding=enc).read()
    except (UnicodeDecodeError, LookupError):
        pass
    else:
        correct_encoding = enc
        print('Done!')
        break


print(correct_encoding)
