from binance.client import Client
import pyrebase

config = {
  "apiKey": "AIzaSyCIhzO4ZOJtx9KoXHQE-YlzEioXnmN5vyo",
  "authDomain": "pyrebaserealtimedbdemo-7f6cb.firebaseapp.com",
  "projectId": "pyrebaserealtimedbdemo-7f6cb",
  "storageBucket": "pyrebaserealtimedbdemo-7f6cb.appspot.com",
  "messagingSenderId": "806999326021",
  "appId": "1:806999326021:web:09b6546f1b2c5e882c922c",
  "measurementId": "G-6J3MN8VRYK",
  "databaseURL" : "https://pyrebaserealtimedbdemo-7f6cb-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("migruedav@gmail.com","Kumo8521!")
db = firebase.database()

api_key    = 'glrxacPAoL82BwKAfWvsqEYmM4pWys6wXfBZOwWYXGKAnCW4nplV62SUDLqsC1b2'
api_secret = '8bllLJnlvLogsbOAflT8N32oSuKrV6aDM8efdze7XdEgW5oYio6cyKOejH4SpPoT'
client = Client(api_key, api_secret)

days_fact = []
for i in range(1,457):
    d = 19-((18/456)*i)
    days_fact.append(d)

USDT = ['1INCH','AAVE','ADA','ALGO','ALICE','ALPHA','ANKR','APE','ATOM','AUDIO','AVAX','BAKE','BAND','BCH','BLZ','BNB','BTC','CELO','CHZ','COMP','COTI','CRV','DASH','DOGE','DOT','DUSK','ENJ','EOS','ETC','ETH','FIL','FTM','FTT','GALA','GMT','HOT','ICP','IOTA','KAVA','KLAY','KSM','LINK','LRC','LTC','MANA','MATIC','MKR','NEAR','NEO','OCEAN','ONE','ONT','OP','QTUM','REEF','REN','RLC','RUNE','RVN','SAND','SOL','STORJ','SUSHI','SXP','THETA','TOMO','TRX','UNFI','UNI','VET','WAVES','XEM','XLM','XMR','XRP','XTZ','YFI','ZEC','ZEN','ZIL'
]


def cryptopower():
    data = []
    for coin in USDT:
        klines = client.get_historical_klines(coin+"USDT", Client.KLINE_INTERVAL_1HOUR, "19 day ago UTC")
        close = []
        for i in range(len(klines)):
            close.append(float(klines[i][4]))
        open = []
        for i in range(len(klines)):
            open.append(float(klines[i][1]))
        change = []
        for i in range(len(close)):
            chg = ((close[i]/open[i])-1)*100
            change.append(chg)
        power_all = []
        for i in range(len(days_fact)):
            ch = change[i]/days_fact[i]
            power_all.append(ch)
        win_list = []
        lose_list =[]
        for i in range(len(power_all)):
            if power_all[i]>=0:
                win_list.append(power_all[i])
            else:
                lose_list.append(power_all[i])
        win = sum(win_list)
        lose = sum(lose_list)
        lose = lose*-1
        win_perc = win/(win+lose)
        lose_perc = lose/(win+lose)
        if win_perc>lose_perc:
            power=round(win_perc*100,2)
            direction = "bullish"
        else:
            power=round(lose_perc*100,2)
            direction = "bearish"
        data.append({"coin":coin,"power":power,"direction":direction})
        data = sorted(data, key=lambda d: d['power'], reverse=True)
        db.child('Crypto').set(data, user['idToken'])
    return data

cryptopower()