import csv


class Stock:
    """Represents a single stock and its financial ratios."""

    def __init__(self, ticker: str, price: float, book_ratio: float, eps: float):
        self.ticker     = ticker
        self.price      = price
        self.book_ratio = book_ratio
        self.eps        = eps

    @property
    def pe_ratio(self) -> float:
        """Price-to-Earnings ratio: price / eps."""
        return round(self.price / self.eps, 2)

    @property
    def pb_ratio(self) -> float:
        """Price-to-Book ratio: price / book_ratio."""
        return round(self.price / self.book_ratio, 2)

    def __repr__(self) -> str:
        return (f"Stock({self.ticker!r}, price={self.price}, "
                f"PE={self.pe_ratio}, PB={self.pb_ratio})")


class RatioCalculator:
    """Reads stock data from a CSV, computes ratios, and writes results."""

    def __init__(self, input_file: str, output_file: str):
        self.input_file  = input_file
        self.output_file = output_file
        self.stocks: list[Stock] = []

    def load(self) -> None:
        """Load stock rows from the input CSV."""
        with open(self.input_file, newline="") as f:
            for row in csv.DictReader(f):
                self.stocks.append(Stock(
                    ticker     = row["ticker"],
                    price      = float(row["price"]),
                    book_ratio = float(row["book_ratio"]),
                    eps        = float(row["eps"]),
                ))

    def save(self) -> None:
        """Write enriched rows (with PE_RATIO & PB_RATIO) to the output CSV."""
        fieldnames = ["ticker", "price", "book_ratio", "eps", "PE_RATIO", "PB_RATIO"]
        with open(self.output_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for s in self.stocks:
                writer.writerow({
                    "ticker":     s.ticker,
                    "price":      s.price,
                    "book_ratio": s.book_ratio,
                    "eps":        s.eps,
                    "PE_RATIO":   s.pe_ratio,
                    "PB_RATIO":   s.pb_ratio,
                })

    def report(self) -> None:
        """Print a summary to the console."""
        print(f"Done! {len(self.stocks)} rows written to {self.output_file}\n")
        print(f"  {'Ticker':<8} {'PE_RATIO':>10} {'PB_RATIO':>10}")
        print(f"  {'-'*8} {'-'*10} {'-'*10}")
        for s in self.stocks:
            print(f"  {s.ticker:<8} {s.pe_ratio:>10} {s.pb_ratio:>10}")

    def run(self) -> None:
        """Full pipeline: load → save → report."""
        self.load()
        self.save()
        self.report()


if __name__ == "__main__":
    calculator = RatioCalculator(
        input_file  = "../2_ratios/in.csv",
        output_file = "out.csv",
    )
    calculator.run()
