from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import mod, keys

__groups = {
    1: Group(" 󰮯 "),
    2: Group("   ", matches=[Match(wm_class=["firefox", "Firefox"])]),
    3: Group("  "),
    4: Group("  "),
    5: Group("  ", matches=[Match(wm_class=["microsoft-edge", "Microsoft-edge"])]),
    6: Group("  "),
}

groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
