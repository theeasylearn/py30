-- 1. Create Product Table
CREATE TABLE Product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    description TEXT,
    weight DECIMAL(8,2),
    size VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create Bill Table
CREATE TABLE Bill (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255) NOT NULL,
    billdate DATE NOT NULL,
    mobile VARCHAR(15),
    amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    mode  int(1) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Create Item Table (with FOREIGN KEYS)
CREATE TABLE Item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    productid INT NOT NULL,
    qty INT NOT NULL DEFAULT 1,
    price DECIMAL(10,2) NOT NULL,
    billid INT DEFAULT 0
);

