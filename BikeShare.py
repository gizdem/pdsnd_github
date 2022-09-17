#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Reference: Udacity course notes

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df [df['month']== month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs

    #Reference: Udacity course notes
    while True:
        try:
            city = str(input('Please enter the city you would like to see the data of, Chicago, New York City or Washington?: ')).lower()
            break
        except ValueError:
            print('Unfortunately that\'s not a valid city name!')
            pass

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Now please enter the month you would like to see the data of: ')).lower()
            break
        except ValueError:
            print('Unfortunately that\'s not a valid month!')
            pass

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Lastly, please enter the day of week you would like to see the data of: ')).lower()
            break
        except ValueError:
            print('Unfortunately that\'s not a valid day_of_week!')
            pass

    print('-'*40)
    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Reference: Udacity course notes

    # display the most common month

    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular day of week:', popular_day_of_week)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Reference: Udacity course notes

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_startend_station = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip:', most_frequent_startend_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Reference: Udacity course notes

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ',total_travel_time/60, 'mins')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ',mean_travel_time/60, 'mins')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Reference: Udacity course notes

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('The total number of user types: ',counts_of_user_types)

    # Display counts of gender
    if 'Gender' in df:
        counts_of_gender = df['Gender'].value_counts()
        print('count of gender: ',counts_of_gender)

    else:
        print('There is no gender column in the data source')

    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        print('The earliest year of birth is: ',df['Birth Year'].min())
        print('The most recent year of birth is: ',df['Birth Year'].max())
        print('The most common year of birth is: ',df['Birth Year'].mode()[0])

    else:
        print('There is no birth year column in the data source')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Reference: Udacity course notes
def display_raw_data(df):

    number_of_lines_count = 0
    while True:

        answer = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        if answer != 'yes':
            break
        else:

            print(df.iloc[number_of_lines_count:number_of_lines_count+5])
            number_of_lines_count += 5


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:
