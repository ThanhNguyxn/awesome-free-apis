# 🚀 Awesome Dev APIs

> A curated collection of awesome free APIs for developers. Open source and community-driven.
> This repository aims to provide a comprehensive collection of free and freemium APIs to help you build your next project.

<div align="center">

[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge&logo=github)](https://github.com/ThanhNguyxn/awesome-dev-apis)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=open-source-initiative)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange?style=for-the-badge&logo=github)](http://makeapullrequest.com)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/thanhnguyxn)

</div>

---

## 📘 General API Usage Guide

Welcome to the world of APIs! If you're new here, this guide will help you get started.

### ❓ What is an API?
**API** stands for **Application Programming Interface**. It allows two applications to talk to each other. Think of it like a waiter in a restaurant: you (the app) tell the waiter (the API) what you want, and they bring you the food (the data) from the kitchen (the server).

### 🔑 Authentication Methods
Most APIs require you to identify yourself.
-   **No Auth**: Open for everyone. Just make a request!
-   **API Key**: A secret code provided by the service. usually sent in the URL (`?api_key=123`) or Headers (`Authorization: 123`).
-   **OAuth**: A secure way to log in users (like "Login with Google").

### 📡 HTTP Methods
How you interact with the API:
-   **GET**: Retrieve data (e.g., get a list of cats).
-   **POST**: Send new data (e.g., upload a photo).
-   **PUT/PATCH**: Update existing data.
-   **DELETE**: Remove data.

### 🚦 Status Codes
The API tells you how it went with a number:
-   `200 OK`: Success! 🎉
-   `400 Bad Request`: You sent something wrong.
-   `401 Unauthorized`: You need a valid API key.
-   `404 Not Found`: The resource doesn't exist.
-   `429 Too Many Requests`: Slow down! You hit the rate limit.
-   `500 Server Error`: The API is having issues.

### 🛠️ Useful Tools
-   **[Postman](https://www.postman.com/)**: A popular tool for testing APIs without writing code.
-   **[cURL](https://curl.se/)**: A command-line tool for making requests.
-   **[Thunder Client](https://www.thunderclient.com/)**: A lightweight VS Code extension.

---

## 📖 Table of Contents

- [📘 General Usage Guide](#-general-api-usage-guide)
- [🐶 Animals](#-animals)
- [🌸 Anime](#-anime)
- [🛡️ Anti-Malware](#anti-malware)
- [📚 Books](#-books)
- [🪙 Cryptocurrency](#-cryptocurrency)
- [💻 Development](#-development)
- [🍿 Entertainment](#-entertainment)
- [💰 Finance](#-finance)
- [🍽️ Food & Drink](#-food--drink)
- [🎮 Games & Comics](#-games--comics)
- [🌍 Geocoding](#-geocoding)
- [❤️ Health](#health)
- [🧠 Machine Learning](#-machine-learning)
- [🎵 Music](#-music)
- [📰 News](#-news)
- [📸 Photography](#-photography)
- [🔬 Science](#-science)
- [🛍️ Shopping](#shopping)
- [💬 Social](#-social)
- [🚆 Transportation](#transportation)
- [🌤️ Weather](#weather)

---

## 🐶 Animals

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AdoptAPet** | Resource to help get pets adopted. | 🔑 ApiKey | ✅ | [Link](https://www.adoptapet.com/public/apis/pet_list.html) |
| **Axolotl** | Collection of axolotl pictures and facts. | No | ✅ | [Link](https://theaxolotlapi.netlify.app/) |
| **Cat Facts** | Daily cat facts. | No | ✅ | [Link](https://alexwohlbruck.github.io/cat-facts/) |
| **Cataas** | Cat as a service (cats pictures and gifs). | No | ✅ | [Link](https://cataas.com/) |
| **Cats** | Pictures of cats from Tumblr. | 🔑 ApiKey | ✅ | [Link](https://docs.thecatapi.com/) |
| **Dog Facts** | Random dog facts. | No | ✅ | [Link](https://dukengn.github.io/Dog-facts-API/) |
| **Dogs** | Based on the Stanford Dogs Dataset. | No | ✅ | [Link](https://dog.ceo/dog-api/) |
| **eBird** | Retrieve recent or notable birding observations within a region. | 🔑 ApiKey | ✅ | [Link](https://documenter.getpostman.com/view/664302/S1ENwy59) |
| **FishWatch** | Information and pictures about individual fish species. | No | ✅ | [Link](https://www.fishwatch.gov/developers) |
| **HTTP Cat** | Cat for every HTTP Status. | No | ✅ | [Link](https://http.cat/) |
| **HTTP Dog** | Dogs for every HTTP response status code. | No | ✅ | [Link](https://http.dog/) |
| **IUCN** | IUCN Red List of Threatened Species. | 🔑 ApiKey | No | [Link](http://apiv3.iucnredlist.org/api/v3/docs) |
| **MeowFacts** | Get random cat facts. | No | ✅ | [Link](https://github.com/wh-iterabb-it/meowfacts) |
| **Movebank** | Movement and Bio-logging Data. | No | ✅ | [Link](https://github.com/movebank/movebank-api-doc) |
| **Petfinder** | Pet adoption data. | 🔑 ApiKey | ✅ | [Link](https://www.petfinder.com/developers/) |
| **PlaceBear** | Placeholder bear pictures. | No | ✅ | [Link](https://placebear.com/) |
| **PlaceDog** | Placeholder Dog pictures. | No | ✅ | [Link](https://place.dog) |
| **PlaceKitten** | Placeholder Kitten pictures. | No | ✅ | [Link](https://placekitten.com/) |
| **RandomDog** | Random pictures of dogs. | No | ✅ | [Link](https://random.dog/woof.json) |
| **RandomDuck** | Random pictures of ducks. | No | ✅ | [Link](https://random-d.uk/api) |
| **RandomFox** | Random pictures of foxes. | No | ✅ | [Link](https://randomfox.ca/floof/) |
| **RescueGroups** | Adoption. | No | ✅ | [Link](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) |
| **Shibe.Online** | Random pictures of Shiba Inu, cats or birds. | No | ✅ | [Link](http://shibe.online/) |
| **The Dog** | A public service all about Dogs, free to use. | 🔑 ApiKey | ✅ | [Link](https://thedogapi.com/) |
| **xeno-canto** | Bird sounds from around the world. | No | ✅ | [Link](https://xeno-canto.org/explore/api) |
| **Zoo Animals** | Facts and pictures of zoo animals. | No | ✅ | [Link](https://zoo-animal-api.herokuapp.com/) |

## 🌸 Anime

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AniAPI** | Anime discovery, streaming & syncing with trackers. | 🔐 OAuth | ✅ | [Link](https://aniapi.com/docs/) |
| **AniDB** | Anime Database. | 🔑 ApiKey | No | [Link](https://wiki.anidb.net/HTTP_API_Definition) |
| **AniList** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://github.com/AniList/ApiV2-GraphQL-Docs) |
| **AnimeChan** | Anime quotes (over 10k+). | No | ✅ | [Link](https://github.com/RocktimSaikia/anime-chan) |
| **AnimeFacts** | Anime facts (over 100+). | No | ✅ | [Link](https://chandan-02.github.io/anime-facts-rest-api/) |
| **AnimeNewsNetwork** | Anime industry news. | No | ✅ | [Link](https://www.animenewsnetwork.com/encyclopedia/api.php) |
| **Catboy** | Neko images, funny GIFs and more. | No | ✅ | [Link](https://catboys.com/api) |
| **Danbooru Anime** | Thousands of anime artist database. | 🔑 ApiKey | ✅ | [Link](https://danbooru.donmai.us/wiki_pages/help:api) |
| **Jikan** | Unofficial MyAnimeList API. | No | ✅ | [Link](https://jikan.moe) |
| **Kitsu** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://kitsu.docs.apiary.io/) |
| **MangaDex** | Manga Database and Community. | 🔑 ApiKey | ✅ | [Link](https://api.mangadex.org/docs.html) |
| **Mangapi** | Translate manga pages. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/pierre.carcellermeunier/api/mangapi3/) |
| **MyAnimeList** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://myanimelist.net/clubs.php?cid=13727) |
| **NekosBest** | Neko Images & Anime GIFs. | No | ✅ | [Link](https://docs.nekos.best) |
| **Shikimori** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://shikimori.one/api/doc) |
| **Studio Ghibli** | Resources from Studio Ghibli films. | No | ✅ | [Link](https://ghibliapi.herokuapp.com) |
| **Trace Moe** | Anime Scene Search Engine. | No | ✅ | [Link](https://soruly.github.io/trace.moe-api/#/) |
| **Waifu.im** | Get waifu pictures. | No | ✅ | [Link](https://waifu.im/docs) |
| **Waifu.pics** | Image sharing platform for anime images. | No | ✅ | [Link](https://waifu.pics/docs) |

## <a id="anti-malware"></a>🛡️ Anti-Malware

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AbuseIPDB** | IP/Domain/URL reputation. | 🔑 ApiKey | ✅ | [Link](https://docs.abuseipdb.com/) |
| **AlienVault OTX** | IP/Domain/URL reputation. | 🔑 ApiKey | ✅ | [Link](https://otx.alienvault.com/api) |
| **CAPEsandbox** | Malware analysis. | 🔑 ApiKey | ✅ | [Link](https://capev2.readthedocs.io/en/latest/usage/api.html) |
| **Google Safe Browsing** | Google Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/safe-browsing/) |
| **MalDatabase** | Malware analysis. | 🔑 ApiKey | ✅ | [Link](https://maldatabase.com/api-doc.html) |
| **MalShare** | Malware analysis. | 🔑 ApiKey | ✅ | [Link](https://malshare.com/doc.php) |
| **MalwareBazaar** | Malware analysis. | 🔑 ApiKey | ✅ | [Link](https://bazaar.abuse.ch/api/) |
| **Metacert** | Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://metacert.com/) |
| **NoPhishy** | Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/Amiichu/api/exerra-phishing-check/) |
| **Phisherman** | Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://phisherman.gg/) |
| **Scanii** | File/Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://docs.scanii.com/) |
| **URLhaus** | Link/Domain reputation. | No | ✅ | [Link](https://urlhaus-api.abuse.ch/) |
| **URLScan.io** | Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://urlscan.io/about-api/) |
| **VirusTotal** | File/URL analysis. | 🔑 ApiKey | ✅ | [Link](https://www.virustotal.com/en/documentation/public-api/) |
| **Web of Trust** | IP/Domain/URL reputation. | 🔑 ApiKey | ✅ | [Link](https://support.mywot.com/hc/en-us/sections/360004477734-API-) |

## 📚 Books

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Google Books** | Search and preview books. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/books/) |
| **Gutendex** | Project Gutenberg books. | No | ✅ | [Link](https://gutendex.com/) |
| **Open Library** | Books, covers, and related data. | No | ✅ | [Link](https://openlibrary.org/developers/api) |
| **Penguin Publishing** | Book data. | No | ✅ | [Link](http://www.penguinrandomhouse.biz/webservices/rest/) |

## 🪙 Cryptocurrency

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **0x** | API for querying the 0x protocol. | No | ✅ | [Link](https://0x.org/api) |
| **1inch** | API for querying the 1inch protocol. | No | ✅ | [Link](https://1inch.io/api/) |
| **Alchemy** | Ethereum API. | 🔑 ApiKey | ✅ | [Link](https://docs.alchemy.com/alchemy/) |
| **Binance** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://github.com/binance/binance-spot-api-docs) |
| **Bitfinex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.bitfinex.com/docs) |
| **Bitmex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://www.bitmex.com/app/apiOverview) |
| **Bittrex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://bittrex.github.io/api/v3) |
| **Block** | Bitcoin Payment, Wallet & Transaction Data. | 🔑 ApiKey | ✅ | [Link](https://block.io/docs/basic) |
| **Blockchain** | Bitcoin Payment, Wallet & Transaction Data. | 🔑 ApiKey | ✅ | [Link](https://www.blockchain.com/api) |
| **CoinAPI** | Market Data API. | 🔑 ApiKey | ✅ | [Link](https://docs.coinapi.io/) |
| **Coinbase** | Bitcoin, Bitcoin Cash, Litecoin and Ethereum. | 🔑 ApiKey | ✅ | [Link](https://developers.coinbase.com) |
| **CoinGecko** | Cryptocurrency prices, market cap, exchange rates. | No | ✅ | [Link](http://www.coingecko.com/api) |
| **CoinMarketCap** | Cryptocurrency prices, market cap, exchange rates. | 🔑 ApiKey | ✅ | [Link](https://coinmarketcap.com/api/) |
| **Coinlayer** | Real-time Crypto Exchange Rates. | 🔑 ApiKey | ✅ | [Link](https://coinlayer.com) |
| **CryptoCompare** | Cryptocurrencies Comparison. | No | ✅ | [Link](https://www.cryptocompare.com/api) |
| **FTX** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.ftx.com/) |
| **Gateio** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://www.gate.io/api2) |
| **Gemini** | Exchange for Trading Cryptocurrencies. | No | ✅ | [Link](https://docs.gemini.com/rest-api/) |
| **Kraken** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.kraken.com/rest/) |
| **KuCoin** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.kucoin.com/) |
| **Mempool** | Bitcoin API. | No | ✅ | [Link](https://mempool.space/api) |
| **Nomics** | Cryptocurrency Market Data. | 🔑 ApiKey | ✅ | [Link](https://nomics.com/docs/) |
| **Poloniex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.poloniex.com) |

## 💻 Development

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **24 Pull Requests** | Project to promote open source collaboration during December. | No | ✅ | [Link](https://24pullrequests.com/api) |
| **Abstract Screenshot** | Take a screenshot of any website. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/website-screenshot-api) |
| **Agify.io** | Predict the age of a person based on their name. | No | ✅ | [Link](https://agify.io) |
| **ApiFlash** | Chrome based screenshot API. | 🔑 ApiKey | ✅ | [Link](https://apiflash.com/) |
| **APIs.guru** | Wikipedia for Web APIs. | No | ✅ | [Link](https://apis.guru/api-doc/) |
| **APILayer** | Marketplace for various APIs. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/) |
| **Azure DevOps** | DevOps tools. | 🔑 ApiKey | ✅ | [Link](https://docs.microsoft.com/en-us/rest/api/azure/devops) |
| **Bitbucket** | Git solution. | 🔐 OAuth | ✅ | [Link](https://developer.atlassian.com/bitbucket/api/2/reference/) |
| **Bored** | Let's find you something to do. | No | ✅ | [Link](https://www.boredapi.com/) |
| **CDNJS** | Library info. | No | ✅ | [Link](https://api.cdnjs.com/libraries/jquery) |
| **Cloudflare Trace** | Get IP Address and other info. | No | ✅ | [Link](https://github.com/fawazahmed0/cloudflare-trace-api) |
| **Docker Hub** | Interact with Docker Hub. | 🔑 ApiKey | ✅ | [Link](https://docs.docker.com/docker-hub/api/latest/) |
| **Genderize.io** | Predict the gender of a person based on their name. | No | ✅ | [Link](https://genderize.io) |
| **GitHub** | Make use of GitHub data. | 🔐 OAuth | ✅ | [Link](https://docs.github.com/en/free-pro-team@latest/rest) |
| **Gitlab** | Automate GitLab. | 🔐 OAuth | ✅ | [Link](https://docs.gitlab.com/ee/api/) |
| **Google Docs** | Create and edit documents. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/docs/api/reference/rest) |
| **Google Sheets** | Read and write to Google Sheets. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/sheets/api/reference/rest) |
| **Heroku** | PaaS. | 🔐 OAuth | ✅ | [Link](https://devcenter.heroku.com/articles/platform-api-reference/) |
| **Host.io** | Domains Data. | 🔑 ApiKey | ✅ | [Link](https://host.io) |
| **Hunter** | Email Verifier. | 🔑 ApiKey | ✅ | [Link](https://hunter.io/api) |
| **IPify** | A simple IP Address API. | No | ✅ | [Link](https://www.ipify.org/) |
| **IPinfo** | IP Address Information. | No | ✅ | [Link](https://ipinfo.io/developers) |
| **Ipstack** | Locate and identify website visitors by IP address. | 🔑 ApiKey | ✅ | [Link](https://ipstack.com/) |
| **JSONbin.io** | Free JSON storage. | 🔑 ApiKey | ✅ | [Link](https://jsonbin.io) |
| **Netlify** | Netlify API. | 🔐 OAuth | ✅ | [Link](https://docs.netlify.com/api/get-started/) |
| **Positionstack** | Forward & Reverse Geocoding. | 🔑 ApiKey | ✅ | [Link](https://positionstack.com/) |
| **Serpstack** | Real-Time Google Search Results. | 🔑 ApiKey | ✅ | [Link](https://serpstack.com/) |
| **Userstack** | User-Agent String Analysis. | 🔑 ApiKey | ✅ | [Link](https://userstack.com/) |
| **Aviationstack** | Real-time flight status and global aviation data. | 🔑 ApiKey | ✅ | [Link](https://aviationstack.com/) |
| **Mailboxlayer** | Email verification and validation. | 🔑 ApiKey | ✅ | [Link](https://mailboxlayer.com/) |
| **Numverify** | Phone number validation. | 🔑 ApiKey | ✅ | [Link](https://numverify.com/) |
| **Pdflayer** | HTML to PDF conversion. | 🔑 ApiKey | ✅ | [Link](https://pdflayer.com/) |
| **Screenshotlayer** | Website screenshots. | 🔑 ApiKey | ✅ | [Link](https://screenshotlayer.com/) |

## 💰 Finance

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Alpaca** | Commission-free stock trading. | 🔑 ApiKey | ✅ | [Link](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/) |
| **Alpha Vantage** | Realtime and historical stock data. | 🔑 ApiKey | ✅ | [Link](https://www.alphavantage.co/) |
| **Binlist** | BIN/IIN Lookup. | No | ✅ | [Link](https://binlist.net/) |
| **Currencylayer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://currencylayer.com/) |
| **Exchangeratesapi** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://exchangeratesapi.io/) |
| **Financial Modeling Prep** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://site.financialmodelingprep.com/developer/docs) |
| **Finnhub** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://finnhub.io/docs/api) |
| **Fixer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://fixer.io/) |
| **FRED** | Economic data. | 🔑 ApiKey | ✅ | [Link](https://fred.stlouisfed.org/docs/api/fred/) |
| **IEX Cloud** | Financial data. | 🔑 ApiKey | ✅ | [Link](https://iexcloud.io/docs/api/) |
| **Klarna** | Payments. | 🔑 ApiKey | ✅ | [Link](https://docs.klarna.com/klarna-payments/api/payments-api/) |
| **MercadoPago** | Payments. | 🔑 ApiKey | ✅ | [Link](https://www.mercadopago.com.br/developers/es/reference) |
| **Plaid** | Connect bank accounts. | 🔑 ApiKey | ✅ | [Link](https://www.plaid.com/docs) |
| **Polygon** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://polygon.io/) |
| **Stripe** | Payments. | 🔑 ApiKey | ✅ | [Link](https://stripe.com/docs/api) |
| **Tax Data API** | Tax rates and validation. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/tax_data-api) |
| **Yahoo Finance** | Financial data. | 🔑 ApiKey | ✅ | [Link](https://www.yahoofinanceapi.com/) |
| **Exchangerate.host** | Foreign exchange & crypto rates. | 🔑 ApiKey | ✅ | [Link](https://exchangerate.host/) |

## 🍔 Food & Drink

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Open Food Facts** | Food product data. | No | ✅ | [Link](https://world.openfoodfacts.org/data) |
| **PunkAPI** | Brewdog beer recipes. | No | ✅ | [Link](https://punkapi.com/) |
| **TheCocktailDB** | Cocktail recipes. | 🔑 ApiKey | ✅ | [Link](https://www.thecocktaildb.com/api.php) |
| **TheMealDB** | Meal recipes. | 🔑 ApiKey | ✅ | [Link](https://www.themealdb.com/api.php) |

## 🎮 Entertainment

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **OMDb** | Open Movie Database. | 🔑 ApiKey | ✅ | [Link](http://www.omdbapi.com/) |
| **Simkl** | Movies, TV, Anime metadata. | 🔑 ApiKey | ✅ | [Link](https://simkl.com/apidoc/) |
| **TMDb** | The Movie Database. | 🔑 ApiKey | ✅ | [Link](https://developers.themoviedb.org/3) |
| **Trakt** | TV and Movie tracking. | 🔐 OAuth | ✅ | [Link](https://trakt.docs.apiary.io/) |
| **Watchmode** | Streaming availability. | 🔑 ApiKey | ✅ | [Link](https://api.watchmode.com/) |

## 🌍 Geocoding

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **IP-API** | IP to location. | No | No | [Link](https://ip-api.com/docs) |
| **Mapbox** | Maps and geocoding. | 🔑 ApiKey | ✅ | [Link](https://docs.mapbox.com/) |
| **Nominatim** | OpenStreetMap Geocoding. | No | ✅ | [Link](https://nominatim.org/release-docs/latest/api/Overview/) |
| **OpenStreetMap** | Map data. | 🔐 OAuth | ✅ | [Link](http://wiki.openstreetmap.org/wiki/API) |

## 🎮 Games & Comics

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Age of Empires II** | Game data. | No | ✅ | [Link](https://age-of-empires-2-api.herokuapp.com) |
| **AmiiboAPI** | Nintendo Amiibo data. | No | ✅ | [Link](https://amiiboapi.com/) |
| **Battle.net** | Blizzard games data. | 🔐 OAuth | ✅ | [Link](https://develop.battle.net/documentation/guides/getting-started) |
| **Brawl Stars** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.brawlstars.com) |
| **Chuck Norris Database** | Jokes. | No | No | [Link](http://www.icndb.com/api/) |
| **Clash of Clans** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.clashofclans.com) |
| **Clash Royale** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.clashroyale.com) |
| **Deck of Cards** | Deck of cards. | No | No | [Link](http://deckofcardsapi.com/) |
| **Dota 2** | Game data. | 🔑 ApiKey | ✅ | [Link](https://docs.opendota.com/) |
| **Dungeons and Dragons** | 5th Edition SRD. | No | ✅ | [Link](https://www.dnd5eapi.co/docs/) |
| **Eve Online** | Game data. | 🔐 OAuth | ✅ | [Link](https://esi.evetech.net/ui) |
| **Final Fantasy XIV** | Game data. | No | ✅ | [Link](https://xivapi.com/) |
| **Fortnite** | Game data. | 🔑 ApiKey | ✅ | [Link](https://fortnitetracker.com/site-api) |
| **Genshin Impact** | Game data. | No | ✅ | [Link](https://genshin.dev) |
| **Guild Wars 2** | Game data. | 🔑 ApiKey | ✅ | [Link](https://wiki.guildwars2.com/wiki/API:Main) |
| **Hypixel** | Minecraft server data. | 🔑 ApiKey | ✅ | [Link](https://api.hypixel.net/) |
| **IGDB.com** | Game database. | 🔑 ApiKey | ✅ | [Link](https://api-docs.igdb.com) |
| **JokeAPI** | Programming and general jokes. | No | ✅ | [Link](https://sv443.net/jokeapi/v2/) |
| **Lichess** | Chess data. | 🔐 OAuth | ✅ | [Link](https://lichess.org/api) |
| **Marvel** | Comics data. | 🔑 ApiKey | ✅ | [Link](https://developer.marvel.com) |
| **Minecraft Server Status** | Server status. | No | ✅ | [Link](https://api.mcsrvstat.us) |
| **Mojang** | Minecraft data. | 🔑 ApiKey | ✅ | [Link](https://wiki.vg/Mojang_API) |
| **Open Trivia** | Trivia questions. | No | ✅ | [Link](https://opentdb.com/api_config.php) |
| **Pokéapi** | Pokémon data. | No | ✅ | [Link](https://pokeapi.co) |
| **PUBG** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.pubg.com/) |
| **Rick and Morty** | Show data. | No | ✅ | [Link](https://rickandmortyapi.com) |
| **Riot Games** | League of Legends data. | 🔑 ApiKey | ✅ | [Link](https://developer.riotgames.com/) |
| **Steam** | Steam data. | 🔑 ApiKey | ✅ | [Link](https://steamcommunity.com/dev) |

## <a id="health"></a>❤️ Health

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BMI Calculator** | Calculate BMI and other metrics. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/navii/api/bmi-calculator/) |
| **Covid-19** | Global COVID-19 data. | No | ✅ | [Link](https://covid19api.com/) |
| **Edamam Nutrition** | Nutrition analysis. | 🔑 ApiKey | ✅ | [Link](https://developer.edamam.com/edamam-nutrition-api) |
| **Nutritionix** | Nutrition database. | 🔑 ApiKey | ✅ | [Link](https://developer.nutritionix.com/) |

## 🧠 Machine Learning

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Clarifai** | Computer Vision. | 🔐 OAuth | ✅ | [Link](https://docs.clarifai.com/api-guide/api-overview) |
| **Cloudmersive** | Image Recognition. | 🔑 ApiKey | ✅ | [Link](https://www.cloudmersive.com/image-recognition-and-processing-api) |
| **DeepAI** | AI tools. | 🔑 ApiKey | ✅ | [Link](https://deepai.org/api-docs) |
| **Dialogflow** | Conversational AI. | 🔑 ApiKey | ✅ | [Link](https://cloud.google.com/dialogflow/docs/) |
| **Imagga** | Image Recognition. | 🔑 ApiKey | ✅ | [Link](https://imagga.com/) |
| **NLP Cloud** | NLP. | 🔑 ApiKey | ✅ | [Link](https://nlpcloud.io) |
| **OpenAI** | GPT-3, DALL-E. | 🔑 ApiKey | ✅ | [Link](https://beta.openai.com/docs/) |
| **Roboflow** | Computer Vision. | 🔑 ApiKey | ✅ | [Link](https://universe.roboflow.com) |
| **WolframAlpha** | Computational Knowledge. | 🔑 ApiKey | ✅ | [Link](https://products.wolframalpha.com/api/) |
| **Languagelayer** | Language detection. | 🔑 ApiKey | ✅ | [Link](https://languagelayer.com/) |

## 🎵 Music

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Audiomack** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://www.audiomack.com/data-api/docs) |
| **Bandcamp** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://bandcamp.com/developer) |
| **Deezer** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://developers.deezer.com/api) |
| **Discogs** | Music database. | 🔐 OAuth | ✅ | [Link](https://www.discogs.com/developers/) |
| **Genius** | Lyrics and knowledge. | 🔐 OAuth | ✅ | [Link](https://docs.genius.com/) |
| **LastFm** | Music database. | 🔑 ApiKey | ✅ | [Link](https://www.last.fm/api) |
| **Mixcloud** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://www.mixcloud.com/developers/) |
| **MusicBrainz** | Music database. | No | ✅ | [Link](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) |
| **Musixmatch** | Lyrics. | 🔑 ApiKey | ✅ | [Link](https://developer.musixmatch.com/) |
| **SoundCloud** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://developers.soundcloud.com/docs/api/guide) |
| **Spotify** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://beta.developer.spotify.com/documentation/web-api/) |

## 📰 News

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Currents** | Latest news. | 🔑 ApiKey | ✅ | [Link](https://currentsapi.services/en) |
| **GNews** | Global news search. | 🔑 ApiKey | ✅ | [Link](https://gnews.io/) |
| **NewsAPI** | Headlines and articles. | 🔑 ApiKey | ✅ | [Link](https://newsapi.org/) |
| **NewsData.io** | News search and tracking. | 🔑 ApiKey | ✅ | [Link](https://newsdata.io/) |
| **The Guardian** | Guardian articles. | 🔑 ApiKey | ✅ | [Link](https://open-platform.theguardian.com/) |

## 📷 Photography

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Giphy** | GIFs. | � ApiKey | ✅ | [Link](https://developers.giphy.com/docs/) |
| **Lorem Picsum** | Placeholder images. | No | ✅ | [Link](https://picsum.photos/) |
| **Pexels** | Free stock photos. | 🔑 ApiKey | ✅ | [Link](https://www.pexels.com/api/) |
| **Unsplash** | High-quality photos. | 🔐 OAuth | ✅ | [Link](https://unsplash.com/developers) |

## �🔬 Science

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **NASA** | NASA data (APOD, Mars, etc.). | 🔑 ApiKey | ✅ | [Link](https://api.nasa.gov/) |
| **SpaceX** | SpaceX launch data. | No | ✅ | [Link](https://github.com/r-spacex/SpaceX-API) |

## <a id="shopping"></a>🛍️ Shopping

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Best Buy** | Retail data. | 🔑 ApiKey | ✅ | [Link](https://bestbuyapis.github.io/api-documentation/#overview) |
| **eBay** | Auction and retail. | 🔐 OAuth | ✅ | [Link](https://developer.ebay.com/) |
| **Etsy** | E-commerce. | 🔐 OAuth | ✅ | [Link](https://www.etsy.com/developers/documentation/getting_started/api_basics) |
| **Mercadolibre** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://developers.mercadolibre.cl/es_ar/api-docs-es) |
| **Shopee** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://open.shopee.com/documents?version=1) |
| **WooCommerce** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://woocommerce.github.io/woocommerce-rest-api-docs/) |

## 💬 Social

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Discord** | Chat platform. | 🔐 OAuth | ✅ | [Link](https://discord.com/developers/docs/intro) |
| **Facebook** | Social network. | 🔐 OAuth | ✅ | [Link](https://developers.facebook.com/) |
| **Instagram** | Photo sharing. | 🔐 OAuth | ✅ | [Link](https://www.instagram.com/developer/) |
| **LinkedIn** | Professional network. | 🔐 OAuth | ✅ | [Link](https://docs.microsoft.com/en-us/linkedin/?context=linkedin/context) |
| **Pinterest** | Visual discovery. | 🔐 OAuth | ✅ | [Link](https://developers.pinterest.com/) |
| **Reddit** | Social news. | 🔐 OAuth | ✅ | [Link](https://www.reddit.com/dev/api) |
| **Slack** | Team communication. | 🔐 OAuth | ✅ | [Link](https://api.slack.com/) |
| **Telegram** | Messaging app. | 🔑 ApiKey | ✅ | [Link](https://core.telegram.org/bots/api) |
| **TikTok** | Video sharing. | 🔐 OAuth | ✅ | [Link](https://developers.tiktok.com/doc/login-kit-web) |
| **Twitch** | Live streaming. | 🔐 OAuth | ✅ | [Link](https://dev.twitch.tv/docs) |
| **Twitter** | Microblogging. | 🔐 OAuth | ✅ | [Link](https://developer.twitter.com/en/docs) |
| **Viber** | Messaging app. | 🔑 ApiKey | ✅ | [Link](https://developers.viber.com/) |
| **WhatsApp** | Messaging app. | 🔐 OAuth | ✅ | [Link](https://developers.facebook.com/docs/whatsapp) |
| **Zalo** | Messaging and social platform. | 🔐 OAuth | ✅ | [Link](https://developers.zalo.me/) |
| **LINE** | Messaging app. | 🔐 OAuth | ✅ | [Link](https://developers.line.biz/en/) |

## <a id="transportation"></a>🚆 Transportation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BART** | Bay Area Rapid Transit. | 🔑 ApiKey | ✅ | [Link](http://api.bart.gov) |
| **OpenSky Network** | Flight tracking. | No | ✅ | [Link](https://opensky-network.org/apidoc/index.html) |
| **Transport for London** | Public transport data. | 🔑 ApiKey | ✅ | [Link](https://api.tfl.gov.uk) |

## <a id="weather"></a>🌤️ Weather

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **7Timer!** | Weather forecast. | No | No | [Link](http://www.7timer.info/doc.php?lang=en) |
| **AccuWeather** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://developer.accuweather.com/apis) |
| **OpenWeatherMap** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://openweathermap.org/api) |
| **RainViewer** | Weather radar. | No | ✅ | [Link](https://www.rainviewer.com/api.html) |
| **WeatherAPI** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://www.weatherapi.com/) |
| **Weatherbit** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://www.weatherbit.io/api) |
| **Weatherstack** | Real-time & historical world weather data. | 🔑 ApiKey | ✅ | [Link](https://weatherstack.com/) |
| **wttr.in** | Console-oriented weather. | No | ✅ | [Link](https://github.com/chubin/wttr.in) |

---

<div align="center">

**Don't forget to ⭐ this repo if you found it useful!**

</div>
