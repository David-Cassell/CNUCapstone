drop database if exists capstone;
create database capstone;
use capstone;

drop table if exists patient;
drop table if exists breast;
drop table if exists bladder;
drop table if exists colon;
drop table if exists lung;
drop table if exists prostate;



create table Patient(
	pGender varchar(20),
    pID int,
    hospitalName varchar(20),
    hospitalAddress varchar(1000),
    primary key (pID)
);

create table breast(
	patientID int,
	breastClass varchar(15),
    breastTValue varchar(15),
    breastGrade varchar(15),
    breastMets varchar(15),
    breastLymph varchar(15),
    breastER varchar(15),
    breastHER2 varchar(15),
    breastPER varchar(15),
    breastStage varchar(15),
    foreign key(patientID) references patient (pID)
);

create table bladder(
	patientID int,
	bladderClass varchar(5),
    bladderTValue varchar(15),
    bladderMets varchar(15),
    bladderLymph varchar(15),
    bladderStage varchar(15),
    foreign key(patientID) references patient (pID)
);

create table colon(
	patientID int,
	colonClass varchar(5),
    colonTValue varchar(15),
    colonMets varchar(15),
    colonLymph varchar(15),
    colonStage varchar(15),
    foreign key(patientID) references patient (pID)
);

create table lung(
	patientID int,
	lungClass varchar(5),
    lungTValue varchar(15),
    lungMets varchar(15),
    lungLymph varchar(15),
    lungStage varchar(15),
    foreign key(patientID) references patient (pID)
);

create table prostate(
	patientID int,
	prostateClass varchar(5),
    prostateTValue varchar(15),
    prostateMets varchar(15),
    prostateLymph varchar(15),
    prostatePSA varchar(15),
    prostateGleason varchar(15),
    prostateStage varchar(15),
    foreign key(patientID) references patient (pID)
);