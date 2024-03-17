
#html form asks for number of ppl in the house, and zip code, and repeats following form x many times
#asks for daily shower duration, toilet flushes, dishwasher usage frequency
#calculations
    #shower duration * water used per min
    #toilet flushes * water used per flush
    #dishwasher usage * water used per cycle
#compare to average shower duration, toilet flushes, dishwasher usage in the zip code

#if user > average, ask chatgpt to give suggestions to shrink that category's usage
#if user < average, ask chatgpt to give positive words

#gives a screenshottable summary of water usage and tips to improve it

import csv
import random
# import avg_usage

global SHOWER_RATE, FLUSH_RATE, CYCLE_RATE, AVG_USAGE
SHOWER_RATE = round(21/19, 1)
FLUSH_RATE = 16/10
CYCLE_RATE = 42/10

AVG_USAGE = 138

def calculate_usage(shower_duration, toilet_flushes, dishwasher_cycles):
    global shower_usage, flush_usage, cycle_usage
    shower_usage = int(shower_duration) * SHOWER_RATE
    shower_usage = round(shower_usage, 2)
    flush_usage = int(toilet_flushes) * FLUSH_RATE
    flush_usage = round(flush_usage, 2)
    cycle_usage = int(dishwasher_cycles) * CYCLE_RATE
    cycle_usage = round(cycle_usage, 2)
    
    total_usage = round(shower_usage + flush_usage + cycle_usage, 2)
    
    return total_usage, shower_usage, flush_usage, cycle_usage

    # return f"""

    #     Water Usage Per Day (in gallons)\n\n
    #     Household: {str(ppl)} people\n\n
    #     Shower Usage: {str(shower_usage)} gallons\n
    #     Toilet Flush Usage: {str(flush_usage)} gallons\n
    #     Dishwasher Cycle Usage: {str(cycle_usage)} gallons\n
    #     Total Usage: {str(total_usage)} gallons\n
    #     """

def average_usage(zip1):
    water_usage_data = {}
    with open('consumption.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            table_zip, avg_usage = row
            water_usage_data[table_zip] = float(avg_usage)

    average_zip_usage = water_usage_data.get(zip1)
    return average_zip_usage



def read_csv():
    pass


def comparing(user_water_consumption, zip_water_consumption):
    global level
    if user_water_consumption > zip_water_consumption:
        level = 'above'
        print('You are above the average by', str(user_water_consumption - AVG_USAGE), 'gallons')
        compliment = random.choice([
    "Please consider lowering your water usage.",
    "You might want to try reducing your water consumption.",
    "Conserving water is important; try using less.",
    "Lowering your water usage can help conserve this precious resource.",
    "Be mindful of your water usage and try to use less whenever possible.",
    "Consider ways to cut back on your water usage for environmental sustainability.",
    "Reducing your water consumption can make a positive impact on the environment.",
    "Help preserve water resources by using less water in your daily activities.",
    "Try to minimize your water usage to help conserve this vital resource.",
    "Being conscious of your water usage and finding ways to reduce it can benefit both you and the planet."
]
)
    elif user_water_consumption < zip_water_consumption:
        level = 'below'
        print('You are doing great. Your water consumption level is much lower than average by', str(AVG_USAGE - user_water_consumption), 'gallons')
        #choose a random statement that tells them to continue lowering their water usage
        compliment = random.choice([
    "Congratulations on your efficient water usage! Keep up the great work!",
    "Great job on conserving water! Your efforts make a positive impact!",
    "Fantastic job on using less water! Your conservation efforts are commendable!",
    "Kudos to you for your low water usage! You're making a difference!",
    "Amazing work on reducing your water consumption! Keep up the excellent effort!",
    "Well done on your minimal water usage! Your commitment to conservation is inspiring!",
    "Congratulations on your responsible water usage! Keep setting a great example!",
    "Impressive job on your water conservation! Your dedication is truly commendable!",
    "Bravo on your efforts to use less water! Keep up the fantastic work!",
    "Congratulations on your eco-friendly water habits! Your contribution to conservation is invaluable!"
]

)
    elif user_water_consumption == zip_water_consumption:
        print('You are exactly on the average water consumption!')
        level = 'exactly on'
        compliment = random.choice([
    "You're using water efficiently; keep up the good work!",
    "Your current water usage seems to be just right. Well done!",
    "It looks like you're already using the appropriate amount of water. Keep it up!",
    "You seem to be using water wisely. Keep maintaining your current usage level!",
    "Your water usage appears to be in line with what's necessary. Great job!",
    "You're already using the right amount of water. Keep it consistent!",
    "Your water usage seems to be appropriate for your needs. Keep it balanced!",
    "Your current water consumption is adequate. Keep up the good habits!",
    "You're using water responsibly. Keep maintaining your current usage level!",
    "It appears that your water usage is sufficient. Keep up the responsible usage!"
]
)
    else:
        pass
    return level, compliment