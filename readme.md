[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/neverlosecc/api-wrapper">
    <img src="https://forum.neverlose.cc/uploads/default/original/1X/c7436ed0aebdb99328a52a65f2ece15a2c58a9be.png" alt="Logo" height="80">
  </a>

  <h3 align="center">Neverlose.cc web API wrapper</h3>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

First of all you need to install:
* python3
```sh
sudo apt-get install python3-pip
```

### Installation

1. Install from pip
```bash
sudo pip3 install neverlose
```



<!-- USAGE EXAMPLES -->
## Usage

```python
from neverlose import Client
from neverlose.models.events import BalanceTransfer
from neverlose.models.events import ItemPurchase


app = Client(
  secret='my_secret', # Can be found on https://neverlose.cc/market/api
  user_id=739 # Can be found on https://neverlose.cc/market/api
)


@app.on_item_purchase()
async def my_purchase_handler(data: ItemPurchase):
    print(f'{data.username} just bought {data.item_id}')


@app.on_balance_transfer()
async def my_balance_transfer_handler(data: BalanceTransfer):
    print(f'{data.username} ty for {data.amount}')


if __name__ == '__main__':
    app.transfer_money(1.0, 'soufivw')
    app.give_market_item('soufivw', 'IS6raE')
    app.run_web()
```



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Arsenii Esenin - me@es3n.in

Project Link: [https://github.com/neverlosecc/api-wrapper](https://github.com/neverlosecc/api-wrapper)




<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/neverlosecc/api-wrapper.svg?style=flat-square
[contributors-url]: https://github.com/neverlosecc/api-wrapper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/neverlosecc/api-wrapper.svg?style=flat-square
[forks-url]: https://github.com/neverlosecc/api-wrapper/network/members
[stars-shield]: https://img.shields.io/github/stars/neverlosecc/api-wrapper.svg?style=flat-square
[stars-url]: https://github.com/neverlosecc/api-wrapper/stargazers
[issues-shield]: https://img.shields.io/github/issues/neverlosecc/api-wrapper.svg?style=flat-square
[issues-url]: https://github.com/neverlosecc/api-wrapper/issues
[license-shield]: https://img.shields.io/github/license/neverlosecc/api-wrapper.svg?style=flat-square
[license-url]: https://github.com/neverlosecc/api-wrapper/blob/master/LICENSE.txt