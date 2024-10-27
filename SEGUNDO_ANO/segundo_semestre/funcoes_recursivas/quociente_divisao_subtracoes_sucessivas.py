def quocienteDivisao(dividendo, divisor):
    resto = dividendo // divisor
    if divisor > resto:
        return 0
    else:
        return 1 + subtracaoSucessiva(dividendo-divisor, divisor)