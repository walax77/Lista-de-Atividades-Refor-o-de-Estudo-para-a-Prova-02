biblioteca = [
    {"titulo": "Dom Casmurro", "isbn": "9788544002011"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "isbn": "9788574425017"},
    {"titulo": "O Alienista", "isbn": "9788535911100"},
    {"titulo": "O Guarani", "isbn": "9788573265119"},
    {"titulo": "Senhora", "isbn": "9788525408274"}
]

# Ordenando a lista por ISBN
biblioteca_ordenada = sorted(biblioteca, key=lambda livro: livro["isbn"])
