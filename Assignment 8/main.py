from contents.babynames import BabyNames

if __name__ == "__main__":
    #Create the Instance of Baby Names
    baby_names = BabyNames()


#Test the Helper Functions
    #Test Sorting Function
    print("First 5 Rows of the Sorted Data Frame:")
    print(baby_names.names_df.head())

    #Plot Total Male and Female Births Per Year
    print("\n\n\nGenerating Male vs Female Births Plot...")
    baby_names.m_f_names()

    #Plot the Three Most Popular Names Ever
    print("\n\n\nGenerating Most Popular Names Plot...")
    baby_names.most_popular_ever()

    #Plot the Number of Unisex Names Over Time
    print("\n\n\nGenerating Unisex Names Over Time Plot...")
    baby_names.unisex()

    #Allow User to Explore Specific Unisex Names Over Time
    print("\n\n\nExploring Unisex Names Evolution...")
    baby_names.unisex_evolution()

    print("\n\n\nAnalysis Complete!")
