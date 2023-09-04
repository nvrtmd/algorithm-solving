import sys

read = sys.stdin.readline
before_text = read().strip()
modified_text = before_text.replace('[ ', '$@').replace(' ]', '$')
text_word_list = modified_text.split('$')
after_text = ''

documents_dict = {}
document_num = 1
for word in text_word_list:
    if '@' in word:
        documents = word.replace('@', '').split(', ')
        quotation_text = '['
        quotation_num = []
        for d in documents:
            try:
                documents_dict[d]
            except:
                documents_dict[d] = document_num
                document_num += 1
            quotation_num.append(documents_dict[d])

        for n in sorted(quotation_num):
            quotation_text += ' ' + str(n) + ','
        quotation_text = quotation_text[:-1] + ' ]'
        after_text += quotation_text
    else:
        after_text += word
else:
    after_text += '\n'

for name, num in documents_dict.items():
    after_text += '[%d] %s' % (num, name) + '\n'

print(after_text)
