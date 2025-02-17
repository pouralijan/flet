from typing import Any, List, Optional, Union

from beartype import beartype
from beartype.typing import Dict

from flet.constrained_control import ConstrainedControl
from flet.control import Control, CrossAxisAlignment, MainAxisAlignment, OptionalNumber
from flet.ref import Ref
from flet.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


class ResponsiveRow(ConstrainedControl):
    def __init__(
        self,
        controls: Optional[List[Control]] = None,
        ref: Optional[Ref] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        #
        # Row specific
        #
        columns: Optional[ResponsiveNumber] = None,
        alignment: MainAxisAlignment = None,
        vertical_alignment: CrossAxisAlignment = None,
        spacing: Optional[ResponsiveNumber] = None,
        run_spacing: Optional[ResponsiveNumber] = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.controls = controls
        self.alignment = alignment
        self.vertical_alignment = vertical_alignment
        self.spacing = spacing
        self.run_spacing = run_spacing
        self.columns = columns

    def _get_control_name(self):
        return "responsiverow"

    def _before_build_command(self):
        super()._before_build_command()
        self._set_attr_json("columns", self._wrap_attr_dict(self.__columns))
        self._set_attr_json("spacing", self._wrap_attr_dict(self.__spacing))
        self._set_attr_json("runSpacing", self._wrap_attr_dict(self.__run_spacing))

    def _get_children(self):
        return self.__controls

    def clean(self):
        Control.clean(self)
        self.__controls.clear()

    # horizontal_alignment
    @property
    def alignment(self) -> MainAxisAlignment:
        return self._get_attr("alignment")

    @alignment.setter
    @beartype
    def alignment(self, value: MainAxisAlignment):
        self._set_attr("alignment", value)

    # vertical_alignment
    @property
    def vertical_alignment(self) -> CrossAxisAlignment:
        return self._get_attr("verticalAlignment")

    @vertical_alignment.setter
    @beartype
    def vertical_alignment(self, value: CrossAxisAlignment):
        self._set_attr("verticalAlignment", value)

    # columns
    @property
    def columns(self) -> Optional[ResponsiveNumber]:
        return self.__columns

    @columns.setter
    @beartype
    def columns(self, value: Optional[ResponsiveNumber]):
        self.__columns = value

    # spacing
    @property
    def spacing(self) -> Optional[ResponsiveNumber]:
        return self.__spacing

    @spacing.setter
    @beartype
    def spacing(self, value: Optional[ResponsiveNumber]):
        self.__spacing = value

    # run_spacing
    @property
    def run_spacing(self) -> Optional[ResponsiveNumber]:
        return self.__run_spacing

    @run_spacing.setter
    @beartype
    def run_spacing(self, value: Optional[ResponsiveNumber]):
        self.__run_spacing = value

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value if value is not None else []
