import requests


class ExchangeRatesNBU:
    exchange_rates = []
    date = None

    def get_rates(self):
        try:
            request = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
            request_json = request.json()
        except Exception as e:
            return f'Error: {e}'
        if 300 < request.status_code < 200:
            return f'Error {request.status_code}'
        elif request.headers.get('Content-Type') != 'application/json; charset=utf-8':
            return 'Not json'
        elif not request_json:
            return 'Request is empty'
        elif 'exchangedate' not in request_json[0] or 'cc' not in request_json[0] or 'rate' not in request_json[0]:
            return 'There are not enough attributes in request'
        self.date = request_json[0]['exchangedate']
        date_for_txt_name = self.date.replace(".", "_")
        with open(f'{date_for_txt_name}.txt', 'w') as file:
            for dictionary in request_json:
                index = request_json.index(dictionary) + 1
                cc = dictionary['cc']
                rate = dictionary['rate']
                self.exchange_rates.append(f'{index}. {cc} to UAH: {rate}')
                file.write(f'{index}. {cc} to UAH: {rate}\n')
        return 'Success!'


def main():
    ex = ExchangeRatesNBU()
    print(ex.get_rates())
    print(ex.exchange_rates)


if __name__ == '__main__':
    main()
