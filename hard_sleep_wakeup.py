from talon import Module, actions, cron, imgui

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

should_show_display = module.setting(
    'hard_sleep_should_show_display',
    type = int,
    default = 1,
    desc = 'Make this 0 if the hard sleep display should not be shown. Make this any other integer otherwise'
)

wakeup_delay = module.setting(
    'hard_sleep_wakeup_delay',
    type = int,
    default = 0,
    desc = 'How long to wait before waking up talon from hard sleep in milliseconds.'
)

wakeup_counter: int = 0
number_of_availability_blocks: int = 0
delayed_wakeup_canceled: bool = False
@module.action_class
class Actions:
    def hard_sleep_wakeup():
        ''''''
        global wakeup_counter, number_of_availability_blocks
        wakeup_counter += 1
        if wakeup_counter >= wakeups_needed.get() and wakeups_needed.get() != 0:
            if number_of_availability_blocks == 0:
                if wakeup_delay.get() == 0:
                    actions.user.hard_sleep_wakeup_immediately()
                else:
                    def wakeup_if_not_canceled():
                        global delayed_wakeup_canceled
                        if not delayed_wakeup_canceled:
                            actions.user.hard_sleep_wakeup_immediately()
                        delayed_wakeup_canceled = False
                    cron.after(f'{wakeup_delay.get()}ms', wakeup_if_not_canceled)
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
        gui.hide()
    
    def hard_sleep_enable():
        ''''''
        actions.speech.disable()
        actions.mode.enable('user.hard_sleep')
        actions.user.hard_sleep_reset_counter()
        if should_show_hard_sleep_display():
            gui.show()
    
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
    
    def hard_sleep_cancel_delayed_wakeup():
        ''''''
        global delayed_wakeup_canceled
        delayed_wakeup_canceled = True

def should_show_hard_sleep_display() -> bool:
    return should_show_display.get() != 0

@imgui.open(y = 0, x = 0)
def gui(gui: imgui.GUI):
    gui.text('Hard Sleep')
    gui.text(f'Wakeup counter: {wakeup_counter}')
    if number_of_availability_blocks > 0:
        gui.text(f'Temporary unavailability counter: {number_of_availability_blocks}')
