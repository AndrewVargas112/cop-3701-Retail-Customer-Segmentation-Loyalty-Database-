import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def feature1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.CustomerID, c.Year_Birth, cp.Email, cp.Phone
        FROM CUSTOMER c
        JOIN CONTACTPROFILE cp ON c.CustomerID = cp.CustomerID
    """)
    for row in cursor.fetchall():
        print(row)

def feature2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT CustomerID, CampaignID, AcceptedFlag
        FROM CUSTOMERCAMPAIGN
    """)
    for row in cursor.fetchall():
        print(row)

def feature3(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ca.CampaignName, cc.CustomerID
        FROM CAMPAIGN ca
        JOIN CUSTOMERCAMPAIGN cc
        ON ca.CampaignID = cc.CampaignID
    """)
    for row in cursor.fetchall():
        print(row)

def feature4(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.CustomerID, d.DependentType, d.DependentAge
        FROM CUSTOMER c
        JOIN CUSTOMERDEPENDENT d
        ON c.CustomerID = d.CustomerID
    """)
    for row in cursor.fetchall():
        print(row)

def feature5(conn):
    min_income = float(input("Enter minimum income: "))
    max_income = float(input("Enter maximum income: "))
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT CustomerID, Income
        FROM CUSTOMER
        WHERE Income BETWEEN ? AND ?
    """, (min_income, max_income))
    
    for row in cursor.fetchall():
        print(row)

def main():
    conn = connect_db()
    
    while True:
        print("\n--- MENU ---")
        print("1. View customers with contact info")
        print("2. View customer campaign participation")
        print("3. View campaigns and customers")
        print("4. View customers with dependents")
        print("5. Search customers by income")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            feature1(conn)
        elif choice == "2":
            feature2(conn)
        elif choice == "3":
            feature3(conn)
        elif choice == "4":
            feature4(conn)
        elif choice == "5":
            feature5(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()