from dearpygui import dearpygui as dpg

def center(modal_id):
    viewport_width = dpg.get_viewport_client_width()
    viewport_height = dpg.get_viewport_client_height()

    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])


def show_error(title, message, selection_callback=None):
    def _callback(sender, unused, user_data):
        dpg.delete_item(user_data[0])
        if selection_callback is not None:
            selection_callback(user_data)

    with dpg.mutex():
        with dpg.window(label=title, modal=True, no_close=True) as modal_id:
            dpg.add_text(message)
            dpg.add_button(label="Ok", width=75, user_data=(modal_id, True),
                           callback=lambda a, b, c: _callback(a, b, c))

    center(modal_id)