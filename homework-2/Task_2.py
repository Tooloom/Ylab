from dataclasses import dataclass
from datetime import datetime, timedelta  # Added timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date in self.dates:
            day_step = 0
            while date[0] + timedelta(days=day_step) <= date[1]:
                yield date[0] + timedelta(days=day_step)
                day_step += 1


# --------------------- Main ---------------------
if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
