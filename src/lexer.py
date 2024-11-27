from .token import Token

class Lexer:
    def __init__(self):
        self.digits = '0123456789'
        self.operators = {'+': 'PLUS', '-': 'MINUS', '*': 'MULTIPLY', '/': 'DIVIDE'}
        
    def tokenize(self, text):
        tokens = []
        i = 0
        
        while i < len(text):
            char = text[i]
            
            if char.isspace():
                i += 1
                continue
                
            if char in self.digits:
                num = ''
                while i < len(text) and (text[i] in self.digits or text[i] == '.'):
                    num += text[i]
                    i += 1
                tokens.append(Token('NUMBER', float(num)))
                continue
                
            if char in self.operators:
                tokens.append(Token(self.operators[char], char))
                i += 1
                continue
                
            if char == '(':
                tokens.append(Token('LPAREN', char))
                i += 1
                continue
            if char == ')':
                tokens.append(Token('RPAREN', char))
                i += 1
                continue
                
            raise ValueError(f'Carácter inválido: {char}')
            
        return tokens