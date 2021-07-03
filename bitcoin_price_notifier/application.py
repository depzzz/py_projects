import requests, time
from datetime import datetime

# coinmarketcap for getting bitcoin price
BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1'

# ifttt webhooks post request api url
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{your-api-key}'

# arbituary bitcoin threshold limit for now
BITCOIN_THRESHOLD_LIMIT = 10000

# headers for making a get request to coinmarketcap api with key
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '{your-api-key}'
}

# function to send api request to coinmarketcap and return the price of bitcoin in float
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL,headers=headers).json()
    price = response['data']['1']['quote']['USD']['price']
    return float(price)

# function to make a post request to ifttt webhooks url
def post_ifttt_webook(event,value):
    data = {'value1' : value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url,json=data)

# function to format telegram message with markdown
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)

# keep executing on 5 minutes interval and send the notification to telegram app as soon as the bitcoin_history reaches the length of 5
def main():
    bitcoin_history = []
    while(True):
        price = get_latest_bitcoin_price()
        current_datetime = datetime.now()
        bitcoin_history.append({'date': current_datetime, 'price': price})

        # send emergency notification
        if(price < BITCOIN_THRESHOLD_LIMIT):
            post_ifttt_webook('bitcoin_price_emergency','price')

        # send telegram notification
        if(len(bitcoin_history) == 5):
            post_ifttt_webook('bitcoin_price_update',format_bitcoin_history(bitcoin_history))
            bitcoin_history = []

        # Sleep for 5 minutes 
        time.sleep(5 * 60)

# execute main
if __name__ == '__main__':
    main()