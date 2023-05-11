mode: sleep
and mode: user.hard_sleep
-
^talon wake$: user.hard_sleep_wakeup()

<phrase>: user.hard_sleep_handle_non_wakeup_speech()

^welcome back$: user.hard_sleep_handle_non_wakeup_speech()
