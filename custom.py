import requests
import base64


def send_sms(phone_number, message):
    # Custom SMS API URL
    encoded_url = "aHR0cHM6Ly90dWhpbi5teS5pZC9BUEktVjEvQ1NNUy1WMz8/bnVtYmVyPTE4WFhYWFhYJm1lc3NhZ2U9aGVsbG8="

   
    decoded_url = base64.b64decode(encoded_url).decode()

    
    url = decoded_url.replace("018XXXXXX", phone_number).replace("hello", message)
    
    
    response = requests.get(url)
    
  
    return response.text

print('''
                                                                                               
                                                                                               
               AAA               RRRRRRRRRRRRRRRRR   XXXXXXX       XXXXXXXUUUUUUUU     UUUUUUUU
              A:::A              R::::::::::::::::R  X:::::X       X:::::XU::::::U     U::::::U
             A:::::A             R::::::RRRRRR:::::R X:::::X       X:::::XU::::::U     U::::::U
            A:::::::A            RR:::::R     R:::::RX::::::X     X::::::XUU:::::U     U:::::UU
           A:::::::::A             R::::R     R:::::RXXX:::::X   X:::::XXX U:::::U     U:::::U 
          A:::::A:::::A            R::::R     R:::::R   X:::::X X:::::X    U:::::D     D:::::U 
         A:::::A A:::::A           R::::RRRRRR:::::R     X:::::X:::::X     U:::::D     D:::::U 
        A:::::A   A:::::A          R:::::::::::::RR       X:::::::::X      U:::::D     D:::::U 
       A:::::A     A:::::A         R::::RRRRRR:::::R      X:::::::::X      U:::::D     D:::::U 
      A:::::AAAAAAAAA:::::A        R::::R     R:::::R    X:::::X:::::X     U:::::D     D:::::U 
     A:::::::::::::::::::::A       R::::R     R:::::R   X:::::X X:::::X    U:::::D     D:::::U 
    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::RXXX:::::X   X:::::XXX U::::::U   U::::::U 
   A:::::A             A:::::A   RR:::::R     R:::::RX::::::X     X::::::X U:::::::UUU:::::::U 
  A:::::A               A:::::A  R::::::R     R:::::RX:::::X       X:::::X  UU:::::::::::::UU  
 A:::::A                 A:::::A R::::::R     R:::::RX:::::X       X:::::X    UU:::::::::UU    
AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRXXXXXXX       XXXXXXX      UUUUUUUUU      
                                                                                               
                                                                                                                                                                                      
''')

phone_number = input("Enter the phone number: ")
message = input("Enter the message: ")

#ARXU
response_text = send_sms(phone_number, message)
print("API Response:", response_text)
