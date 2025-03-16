import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Selecciona 3 preguntas aleatorias
#zip crea tuplas que agrupan las preguntas con sus respuestas y el índice correcto.
#list(zip()) convierte el conjunto de tuplas en una lista.
#random.choices(k=3) selecciona 3 preguntas aleatorias de esa lista.
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# Inicializo contador de puntaje
score = 0

# Itero sobre las preguntas seleccionadas
for question, answer_options, correct_index in questions_to_ask:
    print(question)

    # Muestro las opciones de respuesta
    for i, option in enumerate(answer_options):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for attempt in range(2):
        user_input = input("Respuesta: ")

        # Validar que sea un número dentro del rango válido
        if not user_input.isdigit() or not (1 <= int(user_input) <= len(answer_options)):
            print("Respuesta no válida")
            sys.exit(1)

        user_answer = int(user_input) - 1 # Convertir a entero y ajustar índice

        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            print("¡Correcto!")
            score += 1  # Suma 1 punto por respuesta correcta
            break
        else:
            score -= 0.5  # Resta 0.5 por intento fallido

    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:", answer_options[correct_index])

    # Se imprime un blanco al final de la pregunta
    print()

# Mostrar puntaje final
print(f"Tu puntaje final es: {score:.1f} puntos")