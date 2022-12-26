from talon import Module, actions

module = Module()

module.mode('hard_sleep', 'Like sleep mode but takes consecutive wake ups to wake up from.')

wakeups_needed = module.setting(
    'hard_sleep_wakeups_needed',
    type = int,
    default = 3,
    desc = 'How many consecutive wake ups needed to wakeup talon from hard sleep.'
)

wakeup_counter: int = 0
@module.action_class
class Actions:
    def hard_sleep_wakeup():
        ''''''
        global wakeup_counter
        wakeup_counter += 1
        if wakeup_counter >= wakeups_needed.get():
            actions.user.hard_sleep_wakeup_immediately()
    
    def hard_sleep_reset_counter():
        ''''''
        global wakeup_counter
        wakeup_counter = 0
    
    def hard_sleep_wakeup_immediately():
        ''''''
        actions.user.hard_sleep_reset_counter()
        actions.speech.enable()
        actions.mode.disable('user.hard_sleep')
    
    def hard_sleep_enable():
        ''''''
        actions.speech.disable()
        actions.mode.enable('user.hard_sleep')
        actions.user.hard_sleep_reset_counter()
