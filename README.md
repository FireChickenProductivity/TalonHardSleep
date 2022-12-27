# Talon Hard Sleep
The hard sleep mode for Talon Voice requires consecutively saying talon wake to wakeup talon. The default number of required consecutive times is 3. You can change the number of times you must consecutively tell talon to wake up to exit hard sleep in the settings.talon. Saying anything other than talon wake in the hard sleep mode resets the wakeup counter so that you would have to start saying talon wake again from the beginning. 

The user.hard_sleep_wakeup_immediately() action immediately wakes up talon from hard sleep.

If you only want talon to wakeup through something like a keypress, you could set up a talon script to immediately wake up from hard sleep when you press a key and set the amount of times you must say talon wake to wakeup talon to something absurd like 3000000.
