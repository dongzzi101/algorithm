from math import ceil

def solution(fees, records):
    def convert_to_minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    def get_fee(time):
        basic_time, basic_fee, unit_time, unit_fee = fees
        if time <= basic_time:
            return basic_fee
        return basic_fee + ceil((time - basic_time) / unit_time) * unit_fee

    in_time = {}     
    total_time = {}  

    for record in records:
        time, car, state = record.split()
        time = convert_to_minute(time)

        if state == "IN":
            in_time[car] = time
        else:  
            total = time - in_time[car]
            total_time[car] = total_time.get(car, 0) + total
            del in_time[car]

    end_time = convert_to_minute("23:59")
    for car in in_time:
        total = end_time - in_time[car]
        total_time[car] = total_time.get(car, 0) + total

    answer = []
    for car in sorted(total_time):
        answer.append(get_fee(total_time[car]))

    return answer