set global local_infile=true;

alter table patientDetails drop column cageInYears;
alter table vaccineDetails drop column vaccineType;
alter table vaccineDetails drop column vaxFundBy ;
alter table dateRecords drop column reportDate;
alter table patientOutcomes drop column todaysDate ;

-- CHECK CONSTRAINTS
ALTER TABLE patientDetails
ADD CONSTRAINT DigiConstraint
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE vaccineDetails
ADD CONSTRAINT DC_1
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE symptomDetails
ADD CONSTRAINT DC_2
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE patientResults
ADD CONSTRAINT DC_3
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE preExistingConditions
ADD CONSTRAINT DC_4
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE dateRecords
ADD CONSTRAINT DC_5
CHECK (vaersID NOT LIKE '%[^0-9]%');

ALTER TABLE patientOutcomes
ADD CONSTRAINT DC_6
CHECK (vaersID NOT LIKE '%[^0-9]%');

-- Loading all the Tables

-- loading patientDetails Table

load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table patientDetails
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, ageInYears = NULLIF(@col21, ''), cageInMonth = NULLIF(@col23, ''), sex= if(@col24='U', NULL, @col24);

-- Loading vaccineDetails Table 

load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table vaccineDetails
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1,vaxManu=@col13, vaxLot= NULLIF(@col14, ''), state = NULLIF(@col20, ''), vaxRoute =  NULLIF(@col16, ''), vaxSite = NULLIF(@col17, ''), vaxName = @col18, spltType = NULLIF(@col46, ''),  vaxAdminBy = NULLIF(@col40, '')  ; 


-- Loading Symptom Details table
             
load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table symptomDetails
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, symptom1= NULLIF(@col2, ''), symptomVersion1=NULLIF(@col3, ''), symptom2=NULLIF(@col4, ''), symptomVersion2 = NULLIF(@col5, ''), symptom3 = NULLIF(@col6, ''), symptomVersion3 = NULLIF(@col7, ''), symptom4 = NULLIF(@col8, ''), symptomVersion4 = NULLIF(@col9, ''), symptom5 = NULLIF(@col10, ''), symptomVersion5 = NULLIF(@col11, '')  ; 



-- loading Patient Results Table
             
load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table patientResults
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, recovered = NULLIF(@col35, ''), died  = NULLIF(@col27, ''), dateOfDeath = str_to_date(@col28, "%m/%d/%Y");


-- loading pre existing conditions table

load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table preExistingConditions
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, otherMeds = NULLIF(@col42, ''), historyMeds = NULLIF(@col44, ''), birthDefect = NULLIF(@col49, ''), priorVaccine = NULLIF(@col45, '');



-- loading dateRecords table

load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table dateRecords
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, receivedDate = STR_TO_DATE(@col19, "%m/%d/%Y"),  vaccineDate = STR_TO_DATE(@col36, "%m/%d/%Y"), onsetDate = STR_TO_DATE(@col37, "%m/%d/%Y") ;


 
-- loading patient Outcomes table
             
load data local infile '/Users/sindhumathiramalingam/downloads/WaterlooAcademics/ECE656/Project/Workings/vaccineInfo.csv' ignore into table patientOutcomes
     fields terminated by ','
     optionally enclosed by '"'
     lines terminated by '\r\n'
      ignore 1 lines
      (@col1,@col2,@col3,@col4,@col5,@col6,@col7,@col8,@col9,@col10,@col11,@col12,@col13,@col14,@col15,@col16,@col17,@col18,@col19,@col20,@col21,@col22,@col23,@col24,@col25,@col26,@col27,@col28,@col29,@col30,@col31,@col32,@col33,@col34,@col35,@col36,@col37,@col38,@col39,@col40,@col41,@col42,@col43,@col44,@col45,@col46,@col47,@col48,@col49,@col50,@col51,@col52) 
set vaersID=@col1, lThreat = NULLIF(@col29, ''),  erVisit = NULLIF(@col30, ''), hospital =NULLIF(@col31, ''), hospDays = NULLIF(@col32, ''), xStay = NULLIF(@col33, ''), disabled = NULLIF(@col34, ''), labData = NULLIF(@col39, ''), officeVisit = NULLIF(@col50, ''), eredVisit =NULLIF(@col51, ''), vaxDoseSeries = NULLIF(@col15, ''),  
    symptomText = NULLIF(@col26, ''), numDays = NULLIF(@col38, ''), formVersion =  NULLIF(@col47, ''), allergies = NULLIF(@col52, '')  ;

-- creation of Foreign Keys

ALTER TABLE vaccineDetails
ADD FOREIGN KEY (vaersID) REFERENCES dateRecords(vaersID);
ALTER TABLE symptomDetails
ADD FOREIGN KEY (vaersID) REFERENCES patientDetails(vaersID);
ALTER TABLE patientResults
ADD FOREIGN KEY (vaersID) REFERENCES patientOutcomes(vaersID);
ALTER TABLE preExistingConditions
ADD FOREIGN KEY (vaersID) REFERENCES patientResults(vaersID);
ALTER TABLE dateRecords
ADD FOREIGN KEY (vaersID) REFERENCES patientDetails(vaersID);
ALTER TABLE patientOutcomes
ADD FOREIGN KEY (vaersID) REFERENCES symptomDetails(vaersID);