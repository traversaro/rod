import dataclasses
from typing import List, Optional, Union

import mashumaro

from .common import Frame, Pose
from .element import Element
from .joint import Joint
from .link import Link


@dataclasses.dataclass
class Model(Element):

    name: str = dataclasses.field(metadata=mashumaro.field_options(alias="@name"))

    canonical_link: Optional[str] = dataclasses.field(
        default=None, metadata=mashumaro.field_options(alias="@canonical_link")
    )

    placement_frame: Optional[str] = dataclasses.field(
        default=None, metadata=mashumaro.field_options(alias="@placement_frame")
    )

    static: Optional[bool] = dataclasses.field(
        default=None,
        metadata=mashumaro.field_options(
            serialize=Element.serialize_bool, deserialize=Element.deserialize_bool
        ),
    )

    self_collide: Optional[bool] = dataclasses.field(
        default=None,
        metadata=mashumaro.field_options(
            serialize=Element.serialize_bool, deserialize=Element.deserialize_bool
        ),
    )

    allow_auto_disable: Optional[bool] = dataclasses.field(
        default=None,
        metadata=mashumaro.field_options(
            serialize=Element.serialize_bool, deserialize=Element.deserialize_bool
        ),
    )

    enable_wind: Optional[bool] = dataclasses.field(
        default=None,
        metadata=mashumaro.field_options(
            serialize=Element.serialize_bool, deserialize=Element.deserialize_bool
        ),
    )

    pose: Optional[Pose] = dataclasses.field(default=None)

    model: Optional[Union["Model", List["Model"]]] = dataclasses.field(default=None)

    frame: Optional[Union[Frame, List[Frame]]] = dataclasses.field(default=None)

    link: Optional[Union[Link, List[Link]]] = dataclasses.field(default=None)

    joint: Optional[Union[Joint, List[Joint]]] = dataclasses.field(default=None)

    def is_fixed_base(self) -> bool:

        joints_having_world_parent = [j for j in self.joints() if j.parent == "world"]
        assert len(joints_having_world_parent) in {0, 1}

        return len(joints_having_world_parent) > 0

    def models(self) -> List["Model"]:

        if self.model is None:
            return []

        if isinstance(self.model, Model):
            return [self.model]

        assert isinstance(self.model, list)
        return self.model

    def frames(self) -> List[Frame]:

        if self.frame is None:
            return []

        if isinstance(self.frame, Frame):
            return [self.frame]

        assert isinstance(self.frame, list)
        return self.frame

    def links(self) -> List[Link]:

        if self.link is None:
            return []

        if isinstance(self.link, Link):
            return [self.link]

        assert isinstance(self.link, list), type(self.link)
        return self.link

    def joints(self) -> List[Joint]:

        if self.joint is None:
            return []

        if isinstance(self.joint, Joint):
            return [self.joint]

        assert isinstance(self.joint, list), type(self.joint)
        return self.joint
