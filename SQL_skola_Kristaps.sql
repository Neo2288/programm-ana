insert or ignore into audzekni values("A_103","Aleksandrs","Plēsējs","12a",17,"01.09.2021",93.53);
insert or ignore into audzekni values("A_104","Māris","Žuks","12b",17,"01.10.2021",95.67);
select Audzekna_id, Vards, Uzvards, Klase, Vecums, Iestasanas_datums, Stipendija from audzekni;
select sum(Stipendija) from audzekni;
select max(Stipendija) from audzekni;
select avg(Vecums) from audzekni;
select min(Vecums) from audzekni;
select Vards, Uzvards, Stipendija from audzekni;