import requests
import datetime
import jpholiday
import sys


def send(out_data, campus):
    day = datetime.date.today()
    # today = day.strftime("%-m/%-d")
    today = "{}/{}".format(day.month, day.day)
    send_data = {"value1": today, "value2": out_data, "value3": campus}
    headers = {'Content-Type': "application/json"}
    url = 'YOUR_IFTTT_URL'
    response = requests.post(url, json=send_data, headers=headers)
    print(response.status_code)


if __name__ == '__main__':
    send(test, test)
