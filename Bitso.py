

import requests
from pydub import AudioSegment
from pydub.playback import play



#Poner clase en un demonio
#llamar si hay cambio de precio

class CriptoCoins():
    
    song = AudioSegment.from_mp3('audio.mp3')
    
    def __init__(self, book):
        self.book = book
        
    def get_book(self):
        book = requests.get('https://api.bitso.com/v3/ticker?book=%s'%(self.book) )
        return book.json()
    
    def get_cripto_price(self):
        price =  self.get_book()['payload']['last']
        return float(price)
    
    def historical(self):
        new_price = 0
        while True:
            if(self.get_cripto_price() >= new_price):
                pass
            else:
                print(self.get_cripto_price() )
                play(self.song)
            new_price = self.get_cripto_price()
           #sleep(180)

if __name__ == '__main__':
	CriptoCoins('btc_mxn').historical()



