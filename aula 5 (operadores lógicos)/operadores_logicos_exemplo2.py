# Definindo as variáveis que representam as condições da compra
valor_da_compra = 120
esta_usando_cupom = False
e_membro_premium = False

tem_direito_a_frete_gratis = (valor_da_compra > 100 and not esta_usando_cupom) or e_membro_premium

print (f'O cliente tem direito a frete grátis? {tem_direito_a_frete_gratis}')

# Saída esperada: O cliente tem direito a frete grátis? True