import random
import string


def generate_password(length: int) -> str:
    """
    Génère un mot de passe sécurisé d'une longueur spécifiée.
    Le mot de passe contient au moins une lettre minuscule,
    une lettre majuscule, un chiffre et un caractère spécial.
    """

    if length < 8 or length > 64:
        raise ValueError('Password length must be between 8 and 64 characters')

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(characters) for _ in range(length - 4)]

    random.shuffle(password)
    password = ''.join(password)

    return password
