CREATE DATABASE IF NOT EXISTS producthub;
USE producthub;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT
);

INSERT INTO products (name, price, description) VALUES
('Laptop', 59999.99, 'Powerful laptop for developers'),
('Wireless Mouse', 999.99, 'Smooth and responsive mouse'),
('Mechanical Keyboard', 3499.00, 'Tactile and clicky keyboard');
