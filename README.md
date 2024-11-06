<h1>AutoBeo: Automação para Configuração de Clusters Beowulf</h1>

<p>Este repositório contém os dados e ferramentas desenvolvidas para a automação de configuração de Clusters Beowulf, uma solução prática para lidar com a crescente demanda de poder computacional em aplicações científicas e acadêmicas.</p>

<h2>Resumo do Projeto</h2>

<p>O aumento exponencial da quantidade de dados e da complexidade de aplicações científicas e acadêmicas elevou a demanda por poder computacional, tornando inviável o processamento sequencial em muitos casos. Para atender a essa necessidade de forma acessível, este trabalho desenvolve uma solução baseada em Clusters Beowulf, que utilizam múltiplos computadores comuns conectados para processar tarefas em paralelo.</p>

<p>A configuração manual desses clusters exige conhecimentos técnicos específicos e tempo proporcional ao número de máquinas. O projeto inclui uma versão personalizada do sistema operacional Ubuntu e um script de automação que simplifica e acelera o processo. Os testes demonstraram uma redução significativa no tempo de instalação e configuração, tornando o uso de Clusters Beowulf mais acessível a usuários com menos experiência técnica e mais eficiente para aplicações que requerem processamento paralelo.</p>

<h2>Conteúdo do Repositório</h2>

<ul>
  <li><strong>ISO/</strong>: Contém a ISO personalizada do Ubuntu LTS 20.04.</li>
  <li><strong>Script/</strong>: Diretório com o script de automação e instruções para sua utilização.</li>
  <li><strong>Guia_de_Configuracao/</strong>: Inclui o guia de configuração manual para referência.</li>
</ul>

<h2>Resultados da Pesquisa</h2>

<p>Os testes realizados com o script de automação demonstraram uma redução de cerca de 81,6% no tempo necessário para instalação e configuração do Cluster em comparação com o método manual. Isso torna a solução AutoBeo uma ferramenta eficaz para tornar o uso de Clusters Beowulf mais acessível a usuários com pouca experiência técnica, além de mais eficiente para atender aplicações que exigem processamento paralelo.</p>

<p>Para começar, recomendamos que você consulte o guia de configuração para entender o processo manual, seguido da instalação da ISO personalizada e execução do script, conforme instruções detalhadas abaixo.</p>

<h2>Primeiros Passos</h2>

<h3>1 – Navegar até o Diretório do Script</h3>

<p>Navegue até a pasta contendo o arquivo <code>0_main.py</code>:</p>

<pre><code>cd ~/AutoBeo/Script
</code></pre>

<h3>2 – Executar o Script</h3>

<p>Para iniciar a automação, execute o script com o comando:</p>

<pre><code>sudo python3 0_main.py
</code></pre>

<h3>3 – Avançar no Script</h3>

<p>Durante a execução, o script pode ser pausado por mensagens de status. Para avançar, basta pressionar <strong>"q"</strong>.</p>
