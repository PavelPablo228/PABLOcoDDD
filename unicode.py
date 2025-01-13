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


# #	Кодировка	                    html/charset	saintfish/chardet	  softlandia/cpd	   enca
# 1	CP1251	                        windows-1252	    CP1251	                  CP1251	   CP1251
# 2	CP866	                        windows-1252	    windows-1252	           CP866	   CP866
# 3	KOI8-R	                        windows-1252	    KOI8-R	                  KOI8-R	   KOI8-R
# 4	ISO-8859-5	                    windows-1252	    ISO-8859-5	          ISO-8859-5	   ISO-8859-5
# 5	UTF-8 with BOM	                utf-8	            utf-8	                   utf-8	   utf-8
# 6	UTF-8 without BOM	            utf-8	            utf-8	                   utf-8	   utf-8
# 7	UTF-16LE with BOM	            utf-16le	        utf-16le	            utf-16le	   ISO-10646-UCS-2
# 8	UTF-16LE without BOM	        windows-1252	    ISO-8859-1	            utf-16le	   unknown
# 9	UTF-16BE with BOM	            utf-16le	        utf-16be	            utf-16be	   ISO-10646-UCS-2
# 10 UTF-16BE without BOM	        windows-1252	    ISO-8859-1	            utf-16be	   ISO-10646-UCS-2
# 11 UTF-32LE with BOM	            utf-16le	        utf-32le	            utf-32le	   ISO-10646-UCS-4
# 12 UTF-32LE without BOM	        windows-1252	    utf-32le	            utf-32le	   ISO-10646-UCS-4
# 13 UTF-32BE with BOM	            windows-1252	    utf-32be	            utf-32be	   ISO-10646-UCS-4
# 14 UTF-32BE without BOM	        windows-1252	    utf-32be	            utf-32be	   ISO-10646-UCS-4
# 15 KOI8-R (UPPER)	                windows-1252	    KOI8-R	                KOI8-R	       CP1251
# 16 CP1251 (UPPER)	                windows-1252	    CP1251	                CP1251	       KOI8-R
# 17 CP866 & CP1251	                windows-1252	    CP1251	                CP1251         unknown