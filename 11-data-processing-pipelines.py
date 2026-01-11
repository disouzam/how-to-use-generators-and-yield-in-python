file_name = "data/techcrunch.csv"
lines = (line for line in open(file_name))
print(lines)
list_line = (s.rstrip().split(",") for s in lines)
print(list_line)
cols = next(list_line)
print(cols)
company_dicts = (dict(zip(cols, data)) for data in list_line)
print(company_dicts)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
print(funding)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")