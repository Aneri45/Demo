import random  
import time  
  
from azure.iot.device import IoTHubDeviceClient, Message  
from datetime import datetime 
 
CONNECTION_STRING = "HostName=IoTHubaneri.azure-devices.net;DeviceId=mydevice01;SharedAccessKey=gIy+ROtoUgLasDxIElMSNS1rK5J8fTu2LNikB1DhNrs="
 
DATA = "Device to Cloud Sample"  
MSG_TXT = '{{{current_datetime} > "Message Count": {messageCount}, "Data": {data}}}'  
 
  
def iothub_client_init():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def iothub_client_telemetry_sample_run():  
    messageCount = 0
    try:  
        client = iothub_client_init()
          
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )  
        while True: 
            
            current_datetime = datetime.now()
            messageCount += 1 
            msg_txt_formatted = MSG_TXT.format(current_datetime=current_datetime, messageCount=messageCount, data=DATA)  
            message = Message(msg_txt_formatted)  
  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(5)  
  
    except KeyboardInterrupt:  
        print ( "IoTHubClient sample stopped" )  
  
if __name__ == '__main__':  
    print ( "IoT Hub Quickstart #1 - Simulated device" )  
    print ( "Press Ctrl-C to exit" )  
    iothub_client_telemetry_sample_run()
