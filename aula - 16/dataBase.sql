CREATE DATABASE loja;

USE loja;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL (10,2),
    estoque INT
);


INSERT INTO produtos (nome, preco, estoque)
VALUES
('Camiseta', 59.90, 30),
('Calça Jeans',120, 15),
('Tênis', 250, 10);


SELECT * FROM produtos;

SELECT nome , preco FROM produtos;

SELECT nome FROM produtos where preco > 100 ;

UPDATE produtos 
SET estoque = 15
WHERE nome = 'Tênis';

SELECT * FROM produtos;