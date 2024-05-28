import pandas as pd
import matplotlib.pyplot as plt


def excel():
    '''
    practice
    '''
    df = pd.read_excel('Sheet1.xlsx')
    print(df)
    print(df['Name'])
    print(df.loc[0,'Name'])
    print(df.iloc[0,0])


def my_data():
    '''
    practice
    '''
    data = {
        'Name': ['John', 'Anna', 'Mike'],
        'Age': [30, 22, 32],
        'City': ['New York', 'London', 'San Francisco']
    }
    df = pd.DataFrame(data)
    print(df)
    df['Name'] = ['Dmitriy', 'Veronika', 'Max']
    print(df)

    df = df.drop(columns=['City'])
    print(df)
    df = df.drop(index=0)
    print(df)

    df1 = pd.DataFrame({
        'Name': ['John', 'Anna', 'Mike'],
        'Age': [30, 22, 32]
    })

    df2 = pd.DataFrame({
        'Name': ['John', 'Anna', 'Mike'],
        'City': ['New York', 'London', 'San Francisco']
    })

    merged = pd.merge(df1, df2, on='Name')
    print(merged)

    df1 = pd.DataFrame({
        'Name': ['John', 'Anna'],
        'Age': [30, 22]
    })

    df2 = pd.DataFrame({
        'Name': ['Mike', 'Chris'],
        'Age': [32, 25]
    })

    concatenated = pd.concat([df1, df2])
    print(concatenated)

    data = {
        'Name': ['John', 'Anna', 'Mike', 'Chris'],
        'Age': [30, None, 32, 25],
        'City': ['New York', 'London', 'San Francisco', 'Boston']
    }

    df = pd.DataFrame(data)
    df.fillna({'Age': df['Age'].mean()}, inplace=True)
    print(df)


def task1():
    # Load data from sales.csv file into DataFrame.
    df = pd.read_csv("sales.csv")
    # Print the first 10 rows of the DataFrame.
    print(df.head(10))

    # Calculate the total number of sales (Quantity) for each product and display the results.
    total_sum = df.groupby('Product')['Quantity'].sum()
    print(total_sum)

    # Create a new Total column that will contain the total sales amount (quantity times price) for each row.
    df['Total'] = df['Quantity']*df['Price']
    print(df)

    # Calculate the total sales for each product and display the results.
    total_sum = df.groupby('Product')['Total'].sum()
    print(total_sum)


def task2():
    # Load data from students.csv file into DataFrame.
    df = pd.read_csv("students.csv")
    print(df)

    # Fill in the missing values in the Age column with the mean age value.
    df.fillna({'Age': df['Age'].mean()}, inplace=True)
    print(df)

    # Display a statistical summary of the Age column (minimum, maximum, average).
    print(df['Age'].describe)

    # Count the number of students in each city and display the results.
    student_per_city = df['City'].value_counts()
    print(student_per_city)

    # Find all students whose age is over 18 years old and display their names and cities.
    age = df[df['Age'] > 18][['Name', 'City']]
    print(age)


def task3():
    # Load data from weather.csv file into DataFrame.
    df = pd.read_csv('weather.csv')
    # Display information about the DataFrame (number of rows, columns, data types).
    print(df.info())

    # Find the city with the maximum average temperature and display its name and average temperature.
    max_avg_temperature = df.groupby('City')['Temperature'].mean().max()
    max_avg_temperature_city = df.groupby('City')['Temperature'].mean().idxmax()
    print(f'City: {max_avg_temperature_city} Temperature: {max_avg_temperature}')

    # Create a new DataFrame containing data only for the city with the lowest average
    # humidity and save it to a new CSV file min_humidity_city.csv.
    min_avg_humidity_city = df.groupby('City')['Humidity'].mean().idxmin()
    df1 = df[df['City'] == min_avg_humidity_city]
    df1.to_csv('min_avg_humidity_city', index=False)

    # Construct a graph of temperature changes by date for the city with the maximum average temperature.
    max_temp_city_df = df[df['City'] == max_avg_temperature_city]
    max_temp_city_df.plot(x='Date', y='Temperature', title=f'Temperature Changes in {max_avg_temperature_city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.show()


if __name__ == '__main__':
    #excel()
    #my_data()
    task1()
    task2()
    task3()
