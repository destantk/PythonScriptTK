import os
from datetime import datetime

import psutil
from suds.client import Client

swap = psutil.swap_memory()
vir = psutil.virtual_memory()
# Get Swap & Virtual Memory Size
swapYuzde = (swap.used * 100) / swap.total
virYuzde = (vir.used * 100) / vir.total


def smsSend(param):
    url = "http://10.140.../Sms/sms.php?wsdl"
    client = Client(url)
    request = client.factory.create('SmsSend')
    request.mesaj = param
    request.gsmno.append("05......")
    result = client.service.SmsSend(request.gsmno, request.mesaj)
    repr(result)


def restart():
    os.system("/opt/apache2/bin/apachectl stop")
    os.system("sleep 30")
    os.system("ps -ef | grep java | awk {'print $2'} | xargs kill")
    os.system("/opt/apache2/bin/apachectl start")


if swapYuzde > 90:
    mesaj = "Swap:" + str(swapYuzde) + " Vir:" + str(virYuzde)
    print(mesaj)
    # smsSend(mesaj)
    restart()

mesaj = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - Swap: " + " (%" + str(swapYuzde) + ") " + str(swap.used) + "/" + str(swap.total) + " - Virt: " + " (%" + str(virYuzde) + ") " + str(vir.used) + "/" + str(vir.total)
print(mesaj)
