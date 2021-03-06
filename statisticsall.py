# statisticsall.py
# Script for creating all kinds of statistics.csv
# Iason Ofeidis 2020

import os
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns 
import csv
import json
import patientsfind
# sns.set()



def stat_without_emotion(dirname):
    """ Function for creating 'statistics_user_without_emotion.csv'
        by merging all keystrokes sessions"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_emotion.csv'):
                os.remove(filename)

    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                # df = df.replace('.', '/')
                # Open .csv file and append statistics
                # Needed for header 
                os.chdir(os.path.abspath(os.path.join(os.getcwd(), "./..")))
                file_exists = os.path.isfile('./statistics_user_without_emotion.csv')
                with open('statistics_user_without_emotion.csv', 'a', newline='') \
                        as csvfile:
                    fieldnames = ['Keystrokes', 'Date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_user_without_emotion.csv', mode='a', index=False,
                          header=False)    


def stat_without_keystrokes(dirname):
    """ Function for creating 'statistics_user_without_keystrokes.csv'
        by merging all 'emotion.csv'"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_keystrokes.csv') or \
               filename.endswith('statistics_user_info_emotion.csv'):
                os.remove(filename)

    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('emotion.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                # df = df.replace('.', '/')
                # Open .csv file and append statistics
                # Needed for header 
                os.chdir(os.path.abspath(os.path.join(os.getcwd(), "./..")))
                file_exists = \
                    os.path.isfile('./statistics_user_without_keystrokes.csv')
                with open('statistics_user_without_keystrokes.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Mood', 'Physical_State', 'Date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_user_without_keystrokes.csv', mode='a', index=False,
                          header=False)
    
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('Info.json'):
                data = patientsfind.info(filename)
                df = pd.DataFrame([data])
                dfinfo = df.User_PHQ9
                # df = df.replace('.', '/')
                # Open .csv file and append statistics
                # Needed for header 
                # os.chdir(os.path.abspath(os.path.join(os.getcwd(), "./..")))
                file_exists = \
                    os.path.isfile('./statistics_user_without_keystrokes.csv')
                if file_exists:
                    data = pd.read_csv('statistics_user_without_keystrokes.csv')
                    dfstat = pd.DataFrame(data)

                    df = pd.concat([dfinfo, dfstat], ignore_index=True, axis=1)
                    df = df.fillna(method='ffill')
                    file_exists = \
                        os.path.isfile('./statistics_user_info_emotion.csv')
                    with open('statistics_user_info_emotion.csv',
                              'w', newline='') as csvfile:
                        fieldnames = ['User_PHQ9', 'Mood', 'Physical_State', 'Date']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if not file_exists:
                            writer.writeheader()
                    df.to_csv('statistics_user_info_emotion.csv', mode='a', index=False,
                              header=False)
                
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_keystrokes.csv'):
                os.remove(filename)
            


def sessions_total_ios(dirname):
    """ Function for creating 'statistics_total_sessions.csv' in iOS files
        by merging all 'statistics_user_without_emotions.csv'"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_emotion.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                os.chdir(dirname)
                # Open .csv file and append total statistics
                # Needed for header 
                file_exists = os.path.isfile('./statistics_total_sessions.csv')
                with open('statistics_total_sessions.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Keystrokes', 'Date']        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_total_sessions.csv', mode='a', index=False,
                          header=False)


def sessions_total_android(dirname):
    """ Function for creating 'statistics_total_sessions.csv' in Android files
        by merging all 'statistics_user.csv'"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                df = df[['Keystrokes', 'Date']]
                os.chdir(dirname)
                # Open .csv file and append total statistics
                # Needed for header 
                file_exists = os.path.isfile('./statistics_total_sessions.csv')
                with open('statistics_total_sessions.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Keystrokes', 'Date']        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_total_sessions.csv', mode='a', index=False,
                          header=False)


def emotions_total_ios(dirname):
    """ Function for creating 'statistics_total_emotions.csv' in iOS files
        by merging all 'statistics_user_without_keystrokes.csv'"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_keystrokes.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                os.chdir(dirname)
                # Open .csv file and append total statistics
                # Needed for header 
                file_exists = os.path.isfile('./statistics_total_emotions.csv')
                with open('statistics_total_emotions.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Mood', 'Physical_State', 'Date']        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_total_emotions.csv', mode='a', index=False,
                          header=False)


def emotions_total_android(dirname):
    """ Function for creating 'statistics_total_emotions.csv' in Android files
        by merging all 'statistics_user.csv'"""
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                df = df[['Mood', 'Physical_State', 'Date']]
                os.chdir(dirname)
                # Open .csv file and append total statistics
                # Needed for header 
                file_exists = os.path.isfile('./statistics_total_emotions.csv')
                with open('statistics_total_emotions.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Mood', 'Physical_State', 'Date']        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_total_emotions.csv', mode='a', index=False,
                          header=False)


def statistics_add(dirname):
    """ Just add all 'statistics_user.csv' to a single .csv file"""

    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            # change filename depending on plots
            if filename.endswith('statistics_user_info_emotion.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                df = df[['User_PHQ9', 'Mood', 'Physical_State', 'Date']]
                userid = \
                    str(os.path.abspath(os.path.join(os.getcwd(), "./.")))\
                    .split('/')[-1]
                b = pd.DataFrame([{'UserID': userid}])
                df = pd.concat([b, df], axis=1).fillna(method='ffill')
                os.chdir(dirname)
                # Open .csv file and append total statistics
                # Needed for header 
                file_exists = os.path.isfile('./statistics_total_added_info.csv')
                with open('statistics_total_added_info.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['UserID', 'User_PHQ9', 
                                  'Mood', 'Physical_State', 'Date']        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_total_added_info.csv', mode='a', index=False,
                          header=False)


def dynamics(jsonFile, device):
    """Gather all keystroke dynamics of user in a single .csv"""
    if device == 'Android':
        # Data Acquisition from JSON files
        with open(jsonFile) as json_file:
            data = json.load(json_file)
        # Keeping only SESSION_DATA from json file
        datasession = json.loads(data['SESSION_DATA'])
        # Date of Session
        date = data['DATE_DATA']
        # Format: Y-M-d
        date = date.split(',')[0]
        
        # DownTime
        datadown = (datasession['DownTime'])
        # Uptime
        dataup = (datasession['UpTime'])
        # Euclidean Distance
        distance = datasession['Distance']
        # Deliberately Long Pressed Button
        islongpress = datasession['IsLongPress']
        # PressureValues
        # pressure = datasession['PressureValue']
        # print(islongpress)
    elif device == 'iOS':
        # Data Acquisition from JSON files
        with open(jsonFile) as json_file:
            datasession = json.load(json_file)

        # DownTime
        datadown = (datasession['startTimeOfKeyPressed'])
        # Uptime
        dataup = (datasession['stopTimeOfKeyPressed'])
        # Euclidean Distance
        distance = datasession['distanceBetweenKeys']
        # Deliberately Long Pressed Button
        islongpress = datasession['longPressed']
        # PressureValues
        # pressure = datasession['pressureMax']
        # print(islongpress)
        # Date
        tmp = str((os.path.basename(os.getcwd())))
        try1 = tmp.split('.')
        date = try1[2] + '-' + try1[1] + '-' + try1[0]

    # ht: HoldTime, ft: FlightTime
    # sp: Speed, pfr: Press-Flight-Rate
    # pv: Pressure Values
    ht = []
    ft = []
    sp = []
    pfr = []
    # pv = []

    length = len(datadown)

    for p in range(length - 1):
        # 0 < flight time < 3000 ms (3 sec)
        # 0 < hold time < 300 ms (0.3 sec)
        tempft = datadown[p + 1] - dataup[p]
        tempht = dataup[p] - datadown[p]
        if tempft > 0 and tempft < 3000 and\
           tempht > 0 and tempht < 300 and\
           (islongpress[p] == 0):
            ft.append(tempft)
            ht.append(tempht)
            # pv.append(pressure[p])
        
    # Total Number of Characters
    length = len(ht)
    lengthht = len(ht)
    lengthft = len(ft)
    lengthdis = len(distance)
    minlength = min(lengthht, lengthft, lengthdis)


    for p in range(minlength - 1):
        sp.append(distance[p] / ft[p])
        pfr.append(ht[p] / ft[p])
        
    # dr: Delete Rate
    # if length > 0:
    #     dr = (datasession['NumDels']) / length
    # else:
    #     dr = 0
    # # Duration of Session (in msec)
    # duration = datasession['StopDateTime'] - datasession['StartDateTime']

    # Convert data lists to Panda.Series
    htseries = pd.Series(ht)
    ftseries = pd.Series(ft)
    spseries = pd.Series(sp)
    pfrseries = pd.Series(pfr)
    # pvseries = pd.Series(pv)

    # Insert Characteristics into Variables Dictionary
    variables = {'Hold_Time': htseries, 'Flight_Time': ftseries,
                 'Speed': spseries, 'Press_Flight_Rate': pfrseries,
                 'Date': date}

    df = pd.DataFrame({key: pd.Series(value) for key, value in variables.items()})
    df.Date = df.Date.fillna(method='ffill')

    # Open .csv file and append statistics
    # Needed for header
    file_exists = os.path.isfile('./dynamics.csv')
    with open('dynamics.csv', 'a', newline='') as csvfile:
        fieldnames = ['Hold_Time', 'Flight_Time', 'Speed',
                      'Press_Flight_Rate', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
    
    df.to_csv('dynamics.csv', mode='a', index=False,
              header=False)
    return


def dynamics_add(dirname, device):
    """ Just add all 'dynamics.csv' to a single 'dynamics_user.csv' file"""
    # Remove existing statistics related .csv files
    for root, dirs, files in os.walk(dirname, topdown=False):
        for filename in files:
            # print(os.path.join(root, filename))
            os.chdir(os.path.abspath(root))
            if filename.endswith('dynamics.csv') or \
               filename.endswith('dynamics_user.csv'):
                os.remove(filename)

    if device == 'Android':
        # Loop across all files and create dynamics.csv
        # containing typingdata of all sessions in a day
        os.chdir(dirname)
        for root, dirs, files in os.walk(dirname, topdown=False):
            for filename in files:
                os.chdir(os.path.abspath(root))
                if filename.endswith('.json'):
                    dynamics(filename, device)
                    

        # Create dynamics_user.csv
        os.chdir(dirname)
        for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            for filename in files:
                os.chdir(os.path.abspath(root))
                if filename.endswith('dynamics.csv'):
                    data = pd.read_csv(filename)
                    df = pd.DataFrame(data)
                    os.chdir(dirname)
                    # Open .csv file and append total statistics
                    # Needed for header 
                    file_exists = os.path.isfile('./dynamics_user.csv')
                    with open('dynamics_user.csv',
                              'a', newline='') as csvfile:
                        fieldnames = ['Hold_Time', 'Flight_Time', 'Speed',
                                      'Press_Flight_Rate', 'Date']      
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if not file_exists:
                            writer.writeheader()
                    df.to_csv('dynamics_user.csv', mode='a', index=False,
                              header=False)
    elif device == 'iOS':
        # Loop across all files and create dynamics.csv
        # containing typingdata of all sessions in a day
        os.chdir(dirname)
        for root, dirs, files in os.walk(dirname, topdown=False):
            for filename in files:
                os.chdir(os.path.abspath(root))
                if (not filename.startswith('Emotion')) and \
                   (not filename.startswith('RawData')) and\
                   (not filename.startswith('Info')) and\
                   filename.endswith('.json'):
                    # print(filename)
                    dynamics(filename, device)
                    

        # Create dynamics_user.csv
        os.chdir(dirname)
        for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            for filename in files:
                os.chdir(os.path.abspath(root))
                if filename.endswith('dynamics.csv'):
                    data = pd.read_csv(filename)
                    df = pd.DataFrame(data)
                    os.chdir(dirname)
                    # Open .csv file and append total statistics
                    # Needed for header 
                    file_exists = os.path.isfile('./dynamics_user.csv')
                    with open('dynamics_user.csv',
                              'a', newline='') as csvfile:
                        fieldnames = ['Hold_Time', 'Flight_Time', 'Speed',
                                      'Press_Flight_Rate', 'Date']      
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if not file_exists:
                            writer.writeheader()
                    df.to_csv('dynamics_user.csv', mode='a', index=False,
                              header=False)
    
    return


def dynamics_users(dirname, device):
    """Loop across all users for dynamics_user.csv"""

    if device == 'Android':
        os.chdir(dirname)
        for root, dirs, files in os.walk(dirname, topdown=False):
            for dir in dirs:
                # If directory refers to user and not a day of sessions
                if ('2020' not in dir) and ('2019' not in dir):
                    os.chdir(os.path.join(root, dir))
                    dynamics_add(os.path.join(root, dir), device)
    elif device == 'iOS':
        os.chdir(dirname)
        for root, dirs, files in os.walk(dirname, topdown=False):
            for dir in dirs:
                # If directory refers to user and not a day of sessions
                if ('2020' not in dir) and ('2019' not in dir):
                    os.chdir(os.path.join(root, dir))
                    dynamics_add(os.path.join(root, dir), device)


def stat_info_emotion(dirname):
    """ UNNECESSARY """
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_info_emotion.csv'):
                os.remove(filename)

    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user_without_keystrokes.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                # df = df.replace('.', '/')
                # Open .csv file and append statistics
                # Needed for header 
                os.chdir(os.path.abspath(os.path.join(os.getcwd(), "./..")))
                file_exists = \
                    os.path.isfile('./statistics_user_without_keystrokes.csv')
                with open('statistics_user_without_keystrokes.csv',
                          'a', newline='') as csvfile:
                    fieldnames = ['Mood', 'Physical_State', 'Date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                df.to_csv('statistics_user_without_keystrokes.csv', mode='a', index=False,
                          header=False)    


def dynamics_total(dirname, device, peakdate):
    """ Merge all dynamics_user.csv into a single dynamics_total_added.csv """
    if device == 'Android':
        print('DO STH')
    elif device == 'iOS':
        os.chdir(dirname)
        dfall = pd.DataFrame([])
        for root, dirs, files in os.walk(os.getcwd(), topdown=True):
            for filename in files:
                os.chdir(os.path.abspath(root))
                if filename.endswith('dynamics_user.csv'):
                    data = pd.read_csv(filename)
                    dfstat = pd.DataFrame(data)
                    userphq9 = -1
                    userid = \
                        str(os.path.abspath(os.path.join(os.getcwd(), "./.")))\
                        .split('/')[-1]
                    for rootb, dirsb, filesb in os.walk(os.getcwd(), topdown=True):
                        for filenameb in filesb:
                            if filenameb.endswith('Info.json'):
                                userphq9 = patientsfind.info(filenameb)['User_PHQ9']
                    dfstat = dfstat[dfstat['Date'] > '2020-02-14']
                    dfstat.loc[(dfstat.Date < peakdate), 'Date'] = 'period1'
                    dfstat.loc[(dfstat.Date >= peakdate) & 
                               (dfstat.Date != 'period1'), 'Date'] = 'period2'
                    if 'period1' in dfstat.Date.values and \
                       'period2' in dfstat.Date.values:
                        for value, dfdate in dfstat.groupby('Date'):
                            stat = {'UserID': userid, 'User_PHQ9': userphq9,
                            
                                    'HT_Mean': dfdate.Hold_Time.mean(),
                                    'HT_STD': dfdate.Hold_Time.std(),
                                    'HT_Skewness': dfdate.Hold_Time.skew(),
                                    'HT_Kurtosis': dfdate.Hold_Time.kurtosis(), 
                                    
                                    'FT_Mean': dfdate.Flight_Time.mean(),
                                    'FT_STD': dfdate.Flight_Time.std(),
                                    'FT_Skewness': dfdate.Flight_Time.skew(),
                                    'FT_Kurtosis': dfdate.Flight_Time.kurtosis(), 
                                    
                                    'SP_Mean': dfdate.Speed.mean(),
                                    'SP_STD': dfdate.Speed.std(),
                                    'SP_Skewness': dfdate.Speed.skew(),
                                    'SP_Kurtosis': dfdate.Speed.kurtosis(), 
                                    
                                    'PFR_Mean': dfdate.Press_Flight_Rate.mean(),
                                    'PFR_STD': dfdate.Press_Flight_Rate.std(),
                                    'PFR_Skewness': dfdate.Press_Flight_Rate.skew(),
                                    'PFR_Kurtosis': dfdate.Press_Flight_Rate.kurtosis(), 
                                    
                                    'Sessions': len(dfdate),
                                    'Date': value}
                            b = pd.DataFrame([stat])
                            dfall = pd.concat([dfall, b])
        dfall = dfall.reset_index(drop=True)
        os.chdir(dirname)
        dfall = dfall.round(4)
        dfall = dfall.fillna(0)
        dfall.to_csv('dynamics_total_added_' + str(peakdate) + '.csv',
                     mode='w', index=False,
                     header=True)
        # print(dfall.head(10))
                    

def check_nusers():
    """ Check number of users with statistics in both periods """
    for s in range(30):
        p = 0
        if s < 10:
            peakdate = '2020-03-0' + str(s)
        else:
            peakdate = '2020-03-' + str(s)
        print(peakdate)
        os.chdir('/home/jason/Documents/Thesis/azuretry2/iOS')
        for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            for f in files:
                os.chdir(os.path.abspath(root))
                if f.startswith('statistics_user.csv'):
                    data = pd.read_csv(f)
                    df = pd.DataFrame(data)
                    # df = df[df.Keystrokes > 4]
                    # userid = \
                    #     str(os.path.abspath(os.path.join(os.getcwd(), "./.")))\
                    #     .split('/')[-1]
                    if not df.empty:
                        if max(df.Date.values) >= peakdate and \
                           min(df.Date.values) < peakdate:
                            p += 1

    print(p)


def check_availability():
    """ Check number of users with no dynamics or emotion """
    os.chdir('/home/jason/Documents/Thesis/TypingData/iOS')
    p = 0
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for d in dirs:
            os.chdir(os.path.abspath(root))
            if not d.endswith('2020') and \
               not d.endswith('2019'): 
                # print(os.path.abspath(os.path.join(root, d)))
                os.chdir(os.path.abspath(os.path.join(root, d)))
                for rootb, dirsb, filesb in os.walk(os.getcwd(), topdown=True):
                    # print(filesb)    
                    if 'statistics_user_info_emotion.csv' not in filesb or \
                       'dynamics_user.csv' not in filesb:
                        print(os.getcwd())  
                        p += 1
                    break
    print(p)


def distrib(dirname):
    """ Create distrib.csv of users 
        by merging dynamics + statistics """
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for d in dirs:
            os.chdir(os.path.abspath(root))
            if not d.endswith('2020') and \
               not d.endswith('2019'):
                # print(os.path.abspath(os.path.join(root, d)))
                os.chdir(os.path.abspath(os.path.join(root, d)))
                for rootb, dirsb, filesb in os.walk(os.getcwd(), topdown=True):
                    # print(filesb)    
                    if 'statistics_user.csv' in filesb and \
                       'dynamics_user.csv' in filesb:
                        userid = \
                            str(os.path.abspath(os.path.join(os.getcwd(), "./.")))\
                            .split('/')[-1]
                        print(userid)
                        data = pd.read_csv('dynamics_user.csv')
                        dyn = pd.DataFrame(data)
                        data = pd.read_csv('statistics_user.csv')
                        stat = pd.DataFrame(data)
                        dyn = dyn[dyn.Hold_Time.notna()]
                        stat = stat.drop(columns='Keystrokes').drop_duplicates()
                        h = pd.merge(dyn, stat, how='left', on='Date')
                        h.to_csv('distributions.csv', mode='w', index=False,
                                 header=True)
                    break


def sessions_features(dirname):
    """ Compute dynamics features per session per user 
        by using distributions.csv 
        Just a groupby('Date') in distributions.csv """
    os.chdir(dirname)
    for root, dirs, files in os.walk(os.getcwd(), topdown=True):
        for f in files:
            os.chdir(os.path.abspath(root))
            if f.startswith('distributions.csv'):
                data = pd.read_csv(f)
                df = pd.DataFrame(data)
                df = df.round(5)
                df.Mood = df.Mood.fillna('undefined')
                df.Physical_State = df.Physical_State.fillna('undefined')
                df = df[df.Hold_Time < 1]
                df = df[df.Flight_Time < 3]
                df = df[df.Speed < 1000]
                df = df[df.Press_Flight_Rate < 1.5]
                dfall = pd.DataFrame([])
                for a, b in df.groupby('Date'):
                    dfs = pd.DataFrame([])
                    if len(b) > 10:

                        stat = {
                            # 'UserID': userid, 'User_PHQ9': userphq9,

                            'HT_Mean': b.Hold_Time.mean(),
                            'HT_STD': b.Hold_Time.std(),
                            'HT_Skewness': b.Hold_Time.skew(),
                            'HT_Kurtosis': b.Hold_Time.kurtosis(), 
                            
                            'FT_Mean': b.Flight_Time.mean(),
                            'FT_STD': b.Flight_Time.std(),
                            'FT_Skewness': b.Flight_Time.skew(),
                            'FT_Kurtosis': b.Flight_Time.kurtosis(), 
                            
                            'SP_Mean': b.Speed.mean(),
                            'SP_STD': b.Speed.std(),
                            'SP_Skewness': b.Speed.skew(),
                            'SP_Kurtosis': b.Speed.kurtosis(), 
                            
                            'PFR_Mean': b.Press_Flight_Rate.mean(),
                            'PFR_STD': b.Press_Flight_Rate.std(),
                            'PFR_Skewness': b.Press_Flight_Rate.skew(),
                            'PFR_Kurtosis': b.Press_Flight_Rate.kurtosis(), 
                            
                            'Characters': len(b),
                            'Mood': b.Mood.values[0],
                            'Physical_State': b.Physical_State.values[0],
                            'Date': a,
                            'Window': b.window.values[0],
                            'Period': b.period.values[0]
                        }
                        dfs = pd.DataFrame([stat])

                        dfall = pd.concat([dfall, dfs])
                if not dfall.empty:
                    dfall = dfall.round(5).to_csv('sessions_user.csv', mode='w',
                                                  index=False, header=True)
                # print(dfall)
                # for a, b in dfall.groupby('Mood'):
                #     print(a)
                #     print(b)


def statisticsdates(dirname):
    """ Print some statistics about labels for each user """
    os.chdir(dirname)
    p = 0
    dfall = pd.DataFrame([])
    # Includes data between 15 January - April
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('sessions_user.csv'):
                data = pd.read_csv(filename)
                df = pd.DataFrame(data)
                stressed = len(df[df.Mood == 'Stressed'])
                sad = len(df[df.Mood == 'Sad'])
                happy = len(df[df.Mood == 'Happy'])
                undefined = len(df[df.Mood == 'undefined'])
                neutral = len(df[df.Mood == 'Neutral'])
                percentage = len(df[df.Date > '2020-02-28']) / len(df)
                userid = str(os.path.abspath(os.path.join(os.getcwd(), "./.")))\
                    .split('/')[-1]
                # print(userid)
                # print('Stressed: ' + str(stressed))
                # print('Sad: ' + str(sad))
                # print('Happy: ' + str(happy))
                # print('undefined: ' + str(undefined))
                # print('Neutral: ' + str(neutral))
                stat = {'UserID': userid.split('-')[0], 
                        'Useful Labels': happy + stressed + sad,
                        'Happy': happy,
                        'Stressed': stressed,
                        'Sad': sad, 'undefined': undefined, 'Neutral': neutral,
                        'Period_Percentage': percentage}
                dfall = pd.concat([dfall, pd.DataFrame([stat])])
                p += 1
    print(dfall.set_index('UserID').sort_values('Useful Labels',
                                                 ascending=False).round(2))
    print('Undefined: ' + str(dfall.undefined.sum()))
    print('Neutral: ' + str(dfall.Neutral.sum()))
    print('Useful Labels: ' + str(dfall['Useful Labels'].sum()))
    print('Happy: ' + str(dfall.Happy.sum()))
    print('Stressed: ' + str(dfall.Stressed.sum()))
    print('Sad: ' + str(dfall.Sad.sum()))
    print('Total Users:' + str(p))



# Workflow

# stat_without_keystrokes(os.path.abspath(dirname))
# emotion(os.getcwd())
# emotions_total_android(os.getcwd())
# emotions_total_ios(os.getcwd())

# stat_without_emotion(os.path.abspath(dirname))
# sessions(os.getcwd())
# sessions_total_android(os.getcwd())
# sessions_total_ios(os.getcwd())


