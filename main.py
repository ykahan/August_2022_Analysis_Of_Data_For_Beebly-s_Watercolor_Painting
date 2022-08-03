import pandas

piano_df = pandas.read_csv("Data/Piano.csv")
ultracart_df = pandas.read_csv("Data/Ultracart.csv")
bluesnap_df = pandas.read_csv("Data/Bluesnap.csv")
new_piano_df = pandas.read_csv("Data/Access-report---2022-08-03-08_08.csv")

num_piano_entries = len(piano_df)
num_new_piano_entries = len(new_piano_df)
num_ultracart_entries = len(ultracart_df)
num_bluesnap_entries = len(bluesnap_df)
num_total_entries = num_bluesnap_entries + num_ultracart_entries + num_piano_entries + num_new_piano_entries

piano_keys = piano_df.keys()
new_piano_keys = new_piano_df.keys()
ultracart_keys = ultracart_df.keys()
bluesnap_keys = bluesnap_df.keys()


# print(f"Piano has {len(piano_keys)} keys.\n"
#       f"New Piano has {len(new_piano_keys)} keys.\n"
#       f"Ultracart has {len(ultracart_keys)} keys.\n"
#       f"Bluesnap has {len(bluesnap_keys)} keys.")

print(f"Piano has {num_piano_entries} rows\n"
      f"New Piano has {num_new_piano_entries} rows.\n"
      f"Ultracart has {num_ultracart_entries} rows.\n"
      f"Bluesnap has {num_bluesnap_entries} rows.\n"
      f"There are {num_total_entries} total rows.")

print("\n")

unique_emails_new_piano = []
unique_emails_piano = []
unique_emails_ultracart = []
unique_names_bluesnap = []
total_unique_emails = []

for index, row in new_piano_df.iterrows():
      email = row["User Email"]
      if email not in unique_emails_new_piano:
            unique_emails_new_piano.append(email)

for index, row in piano_df.iterrows():
      email = row["Customer"]
      if email not in unique_emails_piano:
            unique_emails_piano.append(email)


for index, row in bluesnap_df.iterrows():
      name = row['Shopper First Name'] + row['Shopper Last Name']
      if name not in unique_names_bluesnap:
            unique_names_bluesnap.append(name)


for index, row in ultracart_df.iterrows():
      if row["Email"] not in unique_emails_ultracart:
            unique_emails_ultracart.append(row["Email"])


for email in unique_emails_ultracart:
      total_unique_emails.append(email)

for email in unique_emails_piano:
      if email not in unique_emails_ultracart and email not in unique_emails_new_piano and email not in total_unique_emails:
            total_unique_emails.append(email)


for email in unique_emails_new_piano:
      if email not in unique_emails_ultracart and email not in total_unique_emails and email not in unique_emails_piano:
            total_unique_emails.append(email)

num_unique_emails_piano = len(unique_emails_piano)
num_unique_emails_new_piano = len(unique_emails_new_piano)
num_unique_emails_ultracart = len(unique_emails_ultracart)
num_unique_names_bluesnap = len(unique_names_bluesnap)
num_total_unique_emails = len(total_unique_emails)

percent_uniques_piano = num_unique_emails_piano / num_piano_entries
percent_uniques_new_piano = num_unique_emails_new_piano / num_new_piano_entries
percent_uniques_ultracart = num_unique_emails_ultracart / num_ultracart_entries
percent_uniques_bluesnap = num_unique_names_bluesnap / num_bluesnap_entries
percent_uniques_total_emails = (num_total_unique_emails + num_unique_names_bluesnap) / num_total_entries

print(f"Uniques percentage is {percent_uniques_total_emails * 100}%")

print(f"New Piano has {num_unique_emails_new_piano} unique emails.\n"
      f"Piano has {num_unique_emails_piano} unique emails.\n"
      f"Bluesnap has {num_unique_names_bluesnap} unique names.\n"
      f"Ultracart has {num_unique_emails_ultracart} unique emails.\n"
      f"There are {num_total_unique_emails} total unique emails.")

