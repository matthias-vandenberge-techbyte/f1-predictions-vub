from data_fetcher import F1DataFetcher

def main():
    fetcher = F1DataFetcher()
    df = fetcher.fetch_all_data()
    
    print("Data succesvol opgehaald")
    print(df)

if __name__ == "__main__":
    main()