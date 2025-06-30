import pandas as pd

# Wczytaj oczyszczone dane
orders = pd.read_csv("orders_cleaned.csv")
returns = pd.read_csv("returns.csv")

# Łączenie danych, by ustalić, które zamówienia zostały zwrócone
orders["is_returned"] = orders["order_id"].isin(returns["order_id"])

# KPI 1: Średnia wartość zamówienia
avg_order_value = orders["total_amount"].mean()

# KPI 2: Liczba unikalnych klientów
unique_customers = orders["customer_id"].nunique()

# KPI 3: Zamówienia dziennie
orders_per_day = orders.groupby("order_date").size().mean()

# KPI 4: Współczynnik zwrotów
return_rate = orders["is_returned"].mean()

# KPI 5: Średnia wartość zwrotu
returns_merged = orders[orders["is_returned"]]
avg_return_value = returns_merged["total_amount"].mean()

# Zapisz KPI do CSV
kpi_data = {
    "avg_order_value": [round(avg_order_value, 2)],
    "unique_customers": [unique_customers],
    "avg_orders_per_day": [round(orders_per_day, 2)],
    "return_rate": [round(return_rate * 100, 2)],
    "avg_return_value": [round(avg_return_value, 2)]
}

kpi_df = pd.DataFrame(kpi_data)
kpi_df.to_csv("kpis.csv", index=False)

print("✅ KPIs saved to 'kpis.csv'")
