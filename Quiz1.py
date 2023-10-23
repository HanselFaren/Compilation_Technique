def is_keyword(s):
    keywords = ['int', 'float', 'while', 'main', 'const']
    return s in keywords

def tokenize(s):
    tokens = []
    lexemes = []
    i = 0
    while i < len(s):
        if s[i].isspace():
            i += 1
        elif s[i:i+2] == '//':
            i = s.index('\n', i)
        elif s[i:i+2] == '/*':
            i = s.index('*/', i) + 2
        elif s[i].isalpha():
            j = i + 1
            while j < len(s) and (s[j].isalpha() or s[j].isdigit()):
                j += 1
            if is_keyword(s[i:j]):
                tokens.append('keyword')
                lexemes.append(s[i:j])
            i = j
        else:
            i += 1
    return tokens, lexemes

s = 'int main(){const float payment = 384.00;float bal;int month = 0;bal=15000;while (bal>0){printf("Month: %2d Balance: %10.2f\n", month, bal);bal=bal-payment+0.015*bal;month=month+1;}}'
tokens, lexemes = tokenize(s)
for token, lexeme in zip(tokens, lexemes):
    print(token)

