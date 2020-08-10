import requests
import json
user = "xxxx"
password = "xxxxx"
checkip = "http://thisisnt.com/api/getRemoteIp.php"
dynupdate = "https://members.dyndns.org/v3/update"
print ("Iniciando. Obteniendo la IP...")
ipraw = requests.get(checkip)
if ipraw.status_code is not 200:
  raise "No se encontro una IP Pública"
  exit

ip = ipraw.json()['REMOTE_ADDR']
print ("IP PUBLICA: " + ip)
print ("Actualizando...")


# update dyndns
headers = {'user-agent': 'mPythonClient/0.0.3'}
dyn = requests.get(dynupdate, \
              headers=headers, \
              auth=(user, password), \
              params={'hostname': 'xxxxxxxx.dnsalias.com', \
                       'myip': ip, \
                       })
if dyn.status_code is not 200:
  print ("Actualización Fallida. HTTP Code: " + str(dyn.status_code))
if "good" in dyn.text:
  print ("Actualización Correcta")
else:
  print ("Error al actualizar : " + dyn.text.strip())