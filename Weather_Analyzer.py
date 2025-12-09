import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

file_path = "Sonya\weather_data.csv"
data = pd.read_csv(file_path)

data["Date"] = pd.to_datetime(data["Date"])

def calculate_statistics(data):
    print("Weather Stats")
    stats = data[["Temperature", "Humidity"]].describe()  # summary statistics
    print(stats)
    return stats


def calculate_average(data, column):
    if column in data.columns:
        return data[column].mean()
    else:
        raise ValueError(
            f"The column '{column}' doesn't exist in the data.")


def calculate_max(data, column):
    if column in data.columns:
        return data[column].max()
    else:
        raise ValueError(f"The column '{column}' is not in the data.")


def calculate_min(data, column):
    if column in data.columns:
        return data[column].min()
    else:
        raise ValueError(f"No column named '{column}' in the data.")


def visualize_data(data):
    # plot temperature and humidity over time
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Temperature"],
             label="Temperature (°C)", color="red")
    plt.plot(data["Date"], data["Humidity"],
             label="Humidity (%)", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.title("Temperature and Humidity Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # correlation heatmap for temperature and humidity
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        data[["Temperature", "Humidity"]].corr(), annot=True, cmap="coolwarm", fmt=".2f"
    )
    plt.title("Temperature vs Humidity: How Are They Related?")
    plt.show()


def simulate_temperature(data, increase_by):
    # simulate a temperature increase
    data[f"Temperature_Simulated_{increase_by}"] = data["Temperature"] + increase_by
    return data

def mark_hot_days(data):
    hot_days = []  # list to store if the day is hot or not
    for temp in data["Temperature"]:
        if temp > 30:
            hot_days.append("Hot Day")
        else:
            hot_days.append("Normal Day")

    data["Day Type"] = hot_days  # adding the result as a new column
    return data


# main Program
if __name__ == "__main__":
    calculate_statistics(data)
    print("Specific Weather Stats")
    avg_temp = calculate_average(data, "Temperature")
    print(f"Average Temperature: {avg_temp:.2f} °C")

    max_humidity = calculate_max(data, "Humidity")
    print(f"Maximum Humidity: {max_humidity:.2f} %")

    min_temp = calculate_min(data, "Temperature")
    print(f"Minimum Temperature: {min_temp:.2f} °C")

    # mark days as hot if the temperature is above 30°C
    data = mark_hot_days(data)
    print("Days Marked as 'Hot Day' or 'Normal Day'")
    print(
        data[["Date", "Temperature", "Day Type"]].head()
    )

    # visualizing the data
    print("\n=== Time to Visualize the Data ===")
    visualize_data(data)

    # simulating temperature increases
    increase_values = [
        1,
    ]  
    for increase in increase_values:
        data = simulate_temperature(data, increase)
        print(f"Simulated Temperature with +{increase}°C increase:")
        print(data[[f"Temperature_Simulated_{increase}"]].head())

    # plotting original vs simulated temperatures
    print("Comparing Original vs Simulated Temperatures")
    plt.figure(figsize=(12, 6))
    plt.plot(
        data["Date"],
        data["Temperature"],
        label="Original Temperature (°C)",
        color="red",
    )
    for increase in increase_values:
        plt.plot(
            data["Date"],
            data[f"Temperature_Simulated_{increase}"],
            linestyle="--",
            label=f"+{increase} °C Simulated",
        )
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Original vs Simulated Temperature Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # save all plots to PDF
    with PdfPages('weather_plots.pdf') as pdf:
        plt.figure(figsize=(12, 6))
        plt.plot(data["Date"], data["Temperature"],
                 label="Temperature (°C)", color="red")
        plt.plot(data["Date"], data["Humidity"],
                 label="Humidity (%)", color="blue")
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.title("Temperature and Humidity Over Time")
        plt.legend()
        plt.grid(True)
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(8, 6))
        sns.heatmap(data[["Temperature", "Humidity"]].corr(),
                    annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Temperature vs Humidity: How Are They Related?")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(12, 6))
        plt.plot(data["Date"], data["Temperature"],
                 label="Original Temperature (°C)", color="red")
        for increase in increase_values:
            plt.plot(
                data["Date"], data[f"Temperature_Simulated_{increase}"], linestyle="--", label=f"+{increase} °C Simulated")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.title("Original vs Simulated Temperature Over Time")
        plt.legend()
        plt.grid(True)
        pdf.savefig()
        plt.close()
