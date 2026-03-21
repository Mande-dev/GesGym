from datetime import date
from pos.models import ExchangeRate

def get_today_rate(gym):
    return ExchangeRate.objects.get(
        gym=gym,
        date=date.today()
    )