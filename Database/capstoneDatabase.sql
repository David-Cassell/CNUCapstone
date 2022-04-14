create table hospital(
	hName varchar(20),
    hAddress varchar(20)
);

create table Patient(
	-- 0 is female, 1 is male
	pGender binary,
    pId int
);

create table breast(
	breastClinorPath binary, -- 0 is Clin, 1 is Path
	breastSize decimal,
    breastLocation varchar(15),
    breastTValue varchar(15),
    breastGrade varchar(15),
    breastMetastasis varchar(15),
    breastLymphNode varchar(15),
    breastER binary,
    breastHER2 binary,
    breastPER binary,
    breastStage varchar(15)
);

create table bladder(
	bladderClinorPath binary,
    bladderTValue varchar(15),
    bladderMetastasis varchar(15),
    bladderLymnpNode varchar(15),
    bladderStage varchar(15)
);

create table colon(
	colonClinorPath binary,
    colonTValue varchar(15),
    colonMetastasis varchar(15),
    colonLymphNode varchar(15),
    colonStage varchar(15)
);

create table lung(
	lungClinorPath binary,
    lungTValue varchar(15),
    lungMetastasis varchar(15),
    lungLymphNode varchar(15),
    lungStage varchar(15)
);

create table prostate(
	prostateClinorPath binary,
    prostateTValue varchar(15),
    prostateMetastasis varchar(15),
    prostateLymphNode varchar(15),
    prostatePSA varchar(15),
    prostateGleason varchar(15)
);