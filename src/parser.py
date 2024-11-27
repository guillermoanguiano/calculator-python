class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        
    def get_current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
        
    def eat(self, token_type):
        current_token = self.get_current_token()
        if current_token and current_token.type == token_type:
            self.pos += 1
            return current_token
        raise SyntaxError(f'Se esperaba {token_type}, se obtuvo {current_token.type if current_token else "None"}')
        
    def parse(self):
        result = self.expr()
        return int(result) if result.is_integer() else result
        
    def expr(self):
        result = self.term()
        
        while self.pos < len(self.tokens):
            token = self.get_current_token()
            if token.type not in ['PLUS', 'MINUS']:
                break
                
            self.pos += 1
            if token.type == 'PLUS':
                result += self.term()
            else:
                result -= self.term()
                
        return result
        
    def term(self):
        result = self.factor()
        
        while self.pos < len(self.tokens):
            token = self.get_current_token()
            if token.type not in ['MULTIPLY', 'DIVIDE']:
                break
                
            self.pos += 1
            if token.type == 'MULTIPLY':
                result *= self.factor()
            else:
                divisor = self.factor()
                if divisor == 0:
                    raise ValueError('División por cero')
                result /= divisor
                
        return result
        
    def factor(self):
        token = self.get_current_token()
        
        if token.type == 'NUMBER':
            self.pos += 1
            return token.value
            
        if token.type == 'LPAREN':
            self.pos += 1
            result = self.expr()
            self.eat('RPAREN')
            return result
            
        raise SyntaxError(f'Token inesperado: {token}')