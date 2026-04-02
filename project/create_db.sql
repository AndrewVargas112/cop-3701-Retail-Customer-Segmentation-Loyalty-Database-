
DROP TABLE CustomerCampaign;
DROP TABLE CustomerDependent;
DROP TABLE ContactProfile;
DROP TABLE Campaign;
DROP TABLE Customer;

-- Customer Table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Year_Birth INT,
    Education VARCHAR(50),
    Marital_Status VARCHAR(20),
    Income DECIMAL(10,2),
    Dt_Customer DATE,
    Recency INT,
    Complain BOOLEAN
);

-- ContactProfile (1:1 with Customer)
CREATE TABLE ContactProfile (
    CustomerID INT PRIMARY KEY,
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(100),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Campaign Table
CREATE TABLE Campaign (
    CampaignID INT PRIMARY KEY,
    CampaignName VARCHAR(100),
    StartDate DATE,
    EndDate DATE
);

-- CustomerDependent (Weak Entity)
CREATE TABLE CustomerDependent (
    CustomerID INT,
    DependentID INT,
    DependentType VARCHAR(50),
    DependentAge INT,
    PRIMARY KEY (CustomerID, DependentID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- CustomerCampaign (M:N relationship)
CREATE TABLE CustomerCampaign (
    CustomerID INT,
    CampaignID INT,
    AcceptedFlag BOOLEAN,
    ResponseDate DATE,
    PRIMARY KEY (CustomerID, CampaignID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (CampaignID) REFERENCES Campaign(CampaignID)
);