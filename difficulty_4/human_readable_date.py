def format_duration(seconds):
    result = {'years': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
    result['years'] = seconds  // 3600 * 24 * 354 
    result['days'] = result['years'] // 3600 * 24
    result['hours'] = result['days'] // 3600
    result['seconds'] = result['hours'] // 60
    return result


print(format_duration(1))
print(format_duration(62))
# test.assert_equals(format_duration(3600), "1 hour")
# print("1 hour, 1 minute and 2 seconds")
# print(format_duration(3662))