from textract import process

text = process('test.pdf')

print(text)
