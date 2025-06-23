# No Longer Maintained
This project has been abandoned now that community has deep sleep.

# Talon Hard Sleep
The hard sleep mode for Talon Voice requires consecutively saying valid wakeup commands to wakeup talon. The default number of required consecutive times is 3. You can change the number of times you must consecutively tell talon to wake up to exit hard sleep in the settings.talon. Making it 0 means that you cannot wake up talon through saying talon wake. Saying anything other than a valid wakeup command in the hard sleep mode resets the wakeup counter so that you would have to start saying wake up commands again from the beginning. 

The user.hard_sleep_wakeup_immediately() action immediately wakes up talon from hard sleep regardless of how any of the settings are set.

If you only want talon to wakeup through something like a keypress, you could set up a talon script to immediately wake up from hard sleep when you press a key and set the amount of times you must use a wakeup command to wakeup talon to 0, which would prevent wakeup commands from waking it up no matter how many times they are used.

The user.hard_sleep_wakeup_availability_delay setting available in the settings.talon file determines how many milliseconds after saying anything other than a valid wakeup command it is impossible to wake up from hard sleep. This is 0 by default but can be used to make it even more unlikely that talon will get woken up on accident in the middle of a conversation. 

The user.hard_sleep_wakeup_delay setting determines the number of milliseconds normal wakeup from hard sleep is delayed. During delayed wakeup, the user.hard_sleep_cancel_delayed_wakeup action can be used to cancel the delayed wakeup. This could be bound to noise input to provide a convenient way to cancel unwanted wakeups before they result in random commands executing. 

The user.hard_sleep_should_show_display setting can be set to 0 to disable the display. 

# Commands
talon hard sleep: activates hard sleep.

talon wake: one of the valid wakeup commands.

wake up: one of the valid wakeup commands if you are using the conformer speech engine.
