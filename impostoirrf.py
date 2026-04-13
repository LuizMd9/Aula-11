print("-" * 20)
print("Calculo IRRF")
print("-" * 20)

reposta = True 

while  resposta == True:
     try:
        sal_bruto = float(input("Digite seu salario bruto"))
        
        if 2428.88 < sal_bruto <= 2826.65:
            irrf = 0.075
        elif 2826.66 < sal_bruto <= 3751.05:
            irrf = 0.15
        elif 3751 < sal_bruto <= 4664.68:
            irrf = 0.225
        else:
             irrf = 0.275    
            
    
        print(f"{sal_bruto} com {irrf}% = R$ {sal_bruto - (sal_bruto * irrf):.2f}")
        
     except ValueError:
        print("Valor do salário invalido")
        resposta = input("Deseja realizar outro cálculo (S/N): ")
        
        
        if reposta == 'S' or resposta == 's':
            reposta = True
        else:
            reposta = False 
    
