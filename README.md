# Talon Hard Sleep
The hard sleep mode for Talon Voice requires consecutively saying talon wake to wakeup talon. The default number of required consecutive times is 3. You can change the number of times you must consecutively tell talon to wake up to exit hard sleep in the settings.talon. Making it 0 means that you cannot wake up talon through saying talon wake. Saying anything other than talon wake in the hard sleep mode resets the wakeup counter so that you would have to start saying talon wake again from the beginning. 

The user.hard_sleep_wakeup_immediately() action immediately wakes up talon from hard sleep.

If you only want talon to wakeup through something like a keypress, you could set up a talon script to immediately wake up from hard sleep when you press a key and set the amount of times you must say talon wake to wakeup talon to 0, which would prevent talon wake from waking it up no matter how many times it is said.

The user.hard_sleep_wakeup_availability_delay setting available in the settings.talon file determines how many milliseconds after saying anything other than talon wake it is impossible to wake up from hard sleep. This is 0 by default, but can be used to make it even more unlikely that talon will get woken up on accident in the middle of a conversation. 

# Commands
talon hard sleep: activates hard sleep

talon wake: must be said consecutively the required number of times to exit hard sleep (the default number of times is 3). 
