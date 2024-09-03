-- Mask the first 12 digits of the credit card number

/*
Input 
|---------------------|
| credit_card_number  |
-----------------------
| 1234567890123456    |
| 2345678910111213    | 
| 3456789101112131    |
-----------------------

Output
|---------------------|
| credit_card_number  |
| ****************3456 |
| ****************1213 |
| ****************2131 |
-----------------------
*/

SELECT 
    CONCAT('************', RIGHT(credit_card_number, 4)) 
    AS credit_card_number
FROM hero_corp.customers;


