import tkinter as tk
from tkinter import ttk, messagebox
from .lexer import Lexer
from .parser import Parser

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        
        self._setup_styles()
        self._create_widgets()
        
    def _setup_styles(self):
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TEntry', padding=5)
        
    def _create_widgets(self):
        self._create_expression_entry()
        self._create_result_label()
        self._create_button_grid()
        self._configure_grid()
        
    def _create_expression_entry(self):
        self.expression_var = tk.StringVar()
        self.expression_entry = ttk.Entry(
            self.root, 
            textvariable=self.expression_var,
            font=('Arial', 14),
            justify='right'
        )
        self.expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
    def _create_result_label(self):
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(
            self.root,
            textvariable=self.result_var,
            font=('Arial', 16, 'bold'),
            anchor='e'
        )
        self.result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')
        
    def _create_button_grid(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'C', 'CE'
        ]
        
        row = 2
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.button_click(x)
            ttk.Button(self.root, text=button, command=cmd).grid(
                row=row, column=col, padx=2, pady=2, sticky='nsew'
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
                
    def _configure_grid(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def button_click(self, char):
        if char == '=':
            self._evaluate()
        elif char == 'C':
            self._clear_all()
        elif char == 'CE':
            self._clear_entry()
        else:
            self._append_char(char)
            
    def _evaluate(self):
        try:
            expression = self.expression_var.get()
            lexer = Lexer()
            tokens = lexer.tokenize(expression)
            parser = Parser(tokens)
            result = parser.parse()
            self.result_var.set(f"= {result}")
        except (ValueError, SyntaxError) as e:
            messagebox.showerror("Error", str(e))
            
    def _clear_all(self):
        self.expression_var.set('')
        self.result_var.set('')
        
    def _clear_entry(self):
        current = self.expression_var.get()
        self.expression_var.set(current[:-1])
        
    def _append_char(self, char):
        current = self.expression_var.get()
        self.expression_var.set(current + char)