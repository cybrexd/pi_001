create database pi_01;

use pi_01;

SET GLOBAL local_infile=1;
show global variables like "local_infile";
drop table if exists sucursal;

create table if not exists sucursal(
id varchar(255),
comercioid int ,
banderaId int ,
banderaDescripcion varchar(250),
comercioRazonSocial varchar(250),
provincia varchar(250),
localidad varchar(250),
direccion varchar(250),
lat varchar(250),
lng varchar(250),
sucursalNombre Varchar(250),
sucursalTipo Varchar(250),
primary key(id)
) engine=InnoDB default charset=utf8mb4 collate=utf8mb4_spanish_ci; 

LOAD DATA LOCAL INFILE "C://Users//elpep//Desktop//etl//Datasets relevamiento precios//sucursal.csv"
INTO TABLE `sucursal` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

select * from sucursal

drop table if exists producto;

create table if not exists producto(
id varchar(20),
marca varchar(100),
nombre varchar(200),
primary key(id)
) engine=InnoDB default charset=utf8mb4 collate=utf8mb4_spanish_ci;

LOAD DATA LOCAL INFILE "C://Users//elpep//Desktop//etl//Datasets relevamiento precios//producto.csv"
INTO TABLE `producto` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

select * from producto

drop table if exists precio_semana;

create table if not exists precio_semana(
precio float,
producto_id varchar(250),
sucursal_id varchar(250),
fecha date
)
select * from precio_semana

#querry requerida

select AVG(precio) as promedio
	from precio_semana where sucursal_id = "9-1-688" 

