from accepted import (
    AcceptedEasy,
    AcceptedMedium,
    AcceptedHard
)

from refused import (
    RefusedEasy,
    RefusedMedium,
    RefusedHard
)


class LeetCodeRefused(RefusedEasy, RefusedMedium, RefusedHard): ...

class LeetCodeAccepted(AcceptedEasy, AcceptedMedium, AcceptedHard): ...