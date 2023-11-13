from datetime import date
import time
today = date.today()
final_date = date(2024, 4, 12)

if final_date < today:
    final_date = date(2024, 4, 12)

if final_date == today:
    print("dneska jsou/byly prijmacky")

days_count = (final_date - today).days
while True:
    if days_count == 1:
        zitra = input("ZÍTRA JSOU PRIJMACKY(uc se nebo se nedostanes na ssps)")
        print(zitra)
        time.sleep(3600)

    else:
        print(f"prijmacy zkousky budou za {days_count} dni")
        time.sleep(3600)