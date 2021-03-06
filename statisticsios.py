# statisticsios.py
#
# Script for extracting statistics of session data
# from .json file to DataFrames
# for iOS devices
#
# Iason Ofeidis 2019

import json
import pandas as pd 
# import numpy as np 
# import sys
import os
import csv
# import matplotlib.pyplot as plt
# import math

# Function for extracting typing session data
# from .json file to .csv file


def keystrokes(jsonFile):
    # Data Acquisition from JSON files
    with open(jsonFile) as json_file:
        datasession = json.load(json_file)

    # Length of Characters
    keystrokes = datasession['sumOfCharacters']

    # Duration
    # duration = datasession['keyboardDownTime'] - datasession['keyboardDownTime'] 

    stat = {'Keystrokes': keystrokes}

    return stat


def emotion(jsonFile):
    # Data Acquisition from JSON files
    with open(jsonFile) as json_file:
        datasession = json.load(json_file)

    # ?Mood and Physical State?
    # Current Mood
    mood = datasession['currentMood']
    # Current Physical State
    physicalstate = datasession['currentPhysicalState']

    stat = {'Mood': mood, 'Physical_State': physicalstate}

    return stat


def info(jsonFile):
    # Data Acquisition from JSON files
    with open(jsonFile) as json_file:
        datasession = json.load(json_file)

    # UserID
    userid = datasession['userDeviceID']
    # UserAge
    userage = datasession['userAge']
    # UserGender
    usergender = datasession['userGender']
    # UserPHQ9
    # userphq9 = datasession['userPhq9Score']
    # UserDeficiency
    # userdeficiency = datasession['userDeficiency']
    # UserMedication
    # usermedication = datasession['userMedication']

    stat = {'UserID': userid, 'User_Age': userage,
            'User_Gender': usergender}

    # df = pd.read_json(jsonFile, orient = 'index')
    df = pd.DataFrame.from_dict([stat])

    return df

# Function for looping across all files in a directory


def filesextract(dirname):
    os.chdir(dirname)

    # Remove existing .csv files
    for root, dirs, files in os.walk(dirname, topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics.csv') or\
               filename.endswith('statistics_user.csv') or\
               filename.endswith('emotion.csv'):
                os.remove(filename)

    # Loop across all files and create output.csv and statistics.csv
    # containing typingdata of all sessions in a day                
    os.chdir(os.path.abspath(dirname))
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            date = {}
            # Session-Keystrokes file 'timestamp.json'
            if filename.startswith('Emotion') and\
               filename.endswith('.json'):
                statistics = emotion(filename)
                tmp = str((os.path.basename(os.getcwd())))
                try1 = tmp.split('.')
                tmp = try1[2] + '-' + try1[1] + '-' + try1[0]
                date = {'Date': tmp}
                statistics.update(date)
                # Open .csv  file and append statistics 
                file_exists = os.path.isfile('./emotion.csv')
                with open('emotion.csv', 'a', newline='') as csvfile:
                    fieldnames = statistics.keys()        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(statistics)
            os.chdir(os.path.abspath(root))
            # Session-Keystrokes file 'timestamp.json'
            if (not filename.startswith('Emotion')) and \
               (not filename.startswith('RawData')) and\
               (not filename.startswith('Info')) and\
               filename.endswith('.json'):
                statistics = keystrokes(filename)
                tmp = str((os.path.basename(os.getcwd())))
                try1 = tmp.split('.')
                tmp = try1[2] + '-' + try1[1] + '-' + try1[0]
                date = {'Date': tmp}
                # print(date)
                statistics.update(date)
                # print(statistics)

                # Open .csv file and append statistics 
                file_exists = os.path.isfile('./statistics.csv')
                
                with open('statistics.csv', 'a', newline='') as csvfile:
                    fieldnames = statistics.keys()        
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(statistics)
            
    # Create statistics_user.csv by merging all .csv in folders below
    os.chdir(dirname)
    # Some variables need to be initialized
    flagstat = flagemotion = False
    pathstat = os.path.abspath('/home')
    pathemotion = os.path.abspath('/home/jason')
    for root, dirs, files in os.walk(dirname, topdown=False):
        os.chdir(dirname)
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics.csv'):
                data = pd.read_csv(filename)
                fieldnames = ['Keystrokes']
                dfstat = pd.DataFrame(data)
                pathstat = os.path.abspath(root)
                flagstat = True
            elif filename.endswith('emotion.csv'):
                data = pd.read_csv(filename)
                fieldnames = ['Mood', 'Physical_State']
                dfemotion = pd.DataFrame(data)
                dfemotion = dfemotion[['Mood', 'Physical_State']]
                pathemotion = os.path.abspath(root)
                flagemotion = True
            # 'statistics.csv' and 'emotion.csv' need to be from the
            # same folder 
            if pathstat == pathemotion and filename.endswith('.csv'):
                # one folder must have both 'emotion.csv' and
                # 'statistics.csv' to be considered for analysis
                if flagstat and flagemotion:
                    os.chdir(dirname)
                    df = pd.concat([dfstat, dfemotion], axis=1)
                    # Propagation to fill empty emotions
                    df = df.fillna(method='ffill')

                    # Open .csv file and append statistics
                    # Needed for header 
                    file_exists = os.path.isfile('./statistics_user.csv')
                    with open('statistics_user.csv', 'a', newline='') as csvfile:
                        fieldnames = ['Keystrokes', 'Date', 'Mood', 'Physical_State']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if not file_exists:
                            writer.writeheader()
                    df.to_csv('statistics_user.csv', mode='a', index=False,
                              header=False)

                    flagemotion = False
                    flagstat = False
            elif pathstat != pathemotion and filename.endswith('.csv'):
                # 'statistics.csv' is first accessed in every folder
                flagstat = False

# Function for looping across all users


def users(dirname):
    os.chdir(dirname)
    # Remove existing .csv files
    for root, dirs, files in os.walk(dirname, topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics.csv') or\
               filename.endswith('statistics_user.csv') or\
               filename.endswith('emotion.csv') or\
               filename.endswith('statistics_total.csv'):
                os.remove(filename)

    os.chdir(dirname)
    for root, dirs, files in os.walk(dirname, topdown=False):
        for dir in dirs:
            # Only user files
            if ('2020' not in dir) and ('2019' not in dir):
                os.chdir(os.path.join(root, dir))
                filesextract(os.path.join(root, dir))

    os.chdir(dirname)
    # Some variables need to be initialized
    flagstat = flaginfo = False
    pathstat = os.path.abspath('/home')
    pathinfo = os.path.abspath('/home/jason')
    for root, dirs, files in os.walk(dirname, topdown=False):
        for filename in files:
            os.chdir(os.path.abspath(root))
            if filename.endswith('statistics_user.csv'):
                dfstat = process(filename)
                pathstat = os.path.abspath(root)
                flagstat = True
            elif filename.endswith('Info.json'):
                dfinfo = info(filename)
                pathinfo = os.path.abspath(root)
                flaginfo = True
            # 'statistics_user.csv' and 'Info.json' need to be from the
            # same folder
            if pathstat == pathinfo:
                # one folder must have both 'Info.csv' and
                # 'statistics_user.csv' to be considered for analysis
                if flagstat and flaginfo:
                    os.chdir(dirname)
                    # Open .csv file and append total statistics
                    # Needed for header 
                    file_exists = os.path.isfile('./statistics_total.csv')
                    df = pd.concat([dfinfo, dfstat], axis=1)
                    # Propagation to fill empty emotions
                    df = df.fillna(method='ffill')
                    with open('statistics_total.csv', 'a', newline='') as csvfile:
                        fieldnames = ['UserID', 'User_Age', 'User_Gender',
                                      'Keystrokes_Mean', 'Happy',
                                      'Sad', 'Neutral', 'Stressed',
                                      'Postponing', 'undefined',
                                      'Sessions_Number',
                                      # 'term1', 'term2', 'term3', 'term4', 'term5'
                                      'sessions/day']        
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if not file_exists:
                            writer.writeheader()

                    df.to_csv('statistics_total.csv', mode='a', index=False,
                              header=False)

                    flagstat = False
                    flaginfo = False    
            elif pathstat != pathinfo: 
                # info.json is first accessed in every folder
                flaginfo = False
            
# Function for processing DataFrame of typing data


def process(csvfile):
    data = pd.read_csv(csvfile)
    df = pd.DataFrame(data)
    sessionsnumber = len(df)
    keystrokesmean = df['Keystrokes'].mean()
    happy = len(df[df['Mood'] == 'Happy']) + \
        len(df[df['Mood'] == 'Happy TIMEOUT'])
    sad = len(df[df['Mood'] == 'Sad']) + \
        len(df[df['Mood'] == 'Sad TIMEOUT'])
    neutral = len(df[df['Mood'] == 'Neutral']) + \
        len(df[df['Mood'] == 'Neutral TIMEOUT'])
    stressed = len(df[df['Mood'] == 'Stressed']) + \
        len(df[df['Mood'] == 'Stressed TIMEOUT'])
    postponing = len(df[df['Mood'] == 'Postponing']) + \
        len(df[df['Mood'] == 'Postponing TIMEOUT'])
    undefined = len(df[df['Mood'] == 'undefined']) + \
        len(df[df['Mood'] == 'undefined TIMEOUT'])
    # term1 = len(df[df['Date'].str.endswith('12.2018')]) + \
    #     len(df[df['Date'].str.endswith('01.2019')]) + \
    #     len(df[df['Date'].str.endswith('02.2019')])
    # term2 = len(df[df['Date'].str.endswith('03.2019')]) + \
    #     len(df[df['Date'].str.endswith('04.2019')]) + \
    #     len(df[df['Date'].str.endswith('05.2019')]) + \
    #     len(df[df['Date'].str.endswith('06.2019')])
    # term3 = len(df[df['Date'].str.endswith('07.2019')]) + \
    #     len(df[df['Date'].str.endswith('08.2019')]) + \
    #     len(df[df['Date'].str.endswith('09.2019')])
    # term4 = len(df[df['Date'].str.endswith('10.2019')]) + \
    #     len(df[df['Date'].str.endswith('11.2019')]) + \
    #     len(df[df['Date'].str.endswith('12.2019')])
    # term5 = len(df[df['Date'].str.endswith('01.2020')]) + \
    #     len(df[df['Date'].str.endswith('02.2020')]) + \
    #     len(df[df['Date'].str.endswith('03.2020')])
    sessionsperday = (sum(df['Date'].value_counts()) / df['Date'].nunique())
    
    statistics = {'Keystrokes_Mean': keystrokesmean, 'Happy': happy,
                  'Sad': sad, 'Neutral': neutral, 'Stressed': stressed,
                  'Postponing': postponing,
                  'Undefined': undefined, 'Sessions_Number': sessionsnumber,
                  # 'term1': term1, 'term2': term2, 'term3': term3,
                  # 'term4': term4, 'term5': term5
                  'sessions/day': sessionsperday}

    df = pd.DataFrame.from_dict([statistics])
    return df
