mode: sleep
and mode: user.hard_sleep
-
^talon wake$: user.hard_sleep_wakeup()

<phrase>: user.hard_sleep_reset_counter()

^welcome back$: user.hard_sleep_reset_counter()
