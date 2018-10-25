import requests
import datetime


def send(out_data, campus):
    re_data = ""
    for i in range(0, len(out_data)):
        re_data = re_data +"\n"+ out_data[i]
        if i % 4 == 0 and i != 0:
            ifttt(re_data,campus)
            re_data = ""
        elif len(out_data) == i + 1:
            ifttt(re_data,campus)
# def send(out_data, campus):
#     # today = day.strftime("%-m/%-d")
#     re_data = split_str(out_data)
#     for i in range(int(len(re_data))):
#         ifttt(str(re_data[i]),campus)


def split_str(s):
    n = 125
    length = len(s)
    return [s[i:i + n] for i in range(0, length, n)]


def ifttt(out_data, campus):
    day = datetime.date.today()
    today = "{}/{}".format(day.month, day.day)
    send_data = {"value1": today, "value2": out_data, "value3": campus}
    headers = {'Content-Type': "application/json"}

    url = 'YOUR_IFTTT_URL'
    response = requests.post(url, json=send_data, headers=headers)
    print(response.status_code)
if __name__ == '__main__':
    send(["1","2","3","4","5","6"], "test_campus")
