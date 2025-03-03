import pandas as pd
import matplotlib.pyplot as plt
from contents.helper_functions.hf import retrieve_files, record_loader_gen

#Contains 6 Methods:
    #1. __init__
    #2. sort_data
    #3. m_f_names
    #4. most_popular_ever
    #5. unisex
    #6. unisex_evolution
class BabyNames:
    def __init__(self):
        #Takes No Arguments and Creates a Pandas Data Frame Attribute
        file_list = retrieve_files(".txt") 
        records = list(record_loader_gen(file_list)) 
        self.names_df = pd.DataFrame(records, columns=["Name", "Gender", "Births", "Year"])
        self.sort_data()

    def sort_data(self):
        #Takes No Arguments, Sorts the DataFrame in Ascending Order By Year
        self.names_df.sort_values(by="Year", inplace=True)

    #Calculates the Total Number of Male and Female Births for Each Year and Creates a Line Plot Chart
    def m_f_names(self, start_year=1880, end_year=2022):
        #Args: Starting Year with Default Values of 1880 to 2022
        df_filtered = self.names_df[(self.names_df["Year"] >= start_year) & 
                                    (self.names_df["Year"] <= end_year)]
        yearly_counts = df_filtered.groupby(["Year", "Gender"])["Births"].sum().unstack()
        plt.figure(figsize=(10, 5))
        plt.plot(yearly_counts.index, yearly_counts["M"], label="Male", linestyle="-")
        plt.plot(yearly_counts.index, yearly_counts["F"], label="Female", linestyle="--")
        plt.xlabel("Year")
        plt.ylabel("Total Births")
        plt.title("Total Male and Female Births per Year")
        plt.legend()
        plt.show()

    #Calculates the Top 3 Most Popular Names Throughout History and Plots Evolution on a Chart
    def most_popular_ever(self):
        #Takes No Arguments, Returns a Chart
        top_names = self.names_df.groupby("Name")["Births"].sum().nlargest(3).index
        df_top = self.names_df[self.names_df["Name"].isin(top_names)]

        plt.figure(figsize=(10, 5))
        for name in top_names:
            name_df = df_top[df_top["Name"] == name].groupby("Year")["Births"].sum()
            plt.plot(name_df.index, name_df.values, label=name)
        plt.xlabel("Year")
        plt.ylabel("Total Births")
        plt.title("Top 3 Most Popular Names Over Time")
        plt.legend()
        plt.show()


    #Calculates Total Number of Births for Each Name for Each Year and Creates a Chart
    def unisex(self):
        #Takes No Arguments, Returns a Chart
        unisex_counts = self.names_df.groupby(["Year", "Name"])["Gender"].nunique()
        unisex_counts = unisex_counts[unisex_counts == 2].reset_index().groupby("Year").size()
        plt.figure(figsize=(10, 5))
        plt.bar(unisex_counts.index, unisex_counts.values, color="purple")
        plt.xlabel("Year")
        plt.ylabel("Number of Unisex Names")
        plt.title("Number of Unisex Names Over Time")
        plt.tick_params(axis='x', which='major', labelsize=7)
        plt.show()

    #Adds Every Name For Men and Women and Creates a Set
    #Verifies the User Entered a Valid Name Before Storing
    #Plots Total Number of Births Over the Years for Each Name From the User
    def unisex_evolution(self):
        #Prints The Set And Asks the User to Pick As Many Names As They Want Until They 'Q' 
        unisex_names = self.names_df.groupby(["Name"])["Gender"].nunique()
        unisex_names = set(unisex_names[unisex_names == 2].index)

        print("Available Unisex Names:", unisex_names)
        selected_names = []
        while True:
            name = input("Enter a name to analyze (or 'q' to quit): ").strip()
            if name == "q":
                break
            if name in unisex_names:
                selected_names.append(name)
            else:
                print("Invalid name. Please select from the list.")

        if selected_names:
            plt.figure(figsize=(10, 5))
            for name in selected_names:
                name_df = self.names_df[self.names_df["Name"] == name].groupby("Year")["Births"].sum()
                plt.plot(name_df.index, name_df.values, label=name)

            plt.xlabel("Year")
            plt.ylabel("Total Births")
            plt.title("Selected Unisex Names Over Time")
            plt.legend()
            plt.show()
        else:
            print("No Names Were Selected.")