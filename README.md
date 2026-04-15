⏱️ SomaHoras

Uma ferramenta simples e prática para somar horas rapidamente no dia a dia — criada para resolver um problema real: agilizar o cálculo de jornadas de trabalho.

🔗 Acesse: https://thiiagosci.github.io/SomaHoras/

📌 Sobre o projeto

O SomaHoras nasceu da necessidade de otimizar cálculos de horas durante o trabalho. Em vez de fazer contas manualmente ou usar planilhas, desenvolvi uma solução direta, leve e funcional.

A proposta é simples:

Inserir horários no formato HHMM ou HH:MM
Somar automaticamente
Retornar o total em HH:MM:SS
⚙️ Funcionalidades
✅ Soma múltiplos horários
✅ Aceita formatos flexíveis (0800 ou 08:00)
✅ Resultado automático
✅ Interface simples e objetiva
✅ Funciona direto no navegador (GitHub Pages)
🧠 Como funciona

O cálculo é feito convertendo todos os horários para segundos, somando tudo e depois reconvertendo para horas, minutos e segundos.

Trecho da lógica principal:

def soma_horas(*horas):
    total_segundos = 0

    for hora in horas:
        if len(hora) == 4:
            hora = hora[:2] + ':' + hora[2:] + ':00'
        
        h, m, s = map(int, hora.split(':'))
        total_segundos += h * 3600 + m * 60 + s

    horas_totais = total_segundos // 3600
    minutos_totais = (total_segundos % 3600) // 60
    segundos_totais = total_segundos % 60

    return '{:02d}:{:02d}:{:02d}'.format(horas_totais, minutos_totais, segundos_totais)

📎 Código completo disponível em:

🎨 Interface

O projeto utiliza um CSS simples, focado em:

Layout centralizado
Boa legibilidade
Uso leve de sombras e cores

📎 Estilo base:

🚀 Tecnologias utilizadas
HTML
CSS
Python (versão inicial com Flask)
GitHub Pages (deploy estático)
💡 Motivação

Esse projeto não foi feito para ser complexo — foi feito para ser útil.

É o tipo de ferramenta que resolve um problema específico de forma rápida, sem excesso de tecnologia ou dependências.

📦 Como usar
Acesse o site
Insira os horários desejados
Clique para somar
Veja o resultado instantaneamente
📈 Possíveis melhorias futuras
⏳ Histórico de cálculos
📱 Melhor responsividade mobile
💾 Exportação de resultados
🧮 Suporte a horas negativas (subtração)
👨‍💻 Autor

Desenvolvido por Thiago Brito
GitHub: https://github.com/thiiagosci