create schema sistaerobd;

use sistaerobd;

create table Companhias(
cnpj varchar(18) not null,
nome varchar(300) not null,
contato varchar(300),
primary key (cnpj)
);

create table Aeroportos(
idAeroporto int not null auto_increment,
nome varchar(300) not null,
endereco varchar(300),
primary key (idAeroporto)
);

create table Passageiros(
cpf varchar(14) not null,
nome varchar(300) not null,
telefone varchar(14) not null,
email varchar(300) not null,
passaporte varchar(8) not null,
dataNascimento date not null,
primary key (cpf)
);

create table Voo(
numeroVoo int not null auto_increment,
dataHoraEmbarque datetime not null,
dataHoraDesembarque datetime not null,
portalEmbarque varchar(2) not null,
terminalEmbarque int not null,
portalDesembarque varchar(2) not null,
terminalDesembarque int not null,
fk_idAeroporto_origem int not null,
fk_idAeroporto_destino int not null,
fk_cnpj varchar(18) not null,
primary key (numeroVOO),
foreign key (fk_idAeroporto_origem) references aeroportos (idAeroporto),
foreign key (fk_idAeroporto_destino) references aeroportos (idAeroporto),
foreign key (fk_cnpj) references companhias (cnpj)
);

create table passageiros_Voos(
fk_cpf varchar(14) not null,
fk_numeroVoo int not null,
assento varchar(4) not null,
numeroReserva int not null,
primary key (fk_numeroVoo, fk_cpf),
foreign key (fk_numeroVoo) references voo (numeroVoo),
foreign key (fk_cpf) references passageiros (cpf)
);