with open("teste.html", "w") as ímpares:
    titulo = str(input("Digite o título: "))


    ímpares.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <link rel="stylesheet" href="/menu/main.css">
</head>
<body>
    <div id="all">
        <header>
            <h1>{titulo}</h1>
            <h3>writer: Daniel Matos</h3>
        </header>
        
    </div>
</body>
</html>""")


ímpares.close()