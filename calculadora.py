from IPython.display import display, HTML

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Willian</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #1e1e1e;
            color: white;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        #calculadora {
            width: 320px;
            padding: 20px;
            background-color: #333;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        #entrada {
            width: 100%;
            height: 70px;
            font-size: 32px;
            margin-bottom: 10px;
            text-align: right;
            padding-right: 10px;
            border-radius: 5px;
            border: none;
            background-color: #444;
            color: white;
        }
        .botoes {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 10px;
        }
        button {
            width: 100%;
            height: 60px;
            font-size: 24px;
            border-radius: 10px;
            border: none;
            background-color: #555;
            color: white;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #777;
        }
        button:active {
            background-color: #999;
        }
        #equal {
            background-color: #28a745;
            color: white;
        }
        #equal:hover {
            background-color: #5bcf60;
        }
        #clear {
            background-color: #dc3545;
        }
        #clear:hover {
            background-color: #f57171;
        }
    </style>
</head>
<body>
    <div id="calculadora">
        <input type="text" id="entrada" disabled>

        <div class="botoes">
            <button onclick="inserir('7')">7</button>
            <button onclick="inserir('8')">8</button>
            <button onclick="inserir('9')">9</button>
            <button onclick="inserir('/')">/</button>

            <button onclick="inserir('4')">4</button>
            <button onclick="inserir('5')">5</button>
            <button onclick="inserir('6')">6</button>
            <button onclick="inserir('*')">*</button>

            <button onclick="inserir('1')">1</button>
            <button onclick="inserir('2')">2</button>
            <button onclick="inserir('3')">3</button>
            <button onclick="inserir('-')">-</button>

            <button onclick="inserir('0')">0</button>
            <button onclick="inserir('.')">.</button>
            <button id="equal" onclick="calcular()">=</button>
            <button onclick="inserir('+')">+</button>

            <button id="clear" onclick="limpar()">C</button>
        </div>
    </div>

    <script>
        function inserir(valor) {
            document.getElementById('entrada').value += valor;
        }

        function limpar() {
            document.getElementById('entrada').value = '';
        }

        function calcular() {
            try {
                let resultado = eval(document.getElementById('entrada').value);
                document.getElementById('entrada').value = resultado;
            } catch (e) {
                document.getElementById('entrada').value = 'Erro';
            }
        }
    </script>
</body>
</html>
"""
# exibir na tela:
display(HTML(html_code))

# apos executar o arquivo py, o codigo cria um arquivo HTML
# pra abrir no navegador e rodar o codigo:
with open('calculadora_willian.html', 'w') as file:
    file.write(html_code)
