import datetime
import jpholiday
import sys
today = datetime.date.today()
week = today.weekday()


def senju():
    global today
    global week
    if jpholiday.is_holiday(today) or week == 6:
        return True
    begin_spring_weekday = datetime.date(2018, 4, 9)
    end_spring_weekday = datetime.date(2018, 7, 28)
    begin_fall_weekday = datetime.date(2018, 9, 10)
    end_fall_weekday = datetime.date(2019, 1, 18)
    begin_winter_holiday = datetime.date(2018, 12, 26)
    end_winter_holiday = datetime.date(2019, 1, 6)
    return (begin_winter_holiday <= today <= end_winter_holiday
            or not (begin_spring_weekday <= today <= end_spring_weekday
                    or begin_fall_weekday <= today <= end_fall_weekday))


def chiba():
    global today
    global week
    if jpholiday.is_holiday(today) or week == 5 or week == 6:
        return True
    begin_spring_weekday = datetime.date(2018, 4, 9)
    end_spring_weekday = datetime.date(2018, 7, 28)
    begin_fall_weekday = datetime.date(2018, 9, 10)
    end_fall_weekday = datetime.date(2019, 1, 18)
    begin_winter_holiday = datetime.date(2018, 12, 26)
    end_winter_holiday = datetime.date(2019, 1, 6)
    return (begin_winter_holiday <= today <= end_winter_holiday
            or not (begin_spring_weekday <= today <= end_spring_weekday
                    or begin_fall_weekday <= today <= end_fall_weekday))


def hatoyama():
    global today
    global week
    if jpholiday.is_holiday(today) or week == 6:
        return True
    begin_spring_weekday = datetime.date(2018, 4, 9)
    end_spring_weekday = datetime.date(2018, 7, 28)
    begin_fall_weekday = datetime.date(2018, 9, 10)
    end_fall_weekday = datetime.date(2019, 1, 18)
    begin_winter_holiday = datetime.date(2018, 12, 26)
    end_winter_holiday = datetime.date(2019, 1, 6)
    return (begin_winter_holiday <= today <= end_winter_holiday
            or not (begin_spring_weekday <= today <= end_spring_weekday
                    or begin_fall_weekday <= today <= end_fall_weekday))


if __name__ == '__main__':
    print("千住は休日か " + str(senju()))
    print("千葉は休日か " + str(chiba()))
    print("鳩山は休日か " + str(hatoyama()))
