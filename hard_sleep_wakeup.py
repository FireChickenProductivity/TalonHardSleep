from talon import Module, actions, cron, imgui, settings

module = Module()

module.mode('hard_sleep', 'Like sleep mode but takes consecutive wake ups to wake up from.')

wakeups_needed_setting_name = 'hard_sleep_wakeups_needed'
wakeups_needed = 'user.' + wakeups_needed_setting_name
module.setting(
    wakeups_needed_setting_name,
    type = int,
    default = 3,
    desc = 'How many consecutive wake ups needed to wakeup talon from hard sleep.'
)

wakeup_availability_delay_setting_name = 'hard_sleep_wakeup_availability_delay'
wakeup_availability_delay = 'user.' + wakeup_availability_delay_setting_name
module.setting(
    wakeup_availability_delay_setting_name,
    type = int,
    default = 0,
    desc = 'How long to make waking up from hard sleep unavailable after something is said other than a wakeup command in milliseconds'
)

should_show_display_setting_name = 'hard_sleep_should_show_display'
should_show_display = 'user.' + should_show_display_setting_name
module.setting(
    should_show_display_setting_name,
    type = int,
    default = 1,
    desc = 'Make this 0 if the hard sleep display should not be shown. Make this any other integer otherwise'
)

wakeup_delay_setting_name = 'hard_sleep_wakeup_delay'
wakeup_delay = 'user.' + wakeup_delay_setting_name
module.setting(
    wakeup_delay_setting_name,
    type = int,
    default = 0,
    desc = 'How long to wait before waking up talon from hard sleep in milliseconds.'
)

wakeup_counter: int = 0
number_of_availability_blocks: int = 0
waking_up: bool = False
@module.action_class
class Actions:
    def hard_sleep_wakeup():
        ''''''
        global wakeup_counter, number_of_availability_blocks, waking_up
        wakeup_counter += 1
        if wakeup_counter >= settings.get(wakeups_needed) and settings.get(wakeups_needed) != 0:
            if number_of_availability_blocks == 0:
                if settings.get(wakeup_delay) == 0:
                    actions.user.hard_sleep_wakeup_immediately()
                else:
                    def wakeup_if_not_canceled():
                        global waking_up
                        if waking_up:
                            actions.user.hard_sleep_wakeup_immediately()
                        else:
                            actions.user.hard_sleep_reset_counter()
                        waking_up = False
                    waking_up = True
                    cron.after(f'{settings.get(wakeup_delay)}ms', wakeup_if_not_canceled)
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
        if settings.get(wakeup_availability_delay) > 0:
            global number_of_availability_blocks
            number_of_availability_blocks += 1
            def after_delay():
                global number_of_availability_blocks
                number_of_availability_blocks -= 1
            cron.after(f'{settings.get(wakeup_availability_delay)}ms', after_delay)
        actions.user.hard_sleep_reset_counter()
    
    def hard_sleep_cancel_delayed_wakeup():
        ''''''
        global waking_up
        waking_up = False

def should_show_hard_sleep_display() -> bool:
    return settings.get(should_show_display) != 0

@imgui.open(y = 0, x = 0)
def gui(gui: imgui.GUI):
    gui.text('Hard Sleep')
    gui.text(f'Wakeup counter: {wakeup_counter}')
    if number_of_availability_blocks > 0:
        gui.text('Wakeup temporarily unavailable!')
    if settings.get(wakeup_delay) != 0 and waking_up:
        gui.text('Waking up!')
