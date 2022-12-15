import socket
import dht
from time import sleep
import machine
from machine import Pin, ADC

led = Pin(2, Pin.OUT)
sensor = dht.DHT22(Pin(14))
pot=ADC(0)

led_state = "OFF"

def read_sensor():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    pot_value = pot.read()
    print('Temperature: %3.1f C' %temp)
    print('Luminosity:', pot_value)
    print('Humidity: %3.1f %%' %hum)
    return temp, hum, pot_value

def web_page():
    result_sensor = read_sensor()
    html = """<!DOCTYPE html>

    <head>
    <meta charset="UTF-8">
    <title>Proyecto Unidad</title>
    <link rel="shortcut icon" href="tech.png">

       <link href="style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
		<div id="titulo" class="titulo">
                        <h1>Proyecto Unidad </h1>

        </div>
                <div id=”prin” class="prin">

                        <identificación de la sección=”columna_izquierda”>
				
                		<div id=”uno” class="uno">
                        <h2>Temperatura</h2>
                         	<img src="https://previews.123rf.com/images/john79/john791704/john79170400067/75985636-s%C3%ADmbolo-de-cambio-de-temperatura-sol-term%C3%B3metro-lluvia-nieve-.jpg">
                            <h2>""" + str(result_sensor[0]) + """ </h2>
                            
					    </div>
					    <div id=”dos” class="dos">
                    		<h2>Humedad</h2>
							<img src="https://cdn-icons-png.flaticon.com/512/728/728093.png">
                            <h2>""" + str(result_sensor[1]) + """ </h2>
                            
					    </div>
					    <div id=”tres” class="tres">
                    		<h2>Luminocidad</h2>
                    		<img src="https://thumbs.dreamstime.com/b/icono-de-vectores-negrita-luminosidad-que-se-puede-editar-o-modificar-f%C3%A1cilmente-168779008.jpg">
                            <h2>""" + str(result_sensor[2]) + """ </h2>
					    </div>
					    <div id=”cuatro” class="cuatro">
                    		<h2>Control de On/Off (Led)</h2>
                            <a href=\"?led_on" class="button1">ON</a>
                        	<a href=\"?led_off" class="button2">OFF</a>
					    </div>
                </div>
                <div id="pied" class="pie">
                            <p>MAESTRÍA EN SISTEMAS COMPUTACIONALES SEMESTRES AGOSTO 2022 – ENERO 2023</p>
                            <p>Tecnologías de Internet</p>
                            <p>Autor: Romero Velazco Fátima Adriana</p>
                            <p>Profesora: Dra. Patricia Elizabeth Figueroa Millán</p>
                            <p></p>
              
              
              </div>
              
              
              <style>
              body {
  width: 1200px;
  height: 1040px;
  margin: 0 auto;
  background-color: black;
  padding: 0 20px 20px 20px;
  border: 5px solid white;
}
h1 {
  margin-top: 2px;
  font-size: 60px;
  text-align: center;
}

h2 {
  font-size: 20px;
  text-align: center;
}

p, li {
  font-size: 10px;
  line-height: 2;
  letter-spacing: 1px;
}
img {
  display: block;
  margin: 0 auto;
  width: 80px;
  height: 80px;
}
/*Contenedores de los Parametros*/
.titulo {
  margin-top: 15px;
  margin-bottom: 50px;
  margin-left: 10px;
  margin-right: 10px;
  background-color: lightblue;
  padding: 40px;
  width: 1090px;
  height: 50px;
  border: 5px solid white;
  color: white;
}

.prin {
  margin-top: 15px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgreen;
  padding: 40px;
  width: 1090px;
  height: 400px;
  border: 5px solid white;
}

.uno {
  margin-top: 5px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgray;
  padding: 40px;
  width: 110px;
  height: 250px;
  float: left;
  border: 5px solid white;
}

.dos {
  margin-top: 5px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgray;
  padding: 40px;
  width: 110px;
  height: 250px;
  float: left;
  border: 5px solid white;
}

.tres {
  margin-top: 5px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgray;
  padding: 40px;
  width: 110px;
  height: 250px;
  float: left;
  border: 5px solid white;
}

.cuatro {
  margin-top: 5px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgray;
  padding: 40px;
  width: 110px;
  height: 250px;
  float: left;
  border: 5px solid white;
}
.cinco {
  margin-top: 5px;
  margin-bottom: 50px;
  margin-left: 10px;
  background-color: lightgray;
  padding: 40px;
  width: 110px;
  height: 250px;
  float: left;
  border: 5px solid white;
}

.pie {
  margin-top: 10px;
  margin-bottom: 50px;
  margin-left: 10px;
  margin-right: 10px;
  background-image: url("tec1.jpg");
  padding: 40px;
  width: 1090px;
  height: 180px;
  border: 5px solid white;
  font-size: 12px;
  font-weight: 900;
  color: #07F2FD;
}

/*Caja de Texto*/
input {
  margin-top: 5px;
  width: 100%;
}

/*Alerta*/
.Reset {
  width: 5px;
  height: 5px;
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 13px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

/*Botones */
.button1 {
	background-color: #4CAF50;
	border-radius: 8px;
	font-size: 15px;
	
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin: 4px 2px;
    cursor: pointer;
}

.button2 {
	background-color: #f44336;
	border-radius: 8px;
	font-size: 15px;
	
	border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin: 4px 2px;
    cursor: pointer;
}
              </style>
  </body>
</html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        led_on = request.find('/?led_on')
        led_off = request.find('/?led_off')
        if led_on == 6:
            print('LED ON -> GPIO2')
            led_state = "ON"
            led.on()
        if led_off == 6:
            print('LED OFF -> GPIO2')
            led_state = "OFF"
            led.off()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
