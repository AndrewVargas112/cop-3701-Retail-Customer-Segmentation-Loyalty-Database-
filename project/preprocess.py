import csv
import random
from datetime import datetime, timedelta

NUM_CUSTOMERS = 120

# Generate Customers
with open("data/customer.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CustomerID","Year_Birth","Education","Marital_Status","Income","Dt_Customer","Recency","Complain"])
    
    for i in range(1, NUM_CUSTOMERS+1):
        writer.writerow([
            i,
            random.randint(1970, 2000),
            random.choice(["Bachelor","Master","PhD"]),
            random.choice(["Single","Married"]),
            random.randint(30000, 100000),
            "2022-01-01",
            random.randint(1, 50),
            random.choice([True, False])
        ])

# ContactProfile
with open("data/contactprofile.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CustomerID","Email","Phone","Address"])
    
    for i in range(1, NUM_CUSTOMERS+1):
        writer.writerow([
            i,
            f"user{i}@email.com",
            f"555-{1000+i}",
            random.choice(["NY","CA","TX","FL"])
        ])

# Campaign
campaigns = [
    (1, "Summer Sale", "2023-06-01", "2023-06-30"),
    (2, "Black Friday", "2023-11-20", "2023-11-27"),
    (3, "Winter Sale", "2023-12-01", "2023-12-31")
]

with open("data/campaign.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CampaignID","CampaignName","StartDate","EndDate"])
    writer.writerows(campaigns)

# CustomerDependent
with open("data/customerdependent.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CustomerID","DependentID","DependentType","DependentAge"])
    
    for i in range(1, NUM_CUSTOMERS+1):
        for d in range(random.randint(0,2)):
            writer.writerow([
                i,
                d+1,
                random.choice(["Child","Spouse"]),
                random.randint(1, 50)
            ])

# CustomerCampaign
with open("data/customercampaign.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CustomerID","CampaignID","AcceptedFlag","ResponseDate"])
    
    for i in range(1, NUM_CUSTOMERS+1):
        for c in [1,2,3]:
            writer.writerow([
                i,
                c,
                random.choice([True, False]),
                "2023-06-10"
            ])