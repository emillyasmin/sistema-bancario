from datetime import datetime

extrato = {}
movimentacoes = 0
conta_bancaria = 0
qnt_saques = 0
LIMITE_SAQUE = 3

def format_numero(tipo):
  while True:
    try:
        valor = float(input(f"Qual valor deseja {tipo}? "))
        if not 0 <= valor <= 1000000:
            raise ValueError("Erro! Insira um valor válido.")
    except:
        print("Erro! Insira um valor válido.")
    else:
        return valor
        break

def hora_atual():
  data_e_hora_atuais = datetime.now()
  data_e_hora_em_texto = data_e_hora_atuais.strftime("Realizado no dia %d/%m/%Y às %H:%M")
  return data_e_hora_em_texto

def add_ao_extrato(numero_movimentacao, tipo, valor):
  extrato[numero_movimentacao] = [tipo, valor, hora_atual()]

def exibe_extrato(dicio):
  for chave, valor in dicio.items():
    if valor[0] == "saque":
      print(f"{chave} | {valor[0].center(10)} | - R$ {valor[1]:.2f} | {valor[2]}")
    else:
      print(f"{chave} | {valor[0].center(10)} | + R$ {valor[1]:.2f} | {valor[2]}")

menu = f"""
{" SISTEMA BANCÁRIO ".center(40, "-")}

[1] Depositar
[2] Sacar
[3] Visualizar extrato
[0] Sair

>>> O que você deseja fazer? """

while True:
  escolha = input(menu)
  print("".center(40, "-"))

  if escolha == "1":
    valor = format_numero("depositar")
    if valor != 0:
      conta_bancaria += valor
      movimentacoes += 1
      add_ao_extrato(movimentacoes, "depósito", valor)
      print("Valor depositado com sucesso!")
    else:
      continue

  elif escolha == "2":
    valor = format_numero("sacar")
    limite_saques = qnt_saques >= LIMITE_SAQUE
    limite_valor = valor > 500
    limite_conta = valor > conta_bancaria

    if limite_saques:
      print("Erro! Você possui um limite de 3 saques diários.")  
    elif limite_valor:
      print("Erro! Você só pode sacar até R$ 500,00.")
    elif limite_conta:
      print("Erro! Você não tem esse dinheiro.")

    elif valor != 0:
      conta_bancaria -= valor
      movimentacoes += 1
      qnt_saques += 1
      add_ao_extrato(movimentacoes, "saque", valor)
      print("Valor sacado com sucesso!")

    else:
      continue

  elif escolha == "3":
    if movimentacoes == 0:
      print("Ainda não houve movimentações na conta.\n")
    else:
      exibe_extrato(extrato)
    print(f"\nSaldo Atual: R$ {conta_bancaria:.2f}")

  elif escolha == "0":
    break

  else:
    print("Opção inválida, tente novamente.")  
