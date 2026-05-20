import csv

INPUT_FILE  = "in.csv"
OUTPUT_FILE = "out.csv"

rows = []

with open(INPUT_FILE, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ["PE_RATIO", "PB_RATIO"]

    for row in reader:
        price      = float(row["price"])
        eps        = float(row["eps"])
        book_ratio = float(row["book_ratio"])

        row["PE_RATIO"] = round(price / eps,        2)
        row["PB_RATIO"] = round(price / book_ratio, 2)

        rows.append(row)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Done! {len(rows)} rows written to {OUTPUT_FILE}")
for r in rows:
    print(f"  {r['ticker']:6s}  PE={r['PE_RATIO']:>8}  PB={r['PB_RATIO']:>8}")
