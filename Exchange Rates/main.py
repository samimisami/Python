import dates
import exchangeRates
import extraction2excel

first_day, last_day, first_day_name=dates.getDates()

dataset = exchangeRates.get_euro_try_rates(first_day, last_day)

extraction2excel.extraction2excel(dataset, first_day_name)
