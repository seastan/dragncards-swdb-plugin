import json
import csv

data = json.load(open("/home/cstanford@novateur.com/Firefox/swdbg_standard.json", "r", encoding="utf-8"))

# Define output filename
output_file = "standard_cards_cardtable.tsv"

# Collect all possible field names
fieldnames = ["Deck", "Title", "Code", "FrontImage", "BackImage", "Type", "ScenarioDeck", "CardSize", "Quantity"]

# Write TSV file
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    for card in data["Cards"]:
        writer.writerow({field: card.get(field, "") for field in fieldnames})

print(f"TSV file written to {output_file}")
