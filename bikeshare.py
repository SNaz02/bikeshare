import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'all':'all',
            'jan':1,
            'feb':2,
            'mar':3,
            'apr':4,
            'may':5,
            'jun':6}
day_data = {'all':'all',
            'sun':6,
            'mon':0,
            'tue':1,
            'wed':2,
            'thu':3,
            'fri':4,
            'sat':5}

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
    #Loops throughs until user provide correct value
    while True:
            city = input("Please enter the name of City: Valid options are Chicago, New york city or Washington [not case sensitive]:")
            city = city.lower()
            if(city!="chicago" and city!="new york city" and city!="washington"):
                print("Type in either 'Chicago' or 'New york city' or 'Washington'")
            else: 
                city = CITY_DATA[city]
                break
    # TO DO: get user input for month (all, january, february, ... , june)
    #Loops throughs until user provide correct value
    while True:
            month = input("Please enter the month for perform analysis: Valid options are All, Jan, Feb, Mar, Apr, May or Jun [not case sensitive]:")
            month = month.lower()
            if(month!="all" and month!="jan" and month!="feb" and month!="mar" and month!="apr" and month!="may"and month!="jun"):
                print("Type in either 'All', 'Jan', 'Feb', 'Mar', 'Apr', 'May' or 'Jun'")
            else:
                month = month_data[month]
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Loops throughs until user provide correct value
    while True:
            day = input("Please enter the day for perform analysis: Valid options are All, Sun, Mon, Tue, Wed, Thu, Fri or Sat [not case sensitive]:")
            day = day.lower()
            if(day!="all" and day!= 'sun' and day!="mon" and day!="tue" and day!="wed" and day!="thu" and day!="fri"and day!="sat"):
                print("Type in either 'All', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri' or 'Sat'")
            else:
                day = day_data[day]
                break
    print('-'*40)
    return city, month, day


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
    
    df=pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if(month!='all'):      
        df = df.loc[df['Start Time'].dt.month==month]
    if(day!='all'):
        df = df.loc[df['Start Time'].dt.dayofweek==day] 
        
  
    return df

def get_key(dict_list, val):
    key_value = list(dict_list.keys())[list(dict_list.values()).index(val)]
    return key_value

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month   
    common_month = df['Start Time'].dt.month.mode().get(key=0)
    common_month_value = get_key(month_data, common_month)
    print('\nMost Common Month')
    print(str(common_month_value).upper())
    
    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.dayofweek.mode().get(key=0)
    common_day_value = get_key(day_data, common_day)
    print('\nMost Common Day of Week')
    print(str(common_day_value).upper())    

    # TO DO: display the most common start hour
    common_st_hr = df['Start Time'].dt.hour.mode().get(key=0)
    print('\nMost Common Start Hour')
    print(common_st_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost Commonly Used Start Station')
    print(df['Start Station'].mode().get(key=0))

    # TO DO: display most commonly used end station
    print('\nMost Commonly Used End Station')
    print(df['End Station'].mode().get(key=0))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent combination of Start station and End station trip')
    print(df[['Start Station','End Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time (Minutes)')
    print((df['Trip Duration'].sum())/60)

    # TO DO: display mean travel time
    print('\nMean Travel Time (Minutes)')
    print((df['Trip Duration'].mean())/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nTrip counts by User Type')
    print(df['User Type'].value_counts())

    #Washington city does not have gender or birth year
    if(city!='washington.csv'):
        # TO DO: Display counts of gender
        print('\nTrip counts by Gender')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest Birth Year')
        print(int(df['Birth Year'].max()))
        print('\nMost recent Birth Year')
        print(int(df['Birth Year'].min()))
        print('\nMost Common Birth year')
        print(int(df['Birth Year'].mode().get(key=0)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Below function is to get input from user
def get_rawdata(data):
        max_rows = data.shape[0]
        start_row = 0
        end_row = 5
        while True:
            us_ip = input("Would you like to see the raw data(5 lines at a time): Options are Yes or No [not case sensitive]:")
            us_ip = us_ip.lower()
            if(us_ip!="yes" and us_ip!="no"):
                print("Type in either 'Yes' or 'No'")
            elif(us_ip=='yes'):
                if(end_row>max_rows):
                    end_row = max_rows
                print(data.iloc[start_row:end_row])
                if(end_row < max_rows):
                    start_row = end_row + 1
                    end_row = end_row + 6
                else:
                    print("End of data")
                    break
            else:
                break
                    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        get_rawdata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

			