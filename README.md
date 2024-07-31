<h1 align="center">
  :mushroom: Shimeji - Estufa para cultivo de Cogumelos Gastronômicos
</h1>

<p align="center">
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-resultados">Resultados</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-testes">Testes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

## :computer: Projeto

O projeto consiste em um Uma Estufa Automática para cultivo de cogumelos Shimeji. O objetivo do projeto consiste na elaboração de um sistema Automático, utilizando tecnologias da Industria 4.0 como solução Tecnológica da escola Sathya Say.

Dentre as tecnologias utilizadas estão os microcontroladores Raspberry Pi 4 e o Arduino.  


## :sparkles: Tecnologias

  - [Python](https://www.python.org) 
  - [Raspberry Pi](https://www.raspberrypi.com)


## :rocket: Como rodar os Testes

  #### :ocean: Arquivo Test-DHT11
  Esse arquivo .py consiste em um Teste Simples para Testar a biblioteca do Sensor DHT11 da Adafruit. É importante seguir o passo a passo para que ocorra a instalação da biblioteca e ela rode nativamente dentro do Sensor.
  Observação: Atente-se à imagem abaixo para saber onde conectar cada jumper.

1) Digitar o seguinte código no Terminal do Raspberry:
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`

2) Entrar dentro da biblioteca usando esse código:
`cd Adafruit_Python_DHT`

3) Antes de continuar com a instalação é importante ver a atualização do Raspberry. Para isso, digite o seguinte código: <br>
```
sudo apt-get update
sudo apt-get install build-essential python-dev
```
4) Para finalizar a instalação, digite o seguinte código:
`sudo python setup.py install`

## :page_facing_up: Licença

O projeto está sobre a licença MIT. Para maiores informações acesse o arquivo [Licença](LICENSE).
