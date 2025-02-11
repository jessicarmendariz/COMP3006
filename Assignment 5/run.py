from real_estate.load_data.load import RealEstate

def main():
    # Takes No Arguments and Instantiates the Real Estate Class
    # Prints First 5 Property Containers for Every State and Territory
    real_estate_data = RealEstate("realtor-data.csv", "real_estate/load_data/data")
    
    print("\n********** First 5 Properties by State and Territory **********\n")
    for category, states in real_estate_data.properties_dict.items():
        for state, properties in states.items():
            print(f"'{state}':")
            for prop in properties[:5]:
                print(f"  {prop}")  
            print()

    print("\n********** Real Estate Statistics **********\n")
    print(f"Cheapest Property in Delaware:\n", real_estate_data.compute_stats("cheapest", "Delaware"))
    print(f"Most Expensive Property in New York:\n", real_estate_data.compute_stats("priciest", "New York"))
    print(f"Absolute Cheapest Property in the US:\n", real_estate_data.compute_stats("dirt_cheap"))
    print(f"Best Deal in Puerto Rico (3B, 2Ba):\n", real_estate_data.compute_stats("best_deal", "Puerto Rico", 3, 2))
    print(f"Best Budget-Friendly Property (3B, 2Ba, Budget: $500,000):\n", real_estate_data.compute_stats("budget_friendly", 3, 2, 500000))

if __name__ == "__main__":
    main()
