# Procesador de Lenguaje para Calculadora

Este proyecto implementa una calculadora básica con interfaz gráfica, incluyendo un analizador léxico y un analizador sintáctico. La calculadora soporta operaciones aritméticas básicas y paréntesis.

## Componentes

1. **Analizador Léxico (`lexer.py`)**
   - Divide la entrada en tokens (números, operadores, paréntesis)
   - Maneja números decimales
   - Soporta operadores: +, -, *, /
   - Soporta paréntesis para agrupación

2. **Analizador Sintáctico (`parser.py`)**
   - Implementa análisis sintáctico descendente recursivo
   - Maneja precedencia de operadores
   - Evalúa expresiones
   - Soporta paréntesis anidados

3. **Interfaz Gráfica (`calculator_gui.py`)**
   - Interfaz gráfica basada en Tkinter
   - Cuadrícula de botones para entrada
   - Visualización de expresiones
   - Visualización de resultados
   - Manejo de errores

## Características

- Operaciones aritméticas básicas (+, -, *, /)
- Soporte para paréntesis
- Soporte para números decimales
- Manejo de errores para entradas inválidas
- Funciones de Borrar y Borrar Entrada
- Visualización de expresiones en tiempo real

## Cómo Ejecutar

1. Asegúrate de tener Python instalado
2. Ejecuta el siguiente comando:
   ```
   python calculator_gui.py
   ```

## Uso

1. Ingresa expresiones usando los botones de la interfaz o el teclado
2. Presiona '=' para evaluar
3. Usa 'C' para borrar todo
4. Usa 'CE' para borrar la última entrada

## Manejo de Errores

La calculadora maneja varios tipos de errores:
- Caracteres inválidos
- Errores de sintaxis
- División por cero
- Expresiones inválidas