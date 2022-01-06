-- Static Data Mining

-- 1. Number of people who got vaccined 1st dose. 2nd dose (in percentage) and total vaccination percentage

SELECT
  ((SELECT count(*) FROM patientOutcomes 
         WHERE vaxDoseSeries IS NOT NULL) / 
  (SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientOutcomes)) * 100 AS Percentage_of_vaccinated 
  FROM patientOutcomes LIMIT 1;

SELECT  
((SELECT count(*) FROM patientOutcomes 
        WHERE vaxDoseSeries = '1') / 
(SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientOutcomes)) * 100 AS Percentage_of_vaccinated 
FROM patientOutcomes LIMIT 1;

SELECT  ((SELECT count(*) FROM patientOutcomes 
               WHERE vaxDoseSeries = '2') / 
         (SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientOutcomes)) * 100 AS Percentage_of_vaccinated 
         FROM patientOutcomes LIMIT 1;

-- 2. Died and Recovered Percentage

SELECT  ((SELECT count(*) FROM patientResults WHERE recovered = 'Y') / 
		(SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientResults)) * 100 AS Percentage_of_vaccinated 
        FROM patientResults LIMIT 1;

SELECT  ((SELECT count(*) FROM patientResults WHERE recovered = 'N') / 
		(SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientResults)) * 100 AS Percentage_of_vaccinated 
         FROM patientResults LIMIT 1;

SELECT  ((SELECT count(*) FROM patientResults WHERE died = 'Y') / 
		(SELECT count(DISTINCT vaersID) AS TotalPatients FROM patientResults)) * 100 AS Percentage_of_vaccinated 
        FROM patientResults LIMIT 1;

-- Which Dose has more adverse effects


SELECT (SELECT count(patientOutcomes.vaersID) FROM patientOutcomes 
         INNER JOIN symptomDetails on symptomDetails.vaersID = patientOutcomes.vaersID 
         WHERE symptomDetails.symptom1 != '' AND
         symptomDetails.symptom2  != '' AND 
         symptomDetails.symptom3 != '' AND 
         symptomDetails.symptom4 != '' AND 
         symptomDetails.symptom5 != '' AND 
         patientOutcomes.vaxDoseSeries = '1')/ 
         (select count(*) from symptomDetails where symptom1 != '' and symptom2  != '' and symptom3 != '' and symptom4 != '' and symptom5 != '') * 100 AS adverse_effects 
         ;
         
SELECT (SELECT count(patientOutcomes.vaersID) FROM patientOutcomes 
         INNER JOIN symptomDetails on symptomDetails.vaersID = patientOutcomes.vaersID 
         WHERE symptomDetails.symptom1 != '' AND
         symptomDetails.symptom2  != '' AND 
         symptomDetails.symptom3 != '' AND 
         symptomDetails.symptom4 != '' AND 
         symptomDetails.symptom5 != '' AND 
         patientOutcomes.vaxDoseSeries = '2')/ 
         (select count(*) from symptomDetails where symptom1 != '' and symptom2  != '' and symptom3 != '' and symptom4 != '' and symptom5 != '') * 100 AS adverse_effects 
         ;