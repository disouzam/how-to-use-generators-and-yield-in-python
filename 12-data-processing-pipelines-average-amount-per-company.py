file_name = "data/techcrunch.csv"

# Get lines of a CSV file
lines = (line for line in open(file_name))

# Process those lines to get a list of values per column
list_line = (s.rstrip().split(",") for s in lines)

# Get column names from header line
cols = next(list_line)

# Generates one dictionary per company with their data
company_dicts = (dict(zip(cols, data)) for data in list_line)

# Gets the raised amount per company
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

funding_materialized = [cf for cf in funding]
print(funding_materialized)

# Sum the raised amount per company
total_series_a = sum(funding_materialized)

# Average raised amount per company
average = total_series_a / len(funding_materialized)

print(f"Total series A fundraising: ${total_series_a}")
print(f"Average amount per company was {average:.2f}")