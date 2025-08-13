def validacao_digito(cpf_parcial: str) -> int:
    # Calcula 1 dígito verificador dado um CPF parcial (9 ou 10 dígitos)
    soma_cpf = 0
    # Multiplica cada dígito pelo peso correspondente (decrescente)
    for cpf, peso in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1)):
        soma_cpf += int(cpf) * peso
    # Fórmula para encontrar o dígito
    dig = 11 - (soma_cpf % 11)
    return 0 if dig > 9 else dig  # Regra: se > 9, vira 0


while True:
    # Entrada do CPF
    cpf = input('Digite o seu CPF: (apenas números)')

    # Valida se contém apenas números
    if not cpf.isdigit():
        print('CPF inválido. Digite apenas números.')
        continue
    
    # Valida tamanho máximo permitido
    if len(cpf) > 11:
        print('CPF inválido. Você digitou mais de 11 números.')
        continue

    # Formata para 11 dígitos (com zeros à esquerda se necessário)
    cpf_str = f'{int(cpf):011d}'
    # Adiciona pontos e traço para exibir
    cpf_formatado = f'{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}'
    
    # Confirmação visual com o usuário
    validacao_cpf = input(f'Você digitou o CPF {cpf_formatado}, está correto? (s/n) ').lower()

    if validacao_cpf != 's':
        print('Digite o CPF novamente')
        break
    else:
        print('Ok! Validando CPF...')

    # Calcula o primeiro dígito verificador
    pri_digito = validacao_digito(cpf_str[0:9])
    # Calcula o segundo dígito verificador
    seg_digito = validacao_digito(cpf_str[0:9] + str(pri_digito))

    # Monta o CPF válido com base no cálculo matemático
    cpf_valido = cpf_str[:9] + str(pri_digito) + str(seg_digito)

    # Compara se o CPF informado bate com o calculado
    if cpf_valido == cpf_str:
        print('✅ CPF válido! Bem-vindo!')
        break
    else:
        print('❌ CPF incorreto. Tente novamente.')