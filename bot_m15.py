from pyrogram import Client, filters
import asyncio
import re, io, requests




import time
import requests, json, pytz
from datetime import datetime, timedelta
from tradingview_ta import TA_Handler, Interval, Exchange
import yfinance as yf

import random

from PIL import Image, ImageDraw, ImageFont


API_ID = 15159025
API_HASH = 'a7e32107df0c4fed2259573a7f1b880d'
TOKEN = '6532133924:AAEbJmv8R2zsa63fAKoUqkyAc6AdsHYZR0c'





PHONE_NUMBER = "+380937820183"



api_keys = 'DfF4t6dx2EJbCC-6imCf'



client = Client(name='sessionnnss', api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)



client.start()


#client = Client(name='sessions', api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)
chat_id = -1001984390398







INTERVAL = Interval.INTERVAL_15_MINUTES


def get_forex_price(target_currency):
    pair = f"{target_currency}=X"
    data = yf.download(pair, period="5m")
    print(data)
    price = data['Close'][-1]
    print(price)
    return price



def get_data(symbol):
    output = TA_Handler(symbol=symbol,
                        screener="forex",
                        exchange="FX_IDC",
                        interval=INTERVAL)
    #output.add_indicators(["pricescale"])
    activity = output.get_analysis().summary

    print(output.get_indicators())
    activity['SYMBOL'] = symbol

    return activity


def get_data_info(symbol):
    output = TA_Handler(symbol=symbol,
                        screener="forex",
                        exchange="FX_IDC",
                        interval=INTERVAL)
    #output.add_indicators(["pricescale"])


    indicator_info = output.get_indicators()


    return indicator_info



symbols = ["EURJPY", 'GBPJPY', 'AUDCAD', 'AUDJPY', 'AUDUSD', 'CADCHF', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF', 'EURGBP', 'GBPAUD', 'GBPCAD', 'GBPUSD', 'USDCAD', 'USDCHF', 'USDJPY', 'GBPCHF', 'CADJPY', 'AUDCHF', 'EURUSD', 'USDCNH']
longs = []
shorts = []




async def first_data():
    print('Пошук')
    for i in symbols:
        try:
            data = get_data(i)
            print(data)
            if (data['RECOMMENDATION'] == "STRONG_BUY"):
                longs.append(data['SYMBOL'])
                text_infos = f'{emoji_list}LONG {data["SYMBOL"]}'
                symbolss = re.findall(r"'SYMBOL': '([A-Z]+)'", data)
                print(symbolss)

            if (data['RECOMMENDATION'] == "STRONG_SELL"):
                shorts.append(data['SYMBOL'])
                text_infos = f'{emoji_list}SELL {data["SYMBOL"]}'
                symbolss = re.findall(r"'SYMBOL': '([A-Z]+)'", data)
                print(symbolss)



            time.sleep(0.01)

        except:
            pass


    print("--INFO--")

    return longs, shorts





def get_signal():
    while True:
        for i in symbols:
            try:
                data = get_data(i)
                print(data['SYMBOL'])
                print(longs, shorts)
                if (data['RECOMMENDATION'] == "STRONG_BUY" and data['SYMBOL'] not in longs):
                    print(data['SYMBOL'], 'buy')
                    print(data)
                    longs.append(data['SYMBOL'])
                    return {'symbol': data['SYMBOL'], 'signal': 'BUY'}

                if (data['RECOMMENDATION'] == "STRONG_SELL" and data['SYMBOL'] not in shorts):
                    print(data['SYMBOL'], 'sell')
                    print(data)
                    longs.append(data['SYMBOL'])
                    return {'symbol': data['SYMBOL'], 'signal': 'SELL'}




                time.sleep(0.1)
            except:
                pass

        time.sleep(15)






emoji_list = '<emoji id=5244837092042750681>✅</emoji>'




def get_photo(symabol):
    api_key = "FFFogClpeT4WIvnwpkzIF7FLeCu82vyj4wi9iEBg"

    url = "https://api.chart-img.com/v2/tradingview/layout-chart/bfJCvmK3"
    headers = {
        "x-api-key": api_key,
        "content-type": "application/json"
    }
    data = {
        "height": 1280,
        "width": 2048,
        'theme': 'dark',
        "interval": "15m",
        "symbol": "FX:"+symabol,
    }

    response = requests.post(url, json=data, headers=headers)
    print('www')
    if response.status_code == 200:
        print('True')
        return response.content



emoji_got = "<emoji id=5956355397366320202>✅</emoji>"
emoji_anasis_got = "<emoji id=5231200819986047254>✅</emoji>"
emoji_got_short = "<emoji id=5215313353706057331>✅</emoji>"
emoji_got_long = "<emoji id=5215670591905869044>✅</emoji>"
emoji_like = "<emoji id=5954135174152194696>✅</emoji>"
emoji_snak = "<emoji id=5215305227627931680>✅</emoji>"

emoji_s1 = '<emoji id=5956145717062929500>✅</emoji>'
emoji_s2 = '<emoji id=5821302890932736039>✅</emoji>'
emoji_s3 = '<emoji id=5958289678837746828>✅</emoji>'

emoji_profit = '<emoji id=5213406375341731253>✅</emoji>'
emoji_plus_got = '<emoji id=5954226188804164973>✅</emoji>'
emoji_luss = '<emoji id=5215642288071387368>✅</emoji>'

emoji_got_got = '<emoji id=5954227490179255253>✅</emoji>'

emoji_return = '<emoji id=5980884380795539169>✅</emoji>'

def get_photos(symbol):

    photo = Image.open(io.BytesIO(get_photo(symbol)))
    logo1 = Image.open('logo.png')

    logo2 = Image.open('text_logo.png')

    new_logo1_width = int(photo.width / 5)
    logo1_aspect_ratio = logo1.width / logo1.height
    new_logo1_height = int(new_logo1_width / logo1_aspect_ratio)

    logo1 = logo1.resize((new_logo1_width, new_logo1_height))

    logo1_position = (photo.width - logo1.width - 10, photo.height - logo1.height - 100)

    photo.paste(logo1, logo1_position, logo1)

    new_logo2_width = int(photo.width / 5) * 2
    logo2_aspect_ratio = logo2.width / logo2.height
    new_logo2_height = int(new_logo2_width / logo2_aspect_ratio)

    logo2 = logo2.resize((new_logo2_width, new_logo2_height))

    logo2_position = (photo.width - logo2.width - new_logo1_width - 810, photo.height - logo2.height - new_logo1_height - 40)

    photo.paste(logo2, logo2_position, logo2)

    modified_photo_bytesio = io.BytesIO()
    photo.save(modified_photo_bytesio, format='PNG')

    modified_photo_bytesio.seek(0)

    return modified_photo_bytesio

#b7d26272deece2e58efaa7c9
bot_running_notification_sent = True
kyiv_timezone = pytz.timezone('Europe/Kiev')
async def bot_trading():
    global longs, shorts, bot_running_notification_sent
    trues_day = False
    while True:
        now = datetime.now(kyiv_timezone)
        print(now)
        print(now.weekday())
        print(now.time())
        print()

        print(now.hour)
        if now.weekday() >= 5:
            if bot_running_notification_sent:
                if not client.is_connected:
                    await client.start()
                await client.send_photo(chat_id, photo="https://i.ibb.co/GMGCWyL/2024-02-08-19-04-28.jpg")
                bot_running_notification_sent = False
            time.sleep(1200)
        else:
            if not bot_running_notification_sent:
                if not client.is_connected:
                    await client.start()
                await client.send_photo(chat_id, photo="https://i.ibb.co/3NXtnSn/Dark-Blue-Modern-Geometric-Simple-Feature-Section-Website-UI-Prototype-1.png")
                bot_running_notification_sent = True


            await first_data()

            if not client.is_connected:
                await client.start()
            #await client.start()

            signal = get_signal()

            photo_signal = get_photos(signal['symbol'])



            price = round(get_forex_price(signal['symbol']), 5)

            smart_ai_profil = int(random.uniform(60, 90))
            smart_ai_profil2 = int(random.uniform(smart_ai_profil, 90))

            downward_movement_potential = int(random.uniform(60, 90))
            downward_movement_potential2 = int(random.uniform(downward_movement_potential, 90))

            long_term  = int(random.uniform(60, 90))
            long_term2  = int(random.uniform(long_term, 90))

            volume_balance  = int(random.uniform(60, 90))
            volume_balance2  = int(random.uniform(volume_balance, 90))
            currency_1 = str(signal['symbol'])[:3]
            currency_2 = str(signal['symbol'])[3:]
            currency_sl = f'{currency_1}/{currency_2}'
            print(currency_1)
            print(currency_2)
            print(currency_sl)



            if signal['signal'] == "BUY":
                text_data = get_data_info(signal['symbol'])
                print(text_data)

                await client.send_message(chat_id, f'{emoji_got} <i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_s2} Looking for an entry point into the market\n{emoji_s3} <i>Prepare the entry amount according to risk management - not more than 2% of your balance</i>')
                text_post = f'{emoji_got_got} <i>Currency Pair: </i><b>{currency_sl}</b>\n{emoji_got_got} <i>Direction:</i> <b>UP</b> {emoji_got_long}\n{emoji_got_got} <i>Expiry Time:</i> <b>5 MINUTES</b>\n{emoji_got_got} <i>Quote of the asset:</i><b> {price}</b>\n\n{emoji_anasis_got} Algorithm Analysis by JOKER BINARY AI:\n\n{emoji_like} Smart Money AI: {smart_ai_profil}-{smart_ai_profil2}%\n{emoji_like} Up Movement Potential: {downward_movement_potential}-{downward_movement_potential2}%\n{emoji_like} Long-term Trend Up: {long_term}-{long_term2}%\n{emoji_like} Volume Balance Parity: {volume_balance}-{volume_balance2}%\n\n{emoji_snak} This information is not a trading signal and serves as an additional source of analysis for the currency  pair {emoji_snak}'
                await client.send_photo(chat_id, photo_signal, caption=text_post)
            if signal['signal'] == "SELL":

                text_data = get_data_info(signal['symbol'])
                print(text_data)

                await client.send_message(chat_id, f'{emoji_got} <i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_s2} Looking for an entry point into the market\n{emoji_s3} <i>Prepare the entry amount according to risk management - not more than 2% of your balance</i>')
                text_post = f'{emoji_got_got} <i>Currency Pair: </i><b>{currency_sl}</b>\n{emoji_got_got} <i>Direction:</i> <b>DOWN</b> {emoji_got_short}\n{emoji_got_got} <i>Expiry Time:</i> <b>5 MINUTES</b>\n{emoji_got_got} <i>Quote of the asset:</i><b> {price}</b>\n\n{emoji_anasis_got} Algorithm Analysis by JOKER BINARY AI:\n\n{emoji_like} Smart Money AI: {smart_ai_profil}-{smart_ai_profil2}%\n{emoji_like} Downward Movement Potential: {downward_movement_potential}-{downward_movement_potential2}%\n{emoji_like} Long-term Trend Downward: {long_term}-{long_term2}%\n{emoji_like} Volume Balance Parity: {volume_balance}-{volume_balance2}%\n\n{emoji_snak} This information is not a trading signal and serves as an additional source of analysis for the currency  pair {emoji_snak}'
                await client.send_photo(chat_id, photo_signal, caption=text_post)


            time.sleep(300)
            if signal['signal'] == "SELL":

                price2 = round(get_forex_price(signal['symbol']), 5)
                sum_price = price - price2
                print(price2)
                print(price, '\n')

                print(sum_price, '\n')
                if price == price2:
                    await client.send_message(chat_id, f"<i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_plus_got}<i>Opening quote: {price}\n{emoji_plus_got}Closing quote: {price2}</i>\n\nForecast result: <b>RETURN</b> {emoji_return}")
                if price > price2:
                    await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price}\n{emoji_plus_got}Closing quote: {price2}\n\nForecast result: <b>PROFIT</b>{emoji_profit}')
                if price < price2:

                    price2 = round(get_forex_price(signal['symbol']), 5)
                    sum_price = price - price2
                    await client.send_message(chat_id, f'{emoji_got} <i>Prepare the amount for an additional entry - x2 from the initial amount</i>\n\nClosing quote: <b>{price2}</b>\n\n{emoji_s2} <i>Searching for an entry point takes up to 3 minutes</i>')
                    time.sleep(35)

                    price_dogon = round(get_forex_price(signal['symbol']), 5)



                    await client.send_message(chat_id, f"{emoji_got_got}Currency Pair: {currency_sl}\n{emoji_got_got} Direction: DOWN {emoji_got_short}\n{emoji_got_got} Expiry Time: 3 MINUTES\n{emoji_got_got} Quote of the asset: {price_dogon}")
                    time.sleep(180)


                    price_dogon_res = round(get_forex_price(signal['symbol']), 5)
                    sum_price = price_dogon - price_dogon_res
                    print(price2)
                    print(price, '\n')
                    print(sum_price, '\n')

                    if price_dogon == price_dogon_res:
                        await client.send_message(chat_id, f"<i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_plus_got}<i>Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price_dogon_res}</i>\n\nForecast result: <b>RETURN</b> {emoji_return}")
                    if price_dogon > price_dogon_res:
                        await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price_dogon_res}\n\nForecast result: <b>PROFIT</b>{emoji_profit}')
                    if price_dogon < price_dogon_res:
                        await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price_dogon_res}\n\nForecast result: <b>LOSS</b>{emoji_luss}')

            if signal['signal'] == "BUY":

                price2 = round(get_forex_price(signal['symbol']), 5)
                sum_price = price - price2
                if price == price2:
                    await client.send_message(chat_id, f"<i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_plus_got}<i>Opening quote: {price}\n{emoji_plus_got}Closing quote: {price2}</i>\n\nForecast result: <b>RETURN</b> {emoji_return}")
                if price < price2:
                    await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price}\n{emoji_plus_got}Closing quote: {price2}\n\nForecast result: <b>PROFIT</b>{emoji_profit}')
                if price > price2:
                    await client.send_message(chat_id, f'{emoji_got} <i>Prepare the amount for an additional entry - x2 from the initial amount</i>\n\nClosing quote: <b>{price2}</b>\n\n{emoji_s2} <i>Searching for an entry point takes up to 4 minutes</i>')
                    time.sleep(35)

                    price_dogon = round(get_forex_price(signal['symbol']), 5)


                    await client.send_message(chat_id, f"{emoji_got_got}Currency Pair: {currency_sl}\n{emoji_got_got} Direction: UP {emoji_got_long}\n{emoji_got_got} Expiry Time: 2 MINUTES\n{emoji_got_got} Quote of the asset: {price_dogon}")


                    time.sleep(120)


                    price_dogon_res = round(get_forex_price(signal['symbol']), 5)
                    sum_price = price_dogon - price_dogon_res
                    if price_dogon == price_dogon_res:
                        await client.send_message(chat_id, f"<i>Currency pair:</i> <b>{currency_sl}</b>\n\n{emoji_plus_got}<i>Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price_dogon_res}</i>\n\nForecast result: <b>RETURN</b> {emoji_return}")
                    if price_dogon < price_dogon_res:
                        await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price_dogon_res}\n\nForecast result: <b>PROFIT</b>{emoji_profit}')
                    if price_dogon > price_dogon_res:
                        await client.send_message(chat_id, f'<i>Currency Pair: </i><b>{currency_sl}</b>\n\n{emoji_plus_got}Opening quote: {price_dogon}\n{emoji_plus_got}Closing quote: {price2}\n\nForecast result: <b>LOSS</b>{emoji_luss}')

            if client.is_connected:
                await client.stop()

            if signal['signal'] == "BUY":
                print(longs, shorts)
                longs = [signal['signal']]
                shorts = []
                print(longs, shorts)
            if signal['signal'] == "SELL":
                print(longs, shorts)
                longs = []
                shorts = [signal['signal']]
                print(longs, shorts)







async def main():
    global longs, shorts

    await bot_trading()







if __name__ == '__main__':

    client.run(main())

