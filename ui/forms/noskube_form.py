import npyscreen
import abc

from ui.events.mainmenu_event_handler import MainMenuEventHandler
from ui.events.podmenu_event_handler import PodMenuEventHandler
from ui.events.servicemenu_event_handler import ServiceMenuEventHandler

from ui.forms.items.main_button import MainButton
from ui.forms.items.pod_button import PodButton
from ui.forms.items.service_button import ServiceButton
from ui.forms.items.status_box import StatusBox

import constants as c


class NosKubeForm(npyscreen.SplitForm):

    @property
    def current_form_id(self):
        return self.form_id

    @current_form_id.setter
    def current_form_id(self, form_id):
        self.form_id = form_id

    def configure_event_handler(self, kubernetes_api, event_handlers,
                                handle_menu=False):
        if handle_menu is True:
            event_handlers = (event_handlers +
                              [{"e": "main_menu", "h": MainMenuEventHandler},
                               {"e": "pod_menu", "h": PodMenuEventHandler},
                               {"e": "service_menu",
                                "h": ServiceMenuEventHandler}])

        for event_handler in event_handlers:
                self.add_event_hander(event_handler["e"],
                                      event_handler["h"](self,
                                                         event_handler["e"],
                                                         kubernetes_api)
                                      .proces_event)

    def get_menu_item_color(self, button_name):
        if self.current_form_id == button_name:
            return 'VERYGOOD'
        else:
            return 'CAUTIONHL'

    def add_horizontal_menu(self):
        self.menu_buttons = []

        x = self.nextrelx
        y = self.nextrely = self.nextrely + 2

        buttons = [{"name": "MAIN CONFIGURATION", "btn": MainButton},
                   {"name": "POD CONTROL", "btn": PodButton},
                   {"name": "SERVICE HUB", "btn": ServiceButton}]

        for button in buttons:
            bt = self.add(button["btn"],
                          name=button["name"],
                          color=self.get_menu_item_color(button["name"]))
            self.menu_buttons.append(bt)
            self.nextrely = y
            self.nextrelx = self.nextrelx + bt.width

        self.nextrelx = x
        self.nextrely = self.nextrely + 2

    def refresh_menu(self):
        for btn in self.menu_buttons:
            btn.color = self.get_menu_item_color(btn.name)
            btn.display()

    @abc.abstractmethod
    def add_form_page(self):
        raise NotImplementedError("""
        users must define add_form_page to use this base class
        """)

    def add_form_components(self):
        y, x = self.useable_space()

        self.add_horizontal_menu()

        self.add_form_page()

        self.nextrely = c.Y_POS_HALF_WAY
        self.status_box = self.add(StatusBox,
                                   max_height=c.Y_MAX_STATUSBOX,
                                   footer="By Michel Nossin",
                                   editable=False,
                                   name="NosKube output",
                                   value="""
        Use TAB and SHIFT-TAB to browse components.
        Use Cursor keys to move inside a component.
        Press ENTER to select an item""")

    def create(self):
        self.add_form_components()

    def update_status_box(self, value):
        self.status_box.value = value
        self.status_box.display()

    def exit_func(self, _input):
        exit(0)
