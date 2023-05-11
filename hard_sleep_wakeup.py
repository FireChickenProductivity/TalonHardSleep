from talon import Module, actions, cron

module = Module()

module.mode('hard_sleep', 'Like sleep mode but takes consecutive wake ups to wake up from.')

wakeups_needed = module.setting(
    'hard_sleep_wakeups_needed',
    type = int,
    default = 3,
    desc = 'How many consecutive wake ups needed to wakeup talon from hard sleep.'
)

wakeup_availability_delay = module.setting(
    'hard_sleep_wakeup_availability_delay',
    type = int,
    default = 0,
    desc = 'How long to make waking up from hard sleep unavailable after something is said other than a wakeup command in milliseconds'
)

wakeup_counter: int = 0
number_of_availability_blocks: int = 0
@module.action_class
class Actions:
    def hard_sleep_wakeup():
        ''''''
        global wakeup_counter, number_of_availability_blocks
        wakeup_counter += 1
        if wakeup_counter >= wakeups_needed.get() and wakeups_needed.get() != 0:
            if number_of_availability_blocks == 0:
                actions.user.hard_sleep_wakeup_immediately()
            else:
                wakeup_counter -= 1
    
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
    
    def hard_sleep_handle_non_wakeup_speech():
        ''''''
        if wakeup_availability_delay.get() > 0:
            global number_of_availability_blocks
            number_of_availability_blocks += 1
            def after_delay():
                global number_of_availability_blocks
                number_of_availability_blocks -= 1
            cron.after(f'{wakeup_availability_delay.get()}ms', after_delay)
        actions.user.hard_sleep_reset_counter()
