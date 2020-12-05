import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
                city = input('Which city you like to explore? Chicago ,New York  or Washington?\n').title()
                if city in (CITY_DATA.keys()):
                    break
                else:
                    print('City is not in the list please select Chicago, New York, or Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
           month = input('Please enter month from January to June that you would like to analyze the data\n You Can Use All for all months:\n').lower()
           if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
               break
           else:
               print('Month is not from Jan to Jun please enter January, February, March, April, May, June or All')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
           day = input('please enter the day of the week that you would like to analyze the data\n You Can Use All for no filter:\n').title()
           if day in ('Saturday', 'Sunday' 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','All'):
               break
           else:
               print('Day is not correct please enter Saturday, Sunday,Monday, Tuesday, Wednesday, Thursday, Friday Use All for all days')

    print('-'*40)
    return city, month, day

def load_data(c, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
   df = pd.read_csv(CITY_DATA[city])
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[c])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':

        List = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = List.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\n Most common month',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\n Most common day of the week',common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\n Most common hour',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = str(df['Start Station'].mode()[0])
    print('\n Most common start station',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = str(df['End Station'].mode()[0])
    print('\n Most common end station',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = (df['Start Station'] + '+' + df['End Station'])
    common_combination_station = str(df['Station Combination'].mode()[0])
    print('\n Most Combination of start station and end station trip',common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ("\n Total travel time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ("\n Mean travel time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].value_counts()
    print ('\nCounts of user types:  ', user)


      # TO DO: Display counts of gender
    try:
        gender = str(df['Gender'].value_counts())
        print('\ncounts of gender:',gender)
    except KeyError:
        print('\nThere is no data for gender in the selected City')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = str(int(df['Birth Year'].min()))
        print('\nEarliest Year: ',earliest_year)
        recent_year = str(int(df['Birth Year'].max()))
        print('\nRecent Year: ',recent_year)
        common_year = str(int(df['Birth Year'].mode()[0]))
        print('\nCommon Year: ',common_year)
    except KeyError:
        print('\nThere is no data for birth year in the selected City')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
        row = 0
        flag = input('\nDo you need to see the first 5 rows of the data? Enter yes or no\n').lower()
        while flag == 'yes':
            #top_five_data = df.head(row+5)
            #print(top_five_data)
            print(df[row:row+5])
            row += 5
            flag = input('\nDo you need to see more 5 rows data? Enter yes or no\n').lower()
        else:
            print('\n Done!! No more rows needed to diplay')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
