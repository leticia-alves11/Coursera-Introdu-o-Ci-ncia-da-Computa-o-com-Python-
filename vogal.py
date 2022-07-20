def vogal(caractere):
    if isinstance(caractere, str):
        vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return caractere in vogais
    return False

# Realiza o teste com vogais
def test_vogais():
    assert vogal("a") == True

# Realiza o teste com consoantes
def test_consoantes():
    assert vogal("b") == False

# Realiza o teste com valores diferentes de string
def test_NaoString():
    assert vogal(1) == False
