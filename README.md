# AutoBeo
 UMA SOLUÇÃO PARA CONSTRUÇÃO DE UM CLUSTER BEOWULF

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto de Automação de Cluster Beowulf</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        ul {
            margin-left: 20px;
        }
        .code {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
        }
    </style>
</head>
<body>

    <h1>Projeto de Automação de Cluster Beowulf</h1>

    <p>Este repositório contém os dados e ferramentas desenvolvidos em nossa pesquisa sobre a automação de configuração de Clusters Beowulf, uma solução prática para lidar com a crescente demanda de poder computacional em aplicações científicas e acadêmicas. Abaixo, você encontrará um resumo do nosso projeto, bem como todos os recursos necessários para recriar o ambiente configurado.</p>

    <h2>Resumo do Projeto</h2>

    <p>Com o aumento exponencial da quantidade de dados e a complexidade das aplicações, tornou-se inviável processar informações de forma sequencial em muitos casos. Visando uma solução acessível para tal desafio, desenvolvemos uma abordagem baseada em Clusters Beowulf, que utiliza computadores comuns interconectados para processar tarefas em paralelo.</p>

    <p>A configuração manual de um Cluster Beowulf, no entanto, requer conhecimentos técnicos específicos e tempo proporcional ao número de máquinas. Para simplificar e acelerar o processo, nosso projeto inclui:</p>
    
    <ul>
        <li><strong>ISO Personalizada do Ubuntu LTS 20.04</strong>: uma imagem do Ubuntu com todos os requisitos para a montagem de um Cluster Beowulf já pré-instalados.</li>
        <li><strong>Guia de Configuração Personalizado</strong>: um passo a passo detalhado para ajudar na montagem e configuração manual do Cluster.</li>
        <li><strong>Script de Automação</strong>: desenvolvido em Python, nosso script facilita a criação do Cluster Beowulf, automatizando a configuração de rede e o ambiente necessário, além de eliminar a necessidade de configuração manual em cada nó.</li>
    </ul>

    <h2>Conteúdo do Repositório</h2>

    <ul>
        <li><code>ISO/</code>: Contém a ISO personalizada do Ubuntu LTS 20.04.</li>
        <li><code>Script/</code>: Diretório com o script de automação e instruções para sua utilização.</li>
        <li><code>Guia_de_Configuracao/</code>: Inclui o guia de configuração manual para referência.</li>
    </ul>

    <h2>Resultados da Pesquisa</h2>

    <p>Os testes realizados com o script de automação mostraram uma redução de cerca de 81,6% no tempo necessário para instalação e configuração do Cluster em comparação com o método manual. Com isso, nossa solução torna o uso de Clusters Beowulf mais acessível a usuários com pouca experiência técnica e mais eficiente para atender aplicações que exigem processamento paralelo.</p>

    <p>Para iniciar, recomendamos começar pelo guia de configuração para se familiarizar com o processo manual, seguido da instalação da ISO personalizada e execução do script, conforme as instruções detalhadas.</p>

</body>
</html>
