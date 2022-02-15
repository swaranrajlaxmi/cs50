-- Keep a log of any SQL queries you execute as you solve the mystery.
-- get the name of thief
SELECT name FROM people
WHERE license_plate IN
-- get the license_plate of car within 10 min duration
(SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity LIKE "exit")
-- get the id of thief by linking atm_transaction and bank_account_number
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions
WHERE transaction_type LIKE "withdraw" AND month = 7 AND day = 28 AND atm_location LIKE "Leggett Street"))
-- get the phone_number of thief
AND phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60);
AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE month = 7 AND day = 29 ORDER BY hour, minute ASC LIMIT 1));


-- get the name of city where the theif escaped to..
SELECT city FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id IN (SELECT flight_id FROM passengers
WHERE passport_number IN (SELECT passport_number FROM people WHERE name LIKE 'Bruce')));
-- get the name of person who helped the theif
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller IN
(SELECT phone_number FROM people WHERE name like "Bruce") AND month = 7 AND day = 28 AND duration < 60);