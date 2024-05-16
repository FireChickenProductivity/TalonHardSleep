mode: sleep
and mode: user.hard_sleep
not mode: sleep
and mode: user.hard_sleep
not speech.engine: dragon
and mode: user.hard_sleep
-
<phrase>: user.hard_sleep_handle_non_wakeup_speech()

^(wake up)+$: user.hard_sleep_wakeup()
^talon wake [<phrase>]$: speech.enable()