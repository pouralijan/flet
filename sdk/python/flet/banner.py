from typing import Any, List, Optional

from beartype import beartype

from flet.control import Control
from flet.ref import Ref
from flet.types import PaddingValue


class Banner(Control):
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
        leading: Optional[Control] = None,
        leading_padding: Optional[PaddingValue] = None,
        content: Optional[Control] = None,
        content_padding: Optional[PaddingValue] = None,
        actions: Optional[List[Control]] = None,
        force_actions_below: Optional[bool] = None,
        bgcolor: Optional[str] = None,
    ):

        Control.__init__(
            self,
            ref=ref,
            disabled=disabled,
            visible=visible,
            data=data,
        )

        self.__leading: Optional[Control] = None
        self.__content: Optional[Control] = None
        self.__actions = []

        self.open = open
        self.leading = leading
        self.leading_padding = leading_padding
        self.content = content
        self.content_padding = content_padding
        self.actions = actions
        self.force_actions_below = force_actions_below
        self.bgcolor = bgcolor

    def _get_control_name(self):
        return "banner"

    def _before_build_command(self):
        super()._before_build_command()
        self._set_attr_json("contentPadding", self.__content_padding)
        self._set_attr_json("leadingPadding", self.__leading_padding)

    def _get_children(self):
        children = []
        if self.__leading:
            self.__leading._set_attr_internal("n", "leading")
            children.append(self.__leading)
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

    # leading
    @property
    def leading(self):
        return self.__leading

    @leading.setter
    def leading(self, value):
        self.__leading = value

    # leading_padding
    @property
    def leading_padding(self) -> PaddingValue:
        return self.__leading_padding

    @leading_padding.setter
    @beartype
    def leading_padding(self, value: PaddingValue):
        self.__leading_padding = value

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

    # force_actions_below
    @property
    def force_actions_below(self) -> Optional[bool]:
        return self._get_attr("forceActionsBelow", data_type="bool", def_value=False)

    @force_actions_below.setter
    @beartype
    def force_actions_below(self, value: Optional[bool]):
        self._set_attr("forceActionsBelow", value)

    # bgcolor
    @property
    def bgcolor(self):
        return self._get_attr("bgColor")

    @bgcolor.setter
    @beartype
    def bgcolor(self, value):
        self._set_attr("bgColor", value)
