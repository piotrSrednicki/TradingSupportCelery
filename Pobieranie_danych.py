from FunkcjeDoDanych import scrap_data_indexes,scrap_data_announcements,scrap_data_pointers

symbols = ["ACTION"]
for symbol in symbols:
    # przynależności do indeksów
    indexes = scrap_data_indexes(symbol)
    # wskaźniki giełdowe
    pointers = scrap_data_pointers(symbol)
    # komunikaty
    announcements = scrap_data_announcements(symbol)
