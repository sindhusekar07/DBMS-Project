-- Client Functionality


-- Type of vaccine which causes death
SELECT patientDetails.vaersID, patientDetails.ageInYears, patientResults.dateOfDeath, vaccineDetails.vaxManu 
	   FROM patientDetails 
       INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID 
       INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID 
       WHERE patientResults.died = 'Y';
       
-- Number of patients died 

SELECT count(*) FROM patientDetails 
	INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID 
	INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID WHERE patientResults.died = 'Y';

-- Number of Patients died because of PFIZER

SELECT count(*) from patientDetails 
	   INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID 
       INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID WHERE patientResults.died = 'Y' AND vaccineDetails.vaxManu = 'PFIZERBIONTECH';
      
-- Number of Patients died because of MODERNA

 SELECT count(*) FROM patientDetails 
		INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID 
        INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID WHERE patientResults.died = 'Y' AND vaccineDetails.vaxManu = 'MODERNA';
        
-- Adverse Effects based on vaccine type

SELECT patientDetails.vaersID, patientDetails.ageInYears, vaccineDetails.vaxManu, symptomDetails.symptom1, symptomDetails.symptom2, symptomDetails.symptom3, symptomDetails.symptom4, symptomDetails.symptom5
	   FROM patientDetails 
       INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID 
	   INNER JOIN symptomDetails ON patientDetails.vaersID = symptomDetails.vaersID;
      