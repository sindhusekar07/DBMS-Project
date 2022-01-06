use covidVaccine_656;
drop table if exists preExistingConditions;
drop table if exists patientResults;
drop table if exists patientOutcomes;
drop table if exists symptomDetails;
drop table if exists vaccineDetails;
drop table if exists dateRecords;
drop table if exists patientDetails;



CREATE TABLE patientDetails (vaersID int primary key,
			 ageInYears decimal (4,2) default null,
             cageInYears decimal (4,2) default null,
             cageInMonth decimal(4,2) default null,
             sex char(2) not null
-- Additional Constraints
			 );

CREATE INDEX PDIndex ON patientDetails(vaersID);

CREATE TABLE vaccineDetails (vaersID int primary key,
			 vaccineType char(15) default null,
			 vaxManu char(40) not null,
             vaxLot char(15) default null,
             state char(2) default null,
             vaxRoute char(6) default null,
             vaxSite char(6) default null,
             vaxName char(100) not null,
             spltType char(25) default null,
             vaxFundBy char(3) default null,
             vaxAdminBy char(3) default null
-- Additional Constraints
			 );
             
create index VDIndex on vaccineDetails(vaersID);
create index VMIndex on vaccineDetails(vaxManu);

create table symptomDetails (vaersID int,
		      symptom1 char(100) default null,
              symptomVersion1 decimal(3,1) default null,
              symptom2 char(100) default null,
              symptomVersion2 decimal(3,1) default null,
              symptom3 char(100)default null,
              symptomVersion3 decimal(3,1) default null,
			  symptom4 char(100) default null,
              symptomVersion4 decimal(3,1) default null,
			  symptom5 char(100) default null,
              symptomVersion5 decimal(3,1) default null
-- Additional Constraints
			 );
  
create index SDIndex on symptomDetails (vaersID);
ALTER TABLE symptomDetails
ADD CONSTRAINT PK_SD PRIMARY KEY (vaersID, symptom1);

create table patientResults (vaersID int primary key,
			 recovered char(5) default null,
             died char(2)default null,
             dateOfDeath date default null
-- Additional Constraints
			 );
create index PRIndex on patientResults (vaersID);
create index PDIndex on patientResults (died);

create table dateRecords (vaersID int primary key,
				receivedDate date default null,
                reportDate date default null,
                vaccineDate date default null,
                onsetDate date default null
-- Additional Constraints
			 );	
create index DRIndex on dateRecords (vaersID);


create table preExistingConditions (vaersID int primary key,
				otherMeds varchar(254) default null,
                currentIllness varchar(254) default null,
                historyMeds varchar(254) default null,
                birthDefect char(5) default null,
                priorVaccine char(128) default null
-- Additional Constraints
			 );

create index PECIndex on preExistingConditions (vaersID);

create table patientOutcomes (vaersID int primary key,
				lThreat char(1) default null,
                erVisit char(1) default null,
                hospital char(1) default null,
                hospDays int default null,
                xStay char(1) default null,
                disabled char(1) default null,
                labData varchar(254) default null,
                officeVisit char(1) default null,
                eredVisit char(1) default null,
                vaxDoseSeries int default null,
                symptomText varchar(254) default null,
                numDays int default null,
                formVersion decimal(3,2) default null,
                todaysDate date default null,
                allergies varchar(254) default null
-- Additional Constraints
			 );
             
create index PCIndex on patientOutcomes (vaersID);