# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

########################################################

## Como funciona esta aplicação
    >>> É necessario ter alguns programas funcioonando em paralelo como:
        pycharm => para rodar a aplicação
        pgadmin4 => para rodar o banco de dados veterinariaDB
        terminal => para instalção de algumas libs python flask
        postman  => para testar as rotas da aplicação

## Dificuldades da aplicação
    >>> 1 - Dificuldade em acertar a renderização dos dados json na tela
    >>> 2 - dificuldade em acertar os dados do banco postgresql com a classe
            implementada no app.py (os campos do banco precisam ser estritamente
            iguais os campos implementados na classe)
    >>> 3 - ERROS DE CORS
            Content Security Policy: As configurações da página bloquearam o carregamento de um recurso em http://127.0.0.1:5000/favicon.ico (“default-src”).
    >>> 4 - Dificuldade em implementar o método POST
            Como implementar o método post com flask e retornar os dados que foram armazenados
            no banco através do postman?
    >>> 5 - Quando Este Erro Surgir:
            
            File "C:\Users\Usuario\Desktop\Projeto_FlaskVete\config.py", line 18, in <genexpr>
            SECRET_KEY = ''.join(random.choice(gen) for i in range(32))
            AttributeError: 'builtin_function_or_method' object has no attribute 'choice'

            Solução:
            Este é um erro clássico de importação errada! neste caso a importação
            foi feita da lib random.random, mas a importação correta seria da lib
            seria da lib random
            

## Links de pesquisa que ajudaram na construção
    como conectar o postgresql no flask - vídeo de ajuda
    https://www.youtube.com/watch?v=XZ_gAWdGzZk
    inserindo valores na tabela_login
    http://www.bosontreinamentos.com.br/postgresql-banco-dados/como-inserir-dados-em-tabelas-no-postgresql-com-insert-into/
    
    react
    https://pt-br.reactjs.org/docs/create-a-new-react-app.html

    sqlalchemy erro
    https://docs.sqlalchemy.org/en/14/errors.html#error-f405

    Erros de segurança cross_origin
    https://www.youtube.com/watch?v=vWl5XcvQBx0&t=246s

    Código de ajuda do repositório Projeto_do_teste
    https://sourcemaking.com/
    https://github.com/BlackCode7/Projeto_do_teste/blob/main/serve/app.py
    https://code.tutsplus.com/pt/tutorials/building-restful-apis-with-flask-diy--cms-26625
    https://blog.debugeverything.com/pt/programacao-em-python-aplicativo-flask/
    https://neps.academy/br/blog/criando-uma-aplica%C3%A7%C3%A3o-web-com-flask---exemplo-simples---parte-1
    
    

## Comandos usados na construção

## Como clonar este repositório
    echo "# Projeto_FlaskVete" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/BlackCode7/Projeto_FlaskVete.git
    git push -u origin main
    
    …or push an existing repository from the command line
    
    git remote add origin https://github.com/BlackCode7/Projeto_FlaskVete.git
    git branch -M main
    git push -u origin main

    
## Parada no tempo em que assisti ao vídeo
    parte_3 >>> min -> 50:57 min >>> configuração de banco de dados na AWS
                e conectando ela na aplicação python / flask