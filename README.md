<h1>AutoBeo: Uma Solução para Contrução de um Cluster Beowulf</h1>

<p>Este repositório contém os dados e ferramentas desenvolvidas para a automação de configuração de Clusters Beowulf, uma solução prática para lidar com a crescente demanda de poder computacional em aplicações científicas e acadêmicas.</p>

<h2>Resumo do Projeto</h2>

<p>O aumento exponencial da quantidade de dados e da complexidade de aplicações científicas e acadêmicas elevou a demanda por poder computacional, tornando inviável o processamento sequencial em muitos casos. Para atender a essa necessidade de forma acessível, este trabalho desenvolve uma solução baseada em Clusters Beowulf, que utilizam múltiplos computadores comuns conectados para processar tarefas em paralelo.</p>

<p>A configuração manual desses clusters exige conhecimentos técnicos específicos e tempo proporcional ao número de máquinas. O projeto inclui uma versão personalizada do sistema operacional Ubuntu e um script de automação que simplifica e acelera o processo. Os testes demonstraram uma redução significativa no tempo de instalação e configuração, tornando o uso de Clusters Beowulf mais acessível a usuários com menos experiência técnica e mais eficiente para aplicações que requerem processamento paralelo.</p>

<h2>Conteúdo do Projeto</h2>

<ul>
  <li><strong>AutoBeo_OS</strong>: Contém a ISO personalizada do Ubuntu LTS 20.04.</li>
  <li><strong>Script</strong>: Diretório com o script de automação e instruções para sua utilização.</li>
  <li><strong>Guia - AutoBeo</strong>: Inclui o guia de configuração automatizado</li>
  <li><strong>Guia - Manual</strong>: Inclui o guia de configuração manual</li>
</ul>

<h2>Primeiros Passos</h2>

<h3>1 – Realizar Download da ISO</h3>

<p>Faça o download do sistema operacional e instale em todas as máquinas que vão ser utilizadas no cluster (atente-se para que o nome de usuário seja o mesmo em todas)</p>

<pre><code>https://mega.nz/file/eFsnzZIK#CFSSSs8AEwAeTcVN30g6S7YhOLBXYbOWpCVx-YpcCKY</code></pre>

<h3>2 – Navegue até o Diretório do Script</h3>

<p>Estando no computador "Mestre" navegue até a pasta contendo o arquivo <code>0_main.py</code>:</p>

<pre><code>cd /etc/AutoBeo/Script </code></pre>

<h3>3 – Executar o Script</h3>

<p>Para iniciar a automação, execute o script com o comando:</p>

<pre><code>sudo python3 0_main.py
</code></pre>

<h3>4 – Avançar no Script</h3>

<p>Durante a execução, o script pode ser pausado por mensagens de status. Para avançar, basta pressionar <strong>"q"</strong> ou digitar a senha solicitada.</p>
