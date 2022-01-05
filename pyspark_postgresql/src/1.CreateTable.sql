SET DATESTYLE TO PostgreSQL,European;



CREATE SEQUENCE IDVendedor;
CREATE TABLE Vendedores(
  IDVendedor int default nextval('IDVendedor'::regclass) PRIMARY KEY,
  Nome Varchar(50)
);

CREATE SEQUENCE IDProduto;
CREATE TABLE Produtos(
  IDProduto int default nextval('IDProduto'::regclass) PRIMARY KEY,
  Produto Varchar(100),
  Preco Numeric(10,2)
);

CREATE SEQUENCE IDCliente;
CREATE TABLE Clientes(
  IDCliente int default nextval('IDCliente'::regclass) PRIMARY KEY,
  Cliente Varchar(50),
  Estado Varchar(2),
  Sexo Char(1),
  Status Varchar(50)
);

CREATE SEQUENCE IDVenda;
CREATE TABLE Vendas(
  IDVenda int default nextval('IDVenda'::regclass) PRIMARY KEY,
  IDVendedor int references Vendedores (IDVendedor),
  IDCliente int references Clientes (IDCliente),
  Data Date,
  Total Numeric(10,2)
);

CREATE TABLE ItensVenda (
    IDProduto int REFERENCES Produtos ON DELETE RESTRICT,
    IDVenda int REFERENCES Vendas ON DELETE CASCADE,
    Quantidade int,
    ValorUnitario decimal(10,2),
    ValorTotal decimal(10,2),
	Desconto decimal(10,2),
    PRIMARY KEY (IDProduto, IDVenda)
);