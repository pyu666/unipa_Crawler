import is_holiday_or_weekday as holiday
import unipa_load as unipa
import send_IFTTT as send
import time


def main():
    unipa.main()
    load_senju = unipa.senju_data
    load_chiba = unipa.chiba_data
    load_hatoyama = unipa.hatoyama_data
    print(load_senju + "\n" + load_chiba + "\n" + load_hatoyama)
    if not holiday.senju():
        send.send(load_senju, "千住")
        time.sleep(20)
    if not holiday.chiba():
        send.send(load_chiba, "千葉")
        time.sleep(20)
    if not holiday.hatoyama():
        send.send(load_hatoyama, "鳩山")


if __name__ == '__main__':
    main()
