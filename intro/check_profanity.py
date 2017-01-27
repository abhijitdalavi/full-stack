import urllib

def read_text():
    quotes = open('/Users/J/FullStack/full-stack/intro/quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen('http://isithackday.com/arrpi.php?text='+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if 'true' in output:
        print('Ohhhh you sad a bad word!')
    elif 'false' in output:
        print('No bad words here!')
    else:
        print('I can\'t read this.')

read_text()
