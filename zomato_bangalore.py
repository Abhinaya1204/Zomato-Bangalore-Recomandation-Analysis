# Zomato Bangalore Recommendation Analysis
# Modified version for Anaconda (No Google API required)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from collections import Counter, OrderedDict

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("Model/indian_restaurants_details_cleaned_data.csv")

# ===============================
# Famous Cuisines Function
# ===============================

def find_famous_cusines(data_frame, title, min_no_of_cusines):
    cusines = data_frame['cusine'].dropna()
    all_cus = []

    for cusine in cusines:
        temp = cusine.split(',')   # ✅ typo fixed
        for t in temp:
            all_cus.append(t.strip().lower())

    cus_counter = dict(Counter(all_cus))

    cus_list = []
    cou_list = []

    for key, value in sorted(cus_counter.items(), key=lambda item: item[1], reverse=True):
        if value > min_no_of_cusines:
            cus_list.append(key)
            cou_list.append(value)

    sns.set(style="whitegrid")
    plt.figure(figsize=(15,10))
    sns.barplot(x=cou_list, y=cus_list)
    plt.xlabel("Number of restaurants")
    plt.title(title)
    plt.show()


# ===============================
# Famous cuisines in Bangalore
# ===============================

df_bangalore = df[df.city == "Bengaluru"]
find_famous_cusines(df_bangalore, "Famous cuisines in Bangalore", 200)


# ===============================
# Restaurant Distribution Pie Chart
# ===============================

restaurant_chains = df.city.value_counts()[:10]

plt.figure(figsize=(12,8))
plt.pie(restaurant_chains.values,
        labels=restaurant_chains.index,
        autopct='%1.1f%%',
        startangle=90)
plt.title("Restaurant distribution of top Cities in India")
plt.show()


# ===============================
# Famous Restaurant Chains
# ===============================

def find_famous_restaurant_chains(title, data):
    restaurant_chains = data.name.value_counts()[:20]

    plt.figure(figsize=(12,8))
    sns.barplot(x=restaurant_chains.values,
                y=restaurant_chains.index)
    plt.xlabel("Number of outlets")
    plt.title(title)
    plt.show()


find_famous_restaurant_chains("Famous restaurant chains in Bangalore", df_bangalore)


# ===============================
# Rating Distribution
# ===============================

plt.figure(figsize=(12,8))
sns.histplot(df.rating.dropna(), bins=30, kde=True)
plt.xlabel("Restaurant Rating")
plt.title("Rating Distribution")
plt.show()


# ===============================
# Cost Distribution
# ===============================

plt.figure(figsize=(12,8))
sns.boxplot(y=df.cost_for_two.dropna())
plt.title("Cost Distribution (Box Plot)")
plt.show()


# ===============================
# Online Orders in Bangalore
# ===============================

online_orders = df_bangalore.online_order.value_counts()

plt.figure(figsize=(8,8))
plt.pie(online_orders.values,
        labels=["Yes", "No"],
        autopct='%1.1f%%')
plt.title("Restaurants Accepting Online Orders - Bangalore")
plt.show()


# ===============================
# Table Reservation
# ===============================

table_reserve = df_bangalore.table_reservation.value_counts()

plt.figure(figsize=(8,8))
plt.pie(table_reserve.values,
        labels=["Yes", "No"],
        autopct='%1.1f%%')
plt.title("Restaurants Accepting Table Reservation - Bangalore")
plt.show()


# ===============================
# Delivery Only Restaurants
# ===============================

delivery_only = df_bangalore.delivery_only.value_counts()

plt.figure(figsize=(8,8))
plt.pie(delivery_only.values,
        labels=["Yes", "No"],
        autopct='%1.1f%%')
plt.title("Delivery Only Restaurants - Bangalore")
plt.show()

print("Analysis Completed Successfully ✅")