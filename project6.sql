CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    City VARCHAR(50),
    Country VARCHAR(50)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers VALUES
(1, 'John', 'Smith', 'New York', 'USA'),
(2, 'Jane', 'Smiley', 'Chicago', 'USA'),
(3, 'Kwame', 'Mensah', 'Accra', 'Ghana'),
(4, 'Akosua', 'Boateng', 'Kumasi', 'Ghana');

INSERT INTO Products VALUES
(1, 'iPhone 14', 'Electronics', 999.99),
(2, 'Samsung Galaxy Phone', 'Electronics', 899.99),
(3, 'Dell Laptop', 'Computers', 1200.00),
(4, 'Headphones', 'Accessories', 199.99);

INSERT INTO Orders VALUES
(1, 1, 1, '2026-05-01', 2),
(2, 2, 2, '2026-05-02', 1),
(3, 3, 3, '2026-05-03', 1),
(4, 4, 4, '2026-05-04', 3);

SELECT DISTINCT FirstName, LastName, City
FROM Customers
WHERE LastName LIKE 'Sm%'
  AND Country = 'USA'
ORDER BY City ASC, LastName DESC;

SELECT DISTINCT ProductName, Price
FROM Products
WHERE ProductName LIKE '%Phone%'
  AND Price < 1000
ORDER BY Price ASC;

SELECT DISTINCT c.FirstName, c.LastName, p.ProductName, o.Quantity
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN Products p ON o.ProductID = p.ProductID
WHERE p.ProductName LIKE '%Phone%'
ORDER BY o.Quantity DESC;
