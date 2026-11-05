from cviceni6_1 import download_rates
import sys

def convert_ammount(ammount, currency):
    rates = download_rates()
    if currency not in rates:
        return 0.0
    rate = rates[currency]
    return ammount / rate

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} amount currency")
        sys.exit()

    amount = int(sys.argv[1])
    currency = sys.argv[2]

    print(convert_ammount(amount, currency))
