import time
import pandas as pd
import numpy as np
import calendar
from datetime import date,datetime

#   this is tested submission code  SUBMISSION SAMPLE
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



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
    print('would you like to see data for Chicago, New York, or Washington?')
    city=""
    month=99
    day=99
    while True:
        city1=input()
        city=city1.lower().replace(" ","")
        if city=="chicago" or city=="newyork" or city=="washington":
            break

    print('would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.')
    filt=""
    while True:
        filt1=input()
        filt=filt1.lower().replace(" ","")
        if filt=="month" or filt=="day" or filt=="both" or filt=="none":
            break
            
        
    # TO DO: get user input for month (all, january, february, ... , june)
    if filt=="month" or filt=="both":
        print('which month? January, February, March, April, May, or June? enter month as integer eg..january=1')
        while True:
            month=int(input())
            if month==1 or month==2 or month==3 or month==4 or month==5 or month==6:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filt=="day" or filt=="both":
        print('which day? Please enter your response as an integer (e.g., 0=Monday 1=...soon ....5= 6=Sunday).')
        while True:
            day=int(input())
            if day>=0 and day<7:
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
    if city=="chicago" :
        fn="./chicago.csv"
    if city=="washington" :
        fn="./washington.csv"
    if city=="newyork" :
        fn="./new_york_city.csv"
    df1=pd.read_csv(fn)
    
    if month!=99 :
        month-=1
        temp1='2017-0'+str(month)+'01'
        month+=1
        temp2='2017-0'+str(month)+'01'
    
        df1=df1.where(df1['Start Time']>=temp1).where(df1['Start Time']<temp2)
    
        df1=df1.dropna(0)
    
    df1['Start Time']=pd.to_datetime(df1['Start Time'])
    
    if day != 99 :
        df12=df1['Start Time'].apply(f_fd2)
        df14=df1.where(df12==day).dropna()
    else :
        df14=df1.dropna()
    
    return df14



""" 
     my own functions <1>.
"""
def f_fd2(x):
    a=x.weekday()
    return a


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    
    # TO DO: display the most common month
    if month == 99 :
        df10=df['Start Time'].apply(f_m)
        
        t2=df10.values
        
        
        
        maxcout,maxcout_mon=-1,-1
        for i in range(1,13,1) :
            if maxcout<list(t2).count(i) :
                maxcout=list(t2).count(i)
                maxcout_mon=i
               
        
        print("Most  common month :",calendar.month_name[maxcout_mon]," Count :",maxcout)
    
        
    
        
    # TO DO: display the most common day of week
    if day == 99 :
        df20=df['Start Time'].apply(f_fd2)
        
        t3=df20.values
        maxcout,maxcout_day=-1,-1
        for i in range(0,7,1) :
            if maxcout<list(t3).count(i) :
                maxcout=list(t3).count(i)
                maxcout_day=i    
        print("Most common day of week :",calendar.day_name[maxcout_day]," Count :",maxcout)
        

    
    #TO DO: display the most common start hour
    
    df1=df['Start Time'].apply(f_h)
    
    t1=df1.values
    maxcout,maxcout_hour=-1,-1
    for i in range(0,24,1) :
        if maxcout<list(t1).count(i) :
            maxcout=list(t1).count(i)
            maxcout_hour=i
    
    
    
    print("Most popular hour: ",maxcout_hour,"  Count: ",maxcout)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def f_h(x):
    a=x.hour
    return a


def f_m(x):
    return x.month

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    
    a=df['Start Station'].value_counts()
    b=a.max()
    print("Most common Start Station and it's Count : ")      #,df.groupby('Start Station').count().max()[0])
    print(a.where(a==a[0]).dropna(),"\n")        #answered
    
    
    
    # TO DO: display most commonly used end station
    a1=df['End Station'].value_counts()
    b1=a1.max()
    print("Most common End Station and it's Count : ")      #,df.groupby('Start Station').count().max()[0])
    print(a1.where(a1==a1[0]).dropna(),"\n")
    
    
    
    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station and it's count : ")
    
    aaa=df.groupby(['Start Station', 'End Station']).count()
    print(aaa.where(aaa['End Time'].max()==aaa['End Time']).dropna()['Start Time'])           #answered
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    
    print("total travel time : ",df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("mean travel time : ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of user types : \n")
    print("Subscriber:",df['User Type'].where(df['User Type']=='Subscriber').count())
    print("Customer:",df['User Type'].where(df['User Type']=='Customer').count(),"\n \n")

    # TO DO: Display counts of gender
    if city != "washington" :
        print("Male:",df['Gender'].where(df['Gender']=='Male').count())
        print("Female:",df['Gender'].where(df['Gender']=='Female').count(),"\n \n")
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print("earliest Year of Birth : ",df['Birth Year'].min())
        print("most recent Year of Birth : ",df['Birth Year'].max())
    
    
        print("Most common Birth Year and it's Count :\n ",)     #,df.groupby('Start Station').count().max()[0])
        a1=df['Birth Year'].value_counts()
        b=a1.max()
        print(a1.where(a1==b).dropna())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dis_play(df) :
    n=0
    while True :
        te=input("\n Would you like to see raw data? Enter yes or no.\n")
        if te.lower() != 'yes':
            break    
        print(df.iloc[n:n+5,:])#,"\n",df.loc[n+1,:],"\n",df.loc[n+2,:],"\n",df.loc[n+3,:],"\n",df.loc[n+4,:],"\n")
        n+=5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        ######                 print(df)   #data is loaded now
        dis_play(df)
        time_stats(df,month,day)
        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
