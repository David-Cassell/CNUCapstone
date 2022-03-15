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
    
);