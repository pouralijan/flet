from typing import Any, List, Optional

from beartype import beartype

from flet.buttons import OutlinedBorder
from flet.control import Control, MainAxisAlignment
from flet.ref import Ref
from flet.types import PaddingValue


class AlertDialog(Control):
    def __init__(
        self,
        ref: Optional[Ref] = None,
        disabled: Optional[bool] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # Specific
        #
        open: bool = False,
        modal: bool = False,
        title: Optional[Control] = None,
        title_padding: PaddingValue = None,
        content: Optional[Control] = None,
        content_padding: PaddingValue = None,
        actions: Optional[List[Control]] = None,
        actions_padding: PaddingValue = None,
        actions_alignment: MainAxisAlignment = None,
        shape: Optional[OutlinedBorder] = None,
        on_dismiss=None,
    ):

        Control.__init__(
            self,
            ref=ref,
            disabled=disabled,
            visible=visible,
            data=data,
        )

        self.__title: Optional[Control] = None
        self.__content: Optional[Control] = None
        self.__actions: List[Control] = []

        self.open = open
        self.modal = modal
        self.title = title
        self.title_padding = title_padding
        self.content = content
        self.content_padding = content_padding
        self.actions = actions
        self.actions_padding = actions_padding
        self.actions_alignment = actions_alignment
        self.shape = shape
        self.on_dismiss = on_dismiss

    def _get_control_name(self):
        return "alertdialog"

    def _before_build_command(self):
        super()._before_build_command()
        self._set_attr_json("actionsPadding", self.__actions_padding)
        self._set_attr_json("contentPadding", self.__content_padding)
        self._set_attr_json("titlePadding", self.__title_padding)
        self._set_attr_json("shape", self.__shape)

    def _get_children(self):
        children = []
        if self.__title:
            self.__title._set_attr_internal("n", "title")
            children.append(self.__title)
        if self.__content:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        for action in self.__actions:
            action._set_attr_internal("n", "action")
            children.append(action)
        return children

    # open
    @property
    def open(self) -> Optional[bool]:
        return self._get_attr("open", data_type="bool", def_value=False)

    @open.setter
    @beartype
    def open(self, value: Optional[bool]):
        self._set_attr("open", value)

    # modal
    @property
    def modal(self) -> Optional[bool]:
        return self._get_attr("modal", data_type="bool", def_value=False)

    @modal.setter
    @beartype
    def modal(self, value: Optional[bool]):
        self._set_attr("modal", value)

    # title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    # title_padding
    @property
    def title_padding(self) -> PaddingValue:
        return self.__title_padding

    @title_padding.setter
    @beartype
    def title_padding(self, value: PaddingValue):
        self.__title_padding = value

    # content
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    # content_padding
    @property
    def content_padding(self) -> PaddingValue:
        return self.__content_padding

    @content_padding.setter
    @beartype
    def content_padding(self, value: PaddingValue):
        self.__content_padding = value

    # actions
    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, value):
        self.__actions = value if value is not None else []

    # actions_padding
    @property
    def actions_padding(self) -> PaddingValue:
        return self.__actions_padding

    @actions_padding.setter
    @beartype
    def actions_padding(self, value: PaddingValue):
        self.__actions_padding = value

    # actions_alignment
    @property
    def actions_alignment(self) -> MainAxisAlignment:
        return self._get_attr("actionsAlignment")

    @actions_alignment.setter
    @beartype
    def actions_alignment(self, value: MainAxisAlignment):
        self._set_attr("actionsAlignment", value)

    # shape
    @property
    def shape(self) -> Optional[OutlinedBorder]:
        return self.__shape

    @shape.setter
    @beartype
    def shape(self, value: Optional[OutlinedBorder]):
        self.__shape = value

    # on_dismiss
    @property
    def on_dismiss(self):
        return self._get_event_handler("dismiss")

    @on_dismiss.setter
    def on_dismiss(self, handler):
        self._add_event_handler("dismiss", handler)
