# 🚀 Awesome Dev APIs

> A curated collection of awesome free APIs for developers. Open source and community-driven.
> This repository aims to provide a comprehensive collection of free and freemium APIs to help you build your next project.

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/ThanhNguyxn/awesome-free-apis?style=social)](https://github.com/ThanhNguyxn/awesome-free-apis/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ThanhNguyxn/awesome-free-apis?style=social)](https://github.com/ThanhNguyxn/awesome-free-apis/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/ThanhNguyxn/awesome-free-apis)](https://github.com/ThanhNguyxn/awesome-free-apis/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ThanhNguyxn/awesome-free-apis)](https://github.com/ThanhNguyxn/awesome-free-apis/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square)](https://github.com/ThanhNguyxn/awesome-free-apis)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=ThanhNguyxn%2Fawesome-free-apis&countColor=%23263759&style=flat)](https://visitorbadge.io/status?path=ThanhNguyxn%2Fawesome-free-apis)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/thanhnguyxn)

</div>

---

## 📚 Code Examples

> **✨ New!** Check out [practical code examples](examples/) showing how to use popular APIs from this collection.  
> Includes Python & JavaScript examples for Pokemon, Cryptocurrency, AI Chat, and more!

---

## <a id="general-api-usage-guide"></a>📘 General API Usage Guide

> **👋 New to APIs?** Don't worry! This guide will help you understand the basics and get started quickly.

---

### 💡 What is an API?

**API** stands for **Application Programming Interface**. It's a way for different applications to communicate with each other.

```
┌─────────┐      ┌─────────┐      ┌─────────┐
│   YOU   │ ───▶│   API   │ ───▶ │ SERVER  │
│  (App)  │ ◀───│ (Waiter)│ ◀─── │(Kitchen)│
└─────────┘      └─────────┘      └─────────┘
   Request         Process          Response
```

**Think of it like a restaurant:**
- 🙋 **You** (the app) place an order
- 🍽️ **Waiter** (the API) takes your request to the kitchen
- 👨‍🍳 **Kitchen** (the server) prepares your food (data)
- ✨ The waiter brings it back to you!

---

### 📝 Authentication Methods

Different APIs have different ways to verify who you are:

| Method | Icon | Description | Example |
|--------|------|-------------|---------|
| **No Auth** | 🌐 | Open for everyone - just call it! | Weather APIs, public data |
| **API Key** | 🔑 | Secret code you get when registering | `?api_key=abc123` or `Authorization: abc123` |
| **OAuth** | 🔐 | Secure login (like "Login with Google") | Social media integrations |

**💡 Pro Tip:** Always keep your API keys secret! Never commit them to GitHub.

---

### 📡 HTTP Request Methods

Learn the common ways to interact with APIs:

| Method | Icon | Purpose | Real-World Example |
|--------|------|---------|-------------------|
| `GET` | 📥 | **Retrieve** data | Get a list of cat pictures |
| `POST` | 📤 | **Create** new data | Upload a new photo |
| `PUT` | ✏️ | **Replace** existing data | Update entire user profile |
| `PATCH` | 🔧 | **Modify** specific fields | Change just your username |
| `DELETE` | 🗑️ | **Remove** data | Delete a comment |

**Example GET Request:**
```bash
curl https://api.example.com/cats
```

**Example POST Request:**
```bash
curl -X POST https://api.example.com/cats \
  -H "Content-Type: application/json" \
  -d '{"name":"Fluffy","age":3}'
```

---

### 🚦 HTTP Status Codes

The API responds with a status code to tell you what happened:

#### ✅ Success Codes (2xx)
| Code | Icon | Meaning |
|------|------|---------|
| `200` | ✅ | **OK** - Request succeeded! |
| `201` | 🎉 | **Created** - New resource created! |
| `204` | 📭 | **No Content** - Success but no data to return |

#### ⚠️ Client Error Codes (4xx)
| Code | Icon | Meaning | What to Do |
|------|------|---------|-----------|
| `400` | ❌ | **Bad Request** - Invalid syntax | Check your request format |
| `401` | 🔒 | **Unauthorized** - Authentication required | Add your API key |
| `403` | 🚫 | **Forbidden** - You don't have permission | Check your access rights |
| `404` | 🔍 | **Not Found** - Resource doesn't exist | Verify the URL |
| `429` | 🐌 | **Too Many Requests** - Rate limit hit | Wait and try again |

#### 🔴 Server Error Codes (5xx)
| Code | Icon | Meaning |
|------|------|---------|
| `500` | 💥 | **Internal Server Error** - API is broken |
| `503` | 🔧 | **Service Unavailable** - API is down |

---

### 🛠️ Essential Tools for Testing APIs

| Tool | Best For | Platform | Free? |
|------|----------|----------|-------|
| [**Postman**](https://www.postman.com/) | 🎯 Complete API testing & documentation | Desktop/Web | ✅ Yes (free tier) |
| [**Thunder Client**](https://www.thunderclient.com/) | ⚡ Lightweight testing in VS Code | VS Code Extension | ✅ Yes |
| [**cURL**](https://curl.se/) | 💻 Command-line requests | Terminal | ✅ Yes (built-in) |
| [**Insomnia**](https://insomnia.rest/) | 🎨 Beautiful UI for API testing | Desktop | ✅ Yes |

---

### 🚀 Quick Start Example

Let's try a real API call! Here's how to get a random cat fact:

**1️⃣ Using cURL (Terminal):**
```bash
curl https://catfact.ninja/fact
```

**2️⃣ Using JavaScript (Browser):**
```javascript
fetch('https://catfact.ninja/fact')
  .then(response => response.json())
  .then(data => console.log(data.fact));
```

**3️⃣ Using Python:**
```python
import requests
response = requests.get('https://catfact.ninja/fact')
print(response.json()['fact'])
```

**📦 Expected Response:**
```json
{
  "fact": "Cats have 32 muscles in each ear.",
  "length": 38
}
```

---

### 📚 Additional Resources

- 📖 [What is REST API?](https://www.redhat.com/en/topics/api/what-is-a-rest-api) - RedHat Guide
- 🎓 [HTTP Status Codes Cheat Sheet](https://httpstatuses.com/) - Quick reference
- 🧪 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Free fake API for practice
- 💬 [API Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/) - Stack Overflow Blog

---

## 📖 Table of Contents

- [📘 General Usage Guide](#general-api-usage-guide)
- [🐶 Animals](#animals)
- [🌸 Anime](#anime)
- [🛡️ Anti-Malware](#anti-malware)
- [📚 Books & Literature](#books)
- [🪙 Cryptocurrency](#cryptocurrency)
- [💻 Development](#development)
- [📖 Dictionaries](#dictionaries)
- [🎓 Education](#education)
- [📊 Public Data & Datasets](#public-data)
- [📧 Email & SMS](#email-sms)
- [🎮 Entertainment](#entertainment)
- [💰 Finance](#finance)
- [🍔 Food & Drink](#food-drink)
- [🎮 Games & Comics](#games-comics)
- [🌍 Geocoding](#geocoding)
- [❤️ Health](#health)
- [🧠 Machine Learning](#machine-learning)
- [🧪 Mock Data & Testing](#mock-data-testing)
- [🎵 Music](#music)
- [📰 News](#news)
- [📸 Photography](#photography)
- [🔬 Science](#science)
- [🔒 Security & Validation](#security-validation)
- [🛍️ Shopping](#shopping)
- [🔧 Utilities & Tools](#utilities-tools)
- [💬 Social](#social)
- [⚽ Sports](#sports)
- [🎨 Design & Colors](#design-colors)
- [🌎 Geography & Countries](#geography-countries)
- [🚆 Transportation](#transportation)
- [⚠️ Unofficial & Community APIs](#unofficial-community)
- [😂 Memes & Fun](#memes-fun)
- [💼 Jobs & Career](#jobs-career)
- [🌤️ Weather](#weather)

---

## <a id="animals"></a>🐶 Animals

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
| **PlaceBear** | Placeholder bear pictures. | No | ✅ | [Link](https://placebear.com/) |
| **RandomDog** | Random pictures of dogs. | No | ✅ | [Link](https://random.dog/woof.json) |
| **RandomDuck** | Random pictures of ducks. | No | ✅ | [Link](https://random-d.uk/api) |
| **RandomFox** | Random pictures of foxes. | No | ✅ | [Link](https://randomfox.ca/floof/) |
| **RescueGroups** | Adoption. | No | ✅ | [Link](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) |
| **Shibe.Online** | Random pictures of Shiba Inu, cats or birds. | No | ✅ | [Link](http://shibe.online/) |
| **The Cat API** | Images of cats (great for testing image grids). | 🔑 ApiKey | ✅ | [Link](https://thecatapi.com/) |
| **The Dog** | A public service all about Dogs, free to use. | 🔑 ApiKey | ✅ | [Link](https://thedogapi.com/) |
| **The Dog API** | Images and data about dogs. | 🔑 ApiKey | ✅ | [Link](https://thedogapi.com/) |
| **TheCatDB** | Cat breeds and facts database. | 🔑 ApiKey | ✅ | [Link](https://www.thecatapi.com/) |
| **Dog CEO** | Dog breeds and random dog images. | No | ✅ | [Link](https://dog.ceo/dog-api/) |
| **xeno-canto** | Bird sounds from around the world. | No | ✅ | [Link](https://xeno-canto.org/explore/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="anime"></a>🌸 Anime

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AniAPI** | Anime discovery, streaming & syncing with trackers. | 🔐 OAuth | ✅ | [Link](https://aniapi.com/docs/) |
| **AniDB** | Anime Database. | 🔑 ApiKey | No | [Link](https://wiki.anidb.net/HTTP_API_Definition) |
| **AniList** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://github.com/AniList/ApiV2-GraphQL-Docs) |
| **AnimeChan** | Anime quotes (over 10k+). | No | ✅ | [Link](https://github.com/RocktimSaikia/anime-chan) |
| **AnimeFacts** | Anime facts (over 100+). | No | ✅ | [Link](https://chandan-02.github.io/anime-facts-rest-api/) |
| **AnimeNewsNetwork** | Anime industry news. | No | ✅ | [Link](https://www.animenewsnetwork.com/encyclopedia/api.php) |
| **Danbooru Anime** | Thousands of anime artist database. | 🔑 ApiKey | ✅ | [Link](https://danbooru.donmai.us/wiki_pages/help:api) |
| **Jikan** | Unofficial MyAnimeList API. | No | ✅ | [Link](https://jikan.moe) |
| **Kitsu** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://kitsu.docs.apiary.io/) |
| **Mangapi** | Translate manga pages. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/pierre.carcellermeunier/api/mangapi3/) |
| **MyAnimeList** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://myanimelist.net/clubs.php?cid=13727) |
| **NekosBest** | Neko Images & Anime GIFs. | No | ✅ | [Link](https://docs.nekos.best) |
| **Shikimori** | Anime and Manga Database. | 🔐 OAuth | ✅ | [Link](https://shikimori.one/api/doc) |
| **Studio Ghibli** | Resources from Studio Ghibli films. | No | ✅ | [Link](https://ghibliapi.vercel.app) |
| **Trace Moe** | Anime Scene Search Engine. | No | ✅ | [Link](https://soruly.github.io/trace.moe-api/#/) |
| **Waifu.im** | API for serving anime images (versatile query options). | No | ✅ | [Link](https://waifu.im/) |
| **Waifu.pics** | Image sharing platform for anime images. | No | ✅ | [Link](https://waifu.pics/docs) |
| **Kitsu Anime** | Discover anime and manga (**No Auth**). | No | ✅ | [Link](https://kitsu.docs.apiary.io/#) |

[⬆ Back to Table of Contents](#-table-of-contents)

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
| **Scanii** | File/Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://docs.scanii.com/) |
| **URLhaus** | Link/Domain reputation. | No | ✅ | [Link](https://urlhaus-api.abuse.ch/) |
| **URLScan.io** | Link/Domain reputation. | 🔑 ApiKey | ✅ | [Link](https://urlscan.io/about-api/) |
| **VirusTotal** | File/URL analysis. | 🔑 ApiKey | ✅ | [Link](https://www.virustotal.com/en/documentation/public-api/) |
| **Web of Trust** | IP/Domain/URL reputation. | 🔑 ApiKey | ✅ | [Link](https://support.mywot.com/hc/en-us/sections/360004477734-API-) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="books"></a>📚 Books & Literature

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Google Books** | Search and preview books. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/books/) |
| **Gutendex** | JSON API for Project Gutenberg (public domain books). | No | ✅ | [Link](https://gutendex.com/) |
| **Open Library** | Fetch data about millions of books and covers. | No | ✅ | [Link](https://openlibrary.org/developers/api) |
| **Penguin Publishing** | Book data. | No | ✅ | [Link](http://www.penguinrandomhouse.biz/webservices/rest/) |
| **Bookcover** | Book cover images by ISBN (**No Auth**). | No | ✅ | [Link](http://openlibrary.org/dev/docs/api/covers) |
| **Goodreads** | Book reviews and ratings metadata. | 🔑 ApiKey | ✅ | [Link](https://www.goodreads.com/api) |
| **ISBNdb** | ISBN book database. | 🔑 ApiKey | ✅ | [Link](https://isbndb.com/apidocs/v2) |
| **Poetry DB** | Database with over 40,000 poems (**No Auth**). | No | ✅ | [Link](https://poetrydb.org/) |
| **Bible API** | Free Bible text in multiple versions (**No Auth**). | No | ✅ | [Link](https://bible-api.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="cryptocurrency"></a>🪙 Cryptocurrency

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **1inch** | API for querying the 1inch protocol. | No | ✅ | [Link](https://1inch.io/api/) |
| **Alchemy** | Ethereum API. | 🔑 ApiKey | ✅ | [Link](https://docs.alchemy.com/) |
| **Binance** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://github.com/binance/binance-spot-api-docs) |
| **Bitfinex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.bitfinex.com/docs) |
| **Bitmex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://www.bitmex.com/app/apiOverview) |
| **Block** | Bitcoin Payment, Wallet & Transaction Data. | 🔑 ApiKey | ✅ | [Link](https://block.io/docs/basic) |
| **Blockchain** | Bitcoin Payment, Wallet & Transaction Data. | 🔑 ApiKey | ✅ | [Link](https://www.blockchain.com/api) |
| **CoinAPI** | Market Data API. | 🔑 ApiKey | ✅ | [Link](https://docs.coinapi.io/) |
| **Coinbase** | Bitcoin, Bitcoin Cash, Litecoin and Ethereum. | 🔑 ApiKey | ✅ | [Link](https://developers.coinbase.com) |
| **CoinGecko** | Cryptocurrency prices, market cap, exchange rates. | No | ✅ | [Link](http://www.coingecko.com/api) |
| **CoinMarketCap** | Cryptocurrency prices, market cap, exchange rates. | 🔑 ApiKey | ✅ | [Link](https://coinmarketcap.com/api/) |
| **Coinlayer** | Real-time Crypto Exchange Rates. | 🔑 ApiKey | ✅ | [Link](https://coinlayer.com) |
| **CryptoCompare** | Cryptocurrencies Comparison. | No | ✅ | [Link](https://www.cryptocompare.com/api) |
| **Gateio** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://www.gate.io/api2) |
| **Gemini** | Exchange for Trading Cryptocurrencies. | No | ✅ | [Link](https://docs.gemini.com/rest-api/) |
| **Kraken** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.kraken.com/rest/) |
| **KuCoin** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.kucoin.com/) |
| **Mempool** | Bitcoin API. | No | ✅ | [Link](https://mempool.space/api) |
| **Poloniex** | Exchange for Trading Cryptocurrencies. | 🔑 ApiKey | ✅ | [Link](https://docs.poloniex.com) |
| **CoinCap** | Real-time cryptocurrency market data (**No Auth**). | No | ✅ | [Link](https://docs.coincap.io/) |
| **Messari** | Crypto research and data. | 🔑 ApiKey | ✅ | [Link](https://messari.io/api) |
| **CoinPaprika** | Cryptocurrency market data (**No Auth, generous limits**). | No | ✅ | [Link](https://api.coinpaprika.com/) |
| **Coinlore** | Cryptocurrency prices and market data (**No Auth**). | No | ✅ | [Link](https://www.coinlore.com/cryptocurrency-data-api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="development"></a>💻 Development

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **24 Pull Requests** | Project to promote open source collaboration during December. | No | ✅ | [Link](https://24pullrequests.com/api) |
| **Abstract Screenshot** | Take a screenshot of any website. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/website-screenshot-api) |
| **Agify.io** | Predict the age of a person based on their name. | No | ✅ | [Link](https://agify.io) |
| **Airtable** | API for cloud collaboration database (free tier available). | 🔑 ApiKey | ✅ | [Link](https://airtable.com/developers/web/api/introduction) |
| **ApiFlash** | Chrome based screenshot API. | 🔑 ApiKey | ✅ | [Link](https://apiflash.com/) |
| **APIs.guru** | Wikipedia for Web APIs. | No | ✅ | [Link](https://apis.guru/api-doc/) |
| **APILayer** | Marketplace for various APIs. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/) |
| **Appwrite** | Open source backend server (database, auth, storage, functions). | 🔑 ApiKey | ✅ | [Link](https://appwrite.io/docs) |
| **Auth0** | Authentication and authorization platform (free tier). | 🔐 OAuth | ✅ | [Link](https://auth0.com/docs/api) |
| **Aviationstack** | Real-time flight status and global aviation data. | 🔑 ApiKey | ✅ | [Link](https://aviationstack.com/) |
| **Azure DevOps** | DevOps tools. | 🔑 ApiKey | ✅ | [Link](https://docs.microsoft.com/en-us/rest/api/azure/devops) |
| **Bitbucket** | Git solution. | 🔐 OAuth | ✅ | [Link](https://developer.atlassian.com/bitbucket/api/2/reference/) |
| **Carbon** | Create and share beautiful code snippets. | No | ✅ | [Link](https://github.com/carbon-app/carbon) |
| **CDNJS** | Library info. | No | ✅ | [Link](https://api.cdnjs.com/libraries/jquery) |
| **Clerk** | User management and authentication (free tier). | 🔑 ApiKey | ✅ | [Link](https://clerk.com/docs/reference/backend-api) |
| **Cloudflare Trace** | Get IP Address and other info. | No | ✅ | [Link](https://github.com/fawazahmed0/cloudflare-trace-api) |
| **Codacy** | Code quality and security analysis. | 🔑 ApiKey | ✅ | [Link](https://api.codacy.com/api/api-docs) |
| **CodeSandbox** | Online code editor API. | 🔑 ApiKey | ✅ | [Link](https://codesandbox.io/docs) |
| **Docker Hub** | Interact with Docker Hub. | 🔑 ApiKey | ✅ | [Link](https://docs.docker.com/docker-hub/api/latest/) |
| **Firebase** | Google's mobile/web app development platform. | 🔑 ApiKey | ✅ | [Link](https://firebase.google.com/docs/reference/rest) |
| **Genderize.io** | Predict the gender of a person based on their name. | No | ✅ | [Link](https://genderize.io) |
| **Google Calendar** | Create, view, or update calendar events. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/calendar/api) |
| **GitHub** | Make use of GitHub data. | 🔐 OAuth | ✅ | [Link](https://docs.github.com/en/free-pro-team@latest/rest) |
| **Gitlab** | Automate GitLab. | 🔐 OAuth | ✅ | [Link](https://docs.gitlab.com/ee/api/) |
| **Google Docs** | Create and edit documents. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/docs/api/reference/rest) |
| **Google Sheets** | Read and write to Google Sheets. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/sheets/api/reference/rest) |
| **Heroku** | PaaS. | 🔐 OAuth | ✅ | [Link](https://devcenter.heroku.com/articles/platform-api-reference/) |
| **Host.io** | Domains Data. | 🔑 ApiKey | ✅ | [Link](https://host.io) |
| **Hunter** | Email Verifier. | 🔑 ApiKey | ✅ | [Link](https://hunter.io/api) |
| **IP2Location** | IP geolocation database (**Free tier**). | 🔑 ApiKey | ✅ | [Link](https://www.ip2location.com/web-service/ip2location) |
| **IPGeolocation** | IP geolocation and timezone API (**Free tier: 30k/month**). | 🔑 ApiKey | ✅ | [Link](https://ipgeolocation.io/) |
| **IPify** | A simple IP Address API. | No | ✅ | [Link](https://www.ipify.org/) |
| **IPinfo** | IP Address Information. | No | ✅ | [Link](https://ipinfo.io/developers) |
| **Ipstack** | Locate and identify website visitors by IP address. | 🔑 ApiKey | ✅ | [Link](https://ipstack.com/) |
| **JSONbin.io** | Free JSON storage. | 🔑 ApiKey | ✅ | [Link](https://jsonbin.io) |
| **LibreTranslate** | Free and open-source translation API (**Self-hosted, No Auth**). | No | ✅ | [Link](https://libretranslate.com/) |
| **Mailboxlayer** | Email verification and validation. | 🔑 ApiKey | ✅ | [Link](https://mailboxlayer.com/) |
| **Nationalize.io** | Predict the nationality of a person based on their name. | No | ✅ | [Link](https://nationalize.io) |
| **Netlify** | Netlify API. | 🔐 OAuth | ✅ | [Link](https://docs.netlify.com/api/get-started/) |
| **Notion** | Access to Notion workspace data via API. | 🔐 OAuth | ✅ | [Link](https://developers.notion.com/) |
| **Numverify** | Phone number validation. | 🔑 ApiKey | ✅ | [Link](https://numverify.com/) |
| **Pdflayer** | HTML to PDF conversion. | 🔑 ApiKey | ✅ | [Link](https://pdflayer.com/) |
| **PocketBase** | Open source backend (database, auth, files). | 🔑 ApiKey | ✅ | [Link](https://pocketbase.io/docs/api-records/) |
| **Positionstack** | Forward & Reverse Geocoding. | 🔑 ApiKey | ✅ | [Link](https://positionstack.com/) |
| **Railway** | Modern deployment platform API. | 🔑 ApiKey | ✅ | [Link](https://docs.railway.app/reference/public-api) |
| **Render** | Cloud platform API for apps and databases. | 🔑 ApiKey | ✅ | [Link](https://api-docs.render.com/reference/introduction) |
| **Screenshotlayer** | Website screenshots. | 🔑 ApiKey | ✅ | [Link](https://screenshotlayer.com/) |
| **Serpstack** | Real-Time Google Search Results. | 🔑 ApiKey | ✅ | [Link](https://serpstack.com/) |
| **Supabase** | Open source Firebase alternative (database, auth, storage). | 🔑 ApiKey | ✅ | [Link](https://supabase.com/docs/guides/api) |
| **Userstack** | User-Agent String Analysis. | 🔑 ApiKey | ✅ | [Link](https://userstack.com/) |
| **UUID Generator** | Generate UUIDs (v1, v3, v4, v5). | No | ✅ | [Link](https://www.uuidgenerator.net/api) |
| **Vercel** | Deployment platform API. | 🔑 ApiKey | ✅ | [Link](https://vercel.com/docs/rest-api/endpoints) |
| **Cloudinary** | Image and video management API. | 🔑 ApiKey | ✅ | [Link](https://cloudinary.com/documentation/image_upload_api_reference) |
| **QRServer** | Generate QR codes dynamically (**No Auth**). | No | ✅ | [Link](https://goqr.me/api/) |
| **Web Scraper** | Web scraping service (ScrapingBee). | 🔑 ApiKey | ✅ | [Link](https://www.scrapingbee.com/documentation/) |
| **EmailJS** | Send emails directly from JavaScript (**Free tier**). | 🔑 ApiKey | ✅ | [Link](https://www.emailjs.com/docs/) |
| **Abstract API** | Suite of useful APIs (IP geolocation, holidays, exchange rates). | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/) |
| **Rebrandly** | URL shortener API. | 🔑 ApiKey | ✅ | [Link](https://developers.rebrandly.com/docs) |
| **QuickChart** | Generate charts and QR codes. | No | ✅ | [Link](https://quickchart.io/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="dictionaries"></a>📖 Dictionaries

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Free Dictionary API** | Free English dictionary API. | No | ✅ | [Link](https://dictionaryapi.dev/) |
| **Merriam-Webster** | Dictionary and thesaurus. | 🔑 ApiKey | ✅ | [Link](https://dictionaryapi.com/) |
| **Oxford Dictionaries** | English dictionary and language data. | 🔑 ApiKey | ✅ | [Link](https://developer.oxforddictionaries.com/) |
| **Urban Dictionary** | Slang dictionary. | No | ✅ | [Link](https://github.com/zdict/zdict/wiki/Urban-dictionary-API-documentation) |
| **WordsAPI** | Word definitions, synonyms, antonyms. | 🔑 ApiKey | ✅ | [Link](https://www.wordsapi.com/) |
| **Lingua Robot** | Word definitions and language detection (**No Auth**). | No | ✅ | [Link](https://www.linguarobot.io/) |
| **Datamuse** | Word-finding query engine (**No Auth**). | No | ✅ | [Link](https://www.datamuse.com/api/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="education"></a>🎓 Education

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Universities List** | List of universities worldwide. | No | ✅ | [Link](http://universities.hipolabs.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="public-data"></a>📊 Public Data & Datasets

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Data.gov** | US Government open data. | No | ✅ | [Link](https://api.data.gov/) |
| **Socrata Open Data** | Access government and public sector data. | No | ✅ | [Link](https://dev.socrata.com/) |
| **USDA FoodData** | Nutritional data for food products. | 🔑 ApiKey | ✅ | [Link](https://fdc.nal.usda.gov/api-guide.html) |
| **World Bank** | Global development data. | No | ✅ | [Link](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) |
| **Nager.Date** | Public holidays for 100+ countries (**No Auth, no rate limit**). | No | ✅ | [Link](https://date.nager.at/Api) |
| **OpenHolidays API** | Public and school holidays worldwide (**No Auth**). | No | ✅ | [Link](https://www.openholidaysapi.org/) |
| **TimeZoneDB** | Time zone data and conversion (**No Auth**). | No | ✅ | [Link](https://timezonedb.com/api) |



[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="email-sms"></a>📧 Email & SMS

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Mailgun** | Email service for developers (free tier). | 🔑 ApiKey | ✅ | [Link](https://documentation.mailgun.com/) |
| **Resend** | Modern email API for developers (free tier). | 🔑 ApiKey | ✅ | [Link](https://resend.com/docs/api-reference/introduction) |
| **SendGrid** | Email delivery service (free tier: 100/day). | 🔑 ApiKey | ✅ | [Link](https://docs.sendgrid.com/api-reference) |
| **Twilio** | SMS, voice, and messaging (trial credits). | 🔑 ApiKey | ✅ | [Link](https://www.twilio.com/docs/usage/api) |
| **Vonage (Nexmo)** | SMS and voice APIs (trial credits). | 🔑 ApiKey | ✅ | [Link](https://developer.vonage.com/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="finance"></a>💰 Finance

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Alpaca** | Commission-free stock trading. | 🔑 ApiKey | ✅ | [Link](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/) |
| **Alpha Vantage** | Realtime and historical stock data. | 🔑 ApiKey | ✅ | [Link](https://www.alphavantage.co/) |
| **Binlist** | BIN/IIN Lookup. | No | ✅ | [Link](https://binlist.net/) |
| **CoinDesk** | Bitcoin Price Index (BPI) data (**No Auth**). | No | ✅ | [Link](https://www.coindesk.com/coindesk-api) |
| **Currencylayer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://currencylayer.com/) |
| **Exchangeratesapi** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://exchangeratesapi.io/) |
| **Financial Modeling Prep** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://site.financialmodelingprep.com/developer/docs) |
| **Finnhub** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://finnhub.io/docs/api) |
| **Fixer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://fixer.io/) |
| **FRED** | Economic data. | 🔑 ApiKey | ✅ | [Link](https://fred.stlouisfed.org/docs/api/fred/) |
| **Klarna** | Payments. | 🔑 ApiKey | ✅ | [Link](https://docs.klarna.com/api/) |
| **MercadoPago** | Payments. | 🔑 ApiKey | ✅ | [Link](https://www.mercadopago.com.br/developers/es/reference) |
| **Marketstack** | Real-time, intraday and historical market data. | 🔑 ApiKey | ✅ | [Link](https://marketstack.com/) |
| **Plaid** | Connect bank accounts. | 🔑 ApiKey | ✅ | [Link](https://www.plaid.com/docs) |
| **Polygon** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://polygon.io/) |
| **Stripe** | Payments. | 🔑 ApiKey | ✅ | [Link](https://stripe.com/docs/api) |
| **Tax Data API** | Tax rates and validation. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/tax_data-api) |
| **Exchangerate.host** | Foreign exchange & crypto rates. | 🔑 ApiKey | ✅ | [Link](https://exchangerate.host/) |
| **Frankfurter** | Open source exchange rates API. | No | ✅ | [Link](https://www.frankfurter.app/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="food-drink"></a>🍔 Food & Drink

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Open Food Facts** | Food product data. | No | ✅ | [Link](https://world.openfoodfacts.org/data) |
| **TheCocktailDB** | Open database for drinks and cocktails. | 🔑 ApiKey | ✅ | [Link](https://www.thecocktaildb.com/api.php) |
| **TheMealDB** | Open source database of recipes from around the world. | 🔑 ApiKey | ✅ | [Link](https://www.themealdb.com/api.php) |
| **Spoonacular** | Food, recipes, and nutrition data. | 🔑 ApiKey | ✅ | [Link](https://spoonacular.com/food-api) |
| **Edamam Recipe** | Recipe search and nutrition analysis. | 🔑 ApiKey | ✅ | [Link](https://developer.edamam.com/edamam-recipe-api) |
| **Coffee** | Random coffee images (**No Auth**). | No | ✅ | [Link](https://coffee.alexflipnote.dev/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="entertainment"></a>🎮 Entertainment

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **OMDb** | Open Movie Database. | 🔑 ApiKey | ✅ | [Link](http://www.omdbapi.com/) |
| **Quiz API** | Random trivia questions (**No Auth**). | No | ✅ | [Link](https://quizapi.io/) |
| **Quotable** | Random quotes (**No Auth**). | No | ✅ | [Link](https://github.com/lukePeavey/quotable) |
| **Activities when get bored** | Random suggestions for activities. | No | ✅ | [Link](https://rapidapi.com/bored/api/bored-api/) |
| **Simkl** | Movies, TV, Anime metadata. | 🔑 ApiKey | ✅ | [Link](https://simkl.com/apidoc/) |
| **TMDb** | The Movie Database. | 🔑 ApiKey | ✅ | [Link](https://developers.themoviedb.org/3) |
| **TVmaze** | TV shows and episode data (**No Auth**). | No | ✅ | [Link](https://www.tvmaze.com/api) |
| **Trakt** | TV and Movie tracking. | 🔐 OAuth | ✅ | [Link](https://trakt.docs.apiary.io/) |
| **Watchmode** | Streaming availability. | 🔑 ApiKey | ✅ | [Link](https://api.watchmode.com/) |
| **Cocktail** | Random cocktail recipes and ingredients. | No | ✅ | [Link](https://www.thecocktaildb.com/api.php) |
| **Trivia API** | Trivia questions in various categories (**No Auth**). | No | ✅ | [Link](https://the-trivia-api.com/) |
| **StreamElements** | Twitch/YouTube live streaming data & overlays. | 🔑 ApiKey | ✅ | [Link](https://dev.streamelements.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="geocoding"></a>🌍 Geocoding

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **IP-API** | IP to location. | No | No | [Link](https://ip-api.com/docs) |
| **Mapbox** | Maps and geocoding. | 🔑 ApiKey | ✅ | [Link](https://docs.mapbox.com/) |
| **Nominatim** | OpenStreetMap Geocoding. | No | ✅ | [Link](https://nominatim.org/release-docs/latest/api/Overview/) |
| **OpenStreetMap** | Map data. | 🔐 OAuth | ✅ | [Link](http://wiki.openstreetmap.org/wiki/API) |
| **Geocodio** | Geocoding and reverse geocoding for US/Canada. | 🔑 ApiKey | ✅ | [Link](https://www.geocod.io/docs/) |
| **LocationIQ** | Geocoding and maps (free tier: 5000 req/day). | 🔑 ApiKey | ✅ | [Link](https://locationiq.com/docs) |
| **Zippopotam.us** | Postal/zip code lookup for 60+ countries (**No Auth**). | No | ✅ | [Link](https://api.zippopotam.us/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="games-comics"></a>🎮 Games & Comics

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AmiiboAPI** | Nintendo Amiibo data. | No | ✅ | [Link](https://amiiboapi.com/) |
| **Battle.net** | Blizzard games data. | 🔐 OAuth | ✅ | [Link](https://develop.battle.net/documentation/guides/getting-started) |
| **BoardGameGeek** | Board games database. | No | ✅ | [Link](https://boardgamegeek.com/wiki/page/BGG_XML_API2) |
| **Brawl Stars** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.brawlstars.com) |
| **Chess.com** | Chess player stats and games. | No | ✅ | [Link](https://www.chess.com/news/view/published-data-api) |
| **Chuck Norris Database** | Jokes. | No | No | [Link](http://www.icndb.com/api/) |
| **Clash of Clans** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.clashofclans.com) |
| **Clash Royale** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.clashroyale.com) |
| **Deck of Cards** | Deck of cards. | No | No | [Link](http://deckofcardsapi.com/) |
| **Digimon** | Digimon information. | No | ✅ | [Link](https://digimon-api.vercel.app/) |
| **Dota 2** | Game data. | 🔑 ApiKey | ✅ | [Link](https://docs.opendota.com/) |
| **Dungeons and Dragons** | 5th Edition SRD. | No | ✅ | [Link](https://www.dnd5eapi.co/docs/) |
| **Eve Online** | Game data. | 🔐 OAuth | ✅ | [Link](https://esi.evetech.net/) |
| **Final Fantasy XIV** | Game data. | No | ✅ | [Link](https://xivapi.com/) |
| **Fortnite** | Game data. | 🔑 ApiKey | ✅ | [Link](https://fortnitetracker.com/site-api) |
| **Genshin Impact** | Game data. | No | ✅ | [Link](https://genshin.dev) |
| **Guild Wars 2** | Game data. | 🔑 ApiKey | ✅ | [Link](https://wiki.guildwars2.com/wiki/API:Main) |
| **Hyrule Compendium** | Legend of Zelda: BOTW data. | No | ✅ | [Link](https://github.com/gadhagod/Hyrule-Compendium-API) |
| **Hypixel** | Minecraft server data. | 🔑 ApiKey | ✅ | [Link](https://api.hypixel.net/) |
| **IGDB.com** | Game database. | 🔑 ApiKey | ✅ | [Link](https://api-docs.igdb.com) |
| **JokeAPI** | Programming and general jokes. | No | ✅ | [Link](https://sv443.net/jokeapi/v2/) |
| **Lichess** | Chess data. | 🔐 OAuth | ✅ | [Link](https://lichess.org/api) |
| **Magic: The Gathering** | MTG card data. | No | ✅ | [Link](https://docs.magicthegathering.io/) |
| **Marvel** | Comics data. | 🔑 ApiKey | ✅ | [Link](https://developer.marvel.com) |
| **Minecraft Server Status** | Server status. | No | ✅ | [Link](https://api.mcsrvstat.us) |
| **Open Trivia** | Trivia questions. | No | ✅ | [Link](https://opentdb.com/api_config.php) |
| **Pokéapi** | Pokémon data. | No | ✅ | [Link](https://pokeapi.co) |
| **PUBG** | Game data. | 🔑 ApiKey | ✅ | [Link](https://developer.pubg.com/) |
| **RAWG** | Video games database (500k+ games). | 🔑 ApiKey | ✅ | [Link](https://rawg.io/apidocs) |
| **Rick and Morty** | Show data. | No | ✅ | [Link](https://rickandmortyapi.com) |
| **Riot Games** | League of Legends data. | 🔑 ApiKey | ✅ | [Link](https://developer.riotgames.com/) |
| **Scryfall** | Magic: The Gathering card search. | No | ✅ | [Link](https://scryfall.com/docs/api) |
| **Valorant** | Valorant game data (unofficial). | No | ✅ | [Link](https://valorant-api.com/) |
| **PokéAPI v2** | Comprehensive Pokémon data (**No Auth, 300M+ requests/month**). | No | ✅ | [Link](https://pokeapi.co/docs/v2) |
| **MMO API** | MMORPG and RPG game items, achievements, characters. | 🔑 ApiKey | ✅ | [Link](https://raider.io/api) |
| **MLB** | Major League Baseball scores and statistics. | No | ✅ | [Link](https://appac.github.io/mlb-data-api-docs/) |
| **Yu-Gi-Oh!** | Yu-Gi-Oh! card data. | No | ✅ | [Link](https://ygoprodeck.com/api-guide/) |
| **GamerPower** | Free games, loot, and giveaways (**No Auth**). | No | ✅ | [Link](https://www.gamerpower.com/api-read) |
| **Monster Hunter World** | MHW items, monsters, weapons, armor data (**No Auth**). | No | ✅ | [Link](https://docs.mhw-db.com/) |
| **Free to Play Games** | Database of free-to-play games (**No Auth**). | No | ✅ | [Link](https://www.freetogame.com/api-doc) |
| **Elden Ring API** | Elden Ring game data (**No Auth**). | No | ✅ | [Link](https://docs.eldenring.fanapis.com/) |
| **Balldontlie** | NBA players, teams, games & stats (**No Auth**). | No | ✅ | [Link](https://www.balldontlie.io/) |
| **Overwatch API** | Overwatch 2 player stats and heroes (**No Auth**). | No | ✅ | [Link](https://overfast-api.tekrop.fr/) |
| **Tarkov API** | Escape from Tarkov items, quests, maps (**No Auth**). | No | ✅ | [Link](https://tarkov.dev/api/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="health"></a>❤️ Health

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BMI Calculator** | Calculate BMI and other metrics. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/navii/api/bmi-calculator/) |
| **Edamam Nutrition** | Nutrition analysis. | 🔑 ApiKey | ✅ | [Link](https://developer.edamam.com/edamam-nutrition-api) |
| **Nutritionix** | Nutrition database. | 🔑 ApiKey | ✅ | [Link](https://developer.nutritionix.com/) |
| **OpenFDA** | Public FDA data about drugs, devices, and foods. | No | ✅ | [Link](https://open.fda.gov/apis/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="machine-learning"></a>🧠 Machine Learning

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Anthropic Claude** | Access Claude AI models (offers free trial credits). | 🔑 ApiKey | ✅ | [Link](https://www.anthropic.com/api) |
| **Clarifai** | Computer Vision. | 🔐 OAuth | ✅ | [Link](https://docs.clarifai.com/api-guide/api-overview) |
| **Cloudmersive** | Image Recognition. | 🔑 ApiKey | ✅ | [Link](https://www.cloudmersive.com/image-recognition-and-processing-api) |
| **Cohere** | NLP and text generation models (free trial tier). | 🔑 ApiKey | ✅ | [Link](https://docs.cohere.com/) |
| **DeepAI** | Simple APIs for image generation and text processing. | 🔑 ApiKey | ✅ | [Link](https://deepai.org/api-docs) |
| **Deepgram** | Speech-to-text and audio intelligence. | 🔑 ApiKey | ✅ | [Link](https://deepgram.com/) |
| **Dialogflow** | Conversational AI. | 🔑 ApiKey | ✅ | [Link](https://cloud.google.com/dialogflow/docs/) |
| **Google Gemini** | Google's latest multimodal AI models. | 🔑 ApiKey | ✅ | [Link](https://ai.google.dev/) |
| **Groq** | Ultra-fast LLM inference API. | 🔑 ApiKey | ✅ | [Link](https://groq.com/) |
| **Hugging Face** | Access thousands of models for NLP, vision, and audio. | 🔑 ApiKey | ✅ | [Link](https://huggingface.co/docs/api-inference/index) |
| **Imagga** | Image Recognition. | 🔑 ApiKey | ✅ | [Link](https://imagga.com/) |
| **Languagelayer** | Language detection. | 🔑 ApiKey | ✅ | [Link](https://languagelayer.com/) |
| **Mistral AI** | High-performance open-source LLMs (free tier available). | 🔑 ApiKey | ✅ | [Link](https://docs.mistral.ai/) |
| **NLP Cloud** | NLP. | 🔑 ApiKey | ✅ | [Link](https://nlpcloud.io) |
| **Twinword Sentiment Analysis** | Sentiment analysis, emotion analysis, and more. | 🔑 ApiKey | ✅ | [Link](https://www.twinword.com/api/sentiment-analysis.php) |
| **Ollama** | Run open-source LLMs locally (self-hosted, no auth). | No | ✅ | [Link](https://github.com/ollama/ollama/blob/main/docs/api.md) |
| **OpenAI** | Access GPT models (offers free trial credits). | 🔑 ApiKey | ✅ | [Link](https://platform.openai.com/docs/api-reference) |
| **Perplexity AI** | AI-powered search and answers (limited free tier). | 🔑 ApiKey | ✅ | [Link](https://docs.perplexity.ai/) |
| **Replicate** | Run AI models via API (pay-as-you-go, free credits). | 🔑 ApiKey | ✅ | [Link](https://replicate.com/docs) |
| **Roboflow** | Computer Vision. | 🔑 ApiKey | ✅ | [Link](https://universe.roboflow.com) |
| **Stability AI** | Image generation (Stable Diffusion). | 🔑 ApiKey | ✅ | [Link](https://platform.stability.ai/docs/api-reference) |
| **Together AI** | Fast inference for open-source LLMs (free credits). | 🔑 ApiKey | ✅ | [Link](https://docs.together.ai/) |
| **WolframAlpha** | Computational Knowledge. | 🔑 ApiKey | ✅ | [Link](https://products.wolframalpha.com/api/) |
| **xAI Grok** | xAI's Grok model API (free tier available). | 🔑 ApiKey | ✅ | [Link](https://x.ai/api) |
| **AI21 Labs** | Powerful language models (free tier). | 🔑 ApiKey | ✅ | [Link](https://docs.ai21.com/) |
| **Fireworks AI** | Fast inference for open-source LLMs. | 🔑 ApiKey | ✅ | [Link](https://docs.fireworks.ai/) |
| **DeepSeek** | Powerful reasoning AI models with free API tier. | 🔑 ApiKey | ✅ | [Link](https://platform.deepseek.com/) |
| **Fal.ai** | Run AI models in serverless GPU (image/video generation). | 🔑 ApiKey | ✅ | [Link](https://fal.ai/docs) |
| **Suno AI** | AI music generation API. | 🔑 ApiKey | ✅ | [Link](https://suno.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="music"></a>🎵 Music

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Audiomack** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://www.audiomack.com/data-api/docs) |
| **Deezer** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://developers.deezer.com/api) |
| **Discogs** | Music database. | 🔐 OAuth | ✅ | [Link](https://www.discogs.com/developers/) |
| **Genius** | Lyrics and knowledge. | 🔐 OAuth | ✅ | [Link](https://docs.genius.com/) |
| **LastFm** | Music database. | 🔑 ApiKey | ✅ | [Link](https://www.last.fm/api) |
| **Mixcloud** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://www.mixcloud.com/developers/) |
| **MusicBrainz** | Music database. | No | ✅ | [Link](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) |
| **Musixmatch** | Lyrics. | 🔑 ApiKey | ✅ | [Link](https://developer.musixmatch.com/) |
| **SoundCloud** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://developers.soundcloud.com/docs/api/guide) |
| **Spotify** | Music streaming. | 🔐 OAuth | ✅ | [Link](https://beta.developer.spotify.com/documentation/web-api/) |
| **TheAudioDB** | Music metadata, charts, and more. | 🔑 ApiKey | ✅ | [Link](https://www.theaudiodb.com/api_guide.php) |
| **Shazam (RapidAPI)** | Music recognition and track details. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/apidojo/api/shazam) |
| **iTunes Search** | Search iTunes store for music, movies, apps (**No Auth**). | No | ✅ | [Link](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/) |
| **Radio Browser** | Community database of internet radio stations (**No Auth**). | No | ✅ | [Link](https://api.radio-browser.info/) |
| **Lyrics.ovh** | Simple lyrics search API (**No Auth**). | No | ✅ | [Link](https://lyricsovh.docs.apiary.io/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="mock-data-testing"></a>🧪 Mock Data & Testing

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **DummyJSON** | Fake REST API with products, users, todos, and more (**No Auth**). | No | ✅ | [Link](https://dummyjson.com/) |
| **Fake Store API** | Free fake e-commerce API for testing (products, carts, users). | No | ✅ | [Link](https://fakestoreapi.com/) |
| **JSONPlaceholder** | Free fake API for testing and prototyping (posts, comments, users). | No | ✅ | [Link](https://jsonplaceholder.typicode.com/) |
| **Mockaroo** | Generate custom realistic test data in JSON, CSV, SQL. | 🔑 ApiKey | ✅ | [Link](https://www.mockaroo.com/) |
| **RandomUser.me** | Generate random user data (like Lorem Ipsum, but for people). | No | ✅ | [Link](https://randomuser.me/) |
| **ReqRes** | A hosted REST-API ready to respond to your AJAX requests. | No | ✅ | [Link](https://reqres.in/) |
| **Httpbin** | HTTP request and response testing (**No Auth**). | No | ✅ | [Link](https://httpbin.org/) |
| **Beeceptor** | Mock REST APIs in seconds (**No Auth**). | No | ✅ | [Link](https://beeceptor.com/) |
| **SampleAPIs** | Playground for RESTful and GraphQL endpoints (**No Auth**). | No | ✅ | [Link](https://api.sampleapis.com/) |
| **MockAPI.io** | Create custom mock REST APIs with fake data. | 🔑 ApiKey | ✅ | [Link](https://mockapi.io/docs) |
| **Postman Echo** | Test REST clients with echo endpoint (**No Auth**). | No | ✅ | [Link](https://www.postman-echo.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="news"></a>📰 News

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Currents** | Latest news. | 🔑 ApiKey | ✅ | [Link](https://currentsapi.services/en) |
| **GNews** | Global news search. | 🔑 ApiKey | ✅ | [Link](https://gnews.io/) |
| **NewsAPI** | Headlines and articles. | 🔑 ApiKey | ✅ | [Link](https://newsapi.org/) |
| **NewsData.io** | News search and tracking. | 🔑 ApiKey | ✅ | [Link](https://newsdata.io/) |
| **TheNewsAPI** | Global news API. | 🔑 ApiKey | ✅ | [Link](https://www.thenewsapi.com/) |
| **NewsAPI.ai** | AI-powered news API. | 🔑 ApiKey | ✅ | [Link](https://newsapi.ai/) |
| **The Guardian** | Guardian articles. | 🔑 ApiKey | ✅ | [Link](https://open-platform.theguardian.com/) |
| **Hacker News** | Tech news from Y Combinator (**No Auth**). | No | ✅ | [Link](https://github.com/HackerNews/API) |
| **Dev.to** | Developer community articles (**No Auth**). | No | ✅ | [Link](https://developers.forem.com/api) |

## <a id="photography"></a>📷 Photography

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Art Institute of Chicago** | Museum artwork data (**No Auth**). | No | ✅ | [Link](https://api.artic.edu/docs/) |
| **Giphy** | GIFs. | 🔑 ApiKey | ✅ | [Link](https://developers.giphy.com/docs/) |
| **Lorem Picsum** | Placeholder images. | No | ✅ | [Link](https://picsum.photos/) |
| **Met Museum** | Metropolitan Museum of Art collection (**No Auth**). | No | ✅ | [Link](https://metmuseum.github.io/) |
| **Pexels** | Free stock photos. | 🔑 ApiKey | ✅ | [Link](https://www.pexels.com/api/) |
| **Picsum Photos** | The Lorem Ipsum for photos. | No | ✅ | [Link](https://picsum.photos/) |
| **Pixabay** | Free stock photos and videos. | 🔑 ApiKey | ✅ | [Link](https://pixabay.com/api/docs/) |
| **Flickr** | Photo sharing and management. | 🔑 ApiKey | ✅ | [Link](https://www.flickr.com/services/api/) |
| **NASA Image Library** | NASA's image and video library (**No Auth**). | No | ✅ | [Link](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf) |
| **Unsplash** | High-quality photos. | 🔐 OAuth | ✅ | [Link](https://unsplash.com/developers) |
| **Imgix** | Real-time image processing and optimization. | 🔑 ApiKey | ✅ | [Link](https://docs.imgix.com/) |
| **Remove.bg** | AI background removal from images. | 🔑 ApiKey | ✅ | [Link](https://www.remove.bg/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="science"></a>🔬 Science & Space

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **NASA API** | Access NASA data, including Astronomy Picture of the Day (APOD). | 🔑 ApiKey | ✅ | [Link](https://api.nasa.gov/) |
| **SpaceX** | SpaceX launch data. | No | ✅ | [Link](https://github.com/r-spacex/SpaceX-API) |
| **arXiv** | Scientific paper search and metadata (**No Auth**). | No | ✅ | [Link](https://arxiv.org/help/api) |
| **ISS Location** | Real-time International Space Station location (**No Auth**). | No | ✅ | [Link](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) |
| **Launch Library** | Rocket launch schedules and information. | No | ✅ | [Link](https://thespacedevs.com/llapi) |
| **USGS Earthquake** | Real-time earthquake data (**No Auth**). | No | ✅ | [Link](https://earthquake.usgs.gov/fdsnws/event/1/) |
| **Newton** | Symbolic and arithmetic math calculator API (**No Auth**). | No | ✅ | [Link](https://newton.vercel.app/) |
| **Wolfram Short Answers** | Computational knowledge answers. | 🔑 ApiKey | ✅ | [Link](https://products.wolframalpha.com/short-answers-api/documentation) |
| **Open Science Framework** | Open source research management platform. | 🔐 OAuth | ✅ | [Link](https://developer.osf.io/) |
| **People in Space** | Current number of people in space (**No Auth**). | No | ✅ | [Link](http://open-notify.org/Open-Notify-API/People-In-Space/) |
| **Solar System OpenData** | Solar system planets and moons data (**No Auth**). | No | ✅ | [Link](https://api.le-systeme-solaire.net/en/) |
| **Where the ISS at** | Real-time ISS position, velocity and visibility (**No Auth**). | No | ✅ | [Link](https://wheretheiss.at/w/developer) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="security-validation"></a>🔐 Security & Validation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **HaveIBeenPwned** | Check if email or password has been compromised in a data breach. | 🔑 ApiKey | ✅ | [Link](https://haveibeenpwned.com/API/v3) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="shopping"></a>🛍️ Shopping

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Best Buy** | Retail data. | 🔑 ApiKey | ✅ | [Link](https://bestbuyapis.github.io/api-documentation/#overview) |
| **eBay** | Auction and retail. | 🔐 OAuth | ✅ | [Link](https://developer.ebay.com/) |
| **Etsy** | E-commerce. | 🔐 OAuth | ✅ | [Link](https://www.etsy.com/developers/documentation/getting_started/api_basics) |
| **Mercadolibre** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://developers.mercadolibre.cl/es_ar/api-docs-es) |
| **Shopee** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://open.shopee.com/documents?version=1) |
| **WooCommerce** | E-commerce. | 🔑 ApiKey | ✅ | [Link](https://woocommerce.github.io/woocommerce-rest-api-docs/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="social"></a>💬 Social

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Bluesky** | Decentralized social network API (AT Protocol). | 🔑 ApiKey | ✅ | [Link](https://docs.bsky.app/) |
| **Discord** | Chat platform. | 🔐 OAuth | ✅ | [Link](https://discord.com/developers/docs/intro) |
| **Facebook** | Social network. | 🔐 OAuth | ✅ | [Link](https://developers.facebook.com/) |
| **Gravatar** | WordPress avatar service. | No | ✅ | [Link](https://gravatar.com/site/implement/images/) |
| **Instagram** | Photo sharing. | 🔐 OAuth | ✅ | [Link](https://www.instagram.com/developer/) |
| **LINE** | Messaging app. | 🔐 OAuth | ✅ | [Link](https://developers.line.biz/en/) |
| **LinkedIn** | Professional network. | 🔐 OAuth | ✅ | [Link](https://docs.microsoft.com/en-us/linkedin/?context=linkedin/context) |
| **Mastodon** | Decentralized microblogging platform. | 🔐 OAuth | ✅ | [Link](https://docs.joinmastodon.org/api/) |
| **Microsoft Teams** | Team collaboration platform. | 🔐 OAuth | ✅ | [Link](https://docs.microsoft.com/en-us/graph/teams-concept-overview) |
| **Pinterest** | Visual discovery. | 🔐 OAuth | ✅ | [Link](https://developers.pinterest.com/) |
| **Reddit** | Social news. | 🔐 OAuth | ✅ | [Link](https://www.reddit.com/dev/api) |
| **Slack** | Team communication. | 🔐 OAuth | ✅ | [Link](https://api.slack.com/) |
| **Snapchat** | Photo and video sharing. | 🔐 OAuth | ✅ | [Link](https://developers.snap.com/) |
| **Telegram** | Messaging app. | 🔑 ApiKey | ✅ | [Link](https://core.telegram.org/bots/api) |
| **Threads** | Meta's microblogging platform. | 🔐 OAuth | ✅ | [Link](https://developers.facebook.com/docs/threads) |
| **TikTok** | Video sharing. | 🔐 OAuth | ✅ | [Link](https://developers.tiktok.com/doc/login-kit-web) |
| **Tumblr** | Microblogging platform. | 🔐 OAuth | ✅ | [Link](https://www.tumblr.com/docs/en/api/v2) |
| **Twitch** | Live streaming. | 🔐 OAuth | ✅ | [Link](https://dev.twitch.tv/docs) |
| **Twitter** | Microblogging. | 🔐 OAuth | ✅ | [Link](https://developer.twitter.com/en/docs) |
| **Viber** | Messaging app. | 🔑 ApiKey | ✅ | [Link](https://developers.viber.com/) |
| **WhatsApp** | Messaging app. | 🔐 OAuth | ✅ | [Link](https://developers.facebook.com/docs/whatsapp) |
| **YouTube** | Video sharing platform. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/youtube/v3) |
| **Zalo** | Messaging and social platform. | 🔐 OAuth | ✅ | [Link](https://developers.zalo.me/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="sports"></a>⚽ Sports

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **TheSportsDB** | Open crowd-sourced sports data and artwork. | 🔑 ApiKey | ✅ | [Link](https://www.thesportsdb.com/api.php) |
| **API-Football** | Football (soccer) live scores, fixtures, stats. | 🔑 ApiKey | ✅ | [Link](https://www.api-football.com/documentation-v3) |
| **Football-Data.org** | Football data and statistics (**Free tier**). | 🔑 ApiKey | ✅ | [Link](https://www.football-data.org/documentation/quickstart) |
| **NBA API** | NBA stats and scores (**No Auth**). | No | ✅ | [Link](https://github.com/swar/nba_api) |
| **ESPN** | Sports scores and news. | No | ✅ | [Link](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b) |


[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="utilities-tools"></a>🔧 Utilities & Tools

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **DiceBear Avatars** | Generate random SVG avatars (**No Auth**). | No | ✅ | [Link](https://www.dicebear.com/) |
| **FakerAPI** | Generate fake data for testing (**No Auth, 1000 req/day**). | No | ✅ | [Link](https://fakerapi.it/en) |
| **goqr.me** | Create QR codes via URL parameters (**No Auth**). | No | ✅ | [Link](https://goqr.me/api/) |
| **Gravatar** | Global avatar service (use email MD5 hash). | No | ✅ | [Link](https://gravatar.com/site/implement/) |
| **ipify** | A simple public IP address API (**No Auth**). | No | ✅ | [Link](https://www.ipify.org/) |
| **Pravatar** | Placeholder avatar images (**No Auth**). | No | ✅ | [Link](https://pravatar.cc/) |
| **QR Code Generator** | Dynamic QR code generation API. | No | ✅ | [Link](https://goqr.me/api/) |
| **RoboHash** | Generate unique robot/monster avatars (**No Auth**). | No | ✅ | [Link](https://robohash.org/) |
| **Shields.io** | Quality metadata badges for open source projects (**No Auth**). | No | ✅ | [Link](https://shields.io/) |
| **UI Avatars** | Generate avatar placeholders from initials (**No Auth, 28M+ daily requests**). | No | ✅ | [Link](https://ui-avatars.com/) |
| **URLBox** | Website screenshot API. | 🔑 ApiKey | ✅ | [Link](https://www.urlbox.io/) |
| **TinyURL** | URL shortener API (**No Auth**). | No | ✅ | [Link](https://tinyurl.com/app/dev) |
| **DuckDuckGo Instant Answer** | Quick, concise answers for definitions, calculations, and conversions. | No | ✅ | [Link](https://duckduckgo.com/api) |
| **Country.is** | Get country from IP address (**No Auth**). | No | ✅ | [Link](https://country.is/) |
| **Text Art API** | Generate text-based art (**No Auth**). | No | ✅ | [Link](http://patorjk.com/software/taag/) |
| **JSONLint** | JSON validation API. | No | ✅ | [Link](https://jsonlint.com/) |
| **Carbon Screenshot** | Create beautiful images of code snippets. | No | ✅ | [Link](https://carbon.now.sh/) |
| **PDF.co** | PDF generation, conversion and manipulation. | 🔑 ApiKey | ✅ | [Link](https://apidocs.pdf.co/) |
| **Short.io** | URL shortener with analytics. | 🔑 ApiKey | ✅ | [Link](https://developers.short.io/) |
| **Cal.com** | Open source scheduling API (Calendly alternative). | 🔑 ApiKey | ✅ | [Link](https://cal.com/docs/api-reference) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="design-colors"></a>🎨 Design & Colors

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Colormind** | AI-powered color palette generator (**No Auth**). | No | ✅ | [Link](http://colormind.io/api-access/) |
| **Lorem Picsum** | Beautiful placeholder images (**No Auth**). | No | ✅ | [Link](https://picsum.photos/) |
| **Placeholder.com** | Simple placeholder image service (**No Auth**). | No | ✅ | [Link](https://placehold.co/) |
| **The Color API** | Color conversion, schemes, and naming (**No Auth**). | No | ✅ | [Link](https://www.thecolorapi.com/) |
| **Dribbble** | Design community and portfolio. | 🔐 OAuth | ✅ | [Link](https://developer.dribbble.com/) |
| **Behance** | Creative work showcase. | 🔑 ApiKey | ✅ | [Link](https://www.behance.net/dev) |
| **Icon Horse** | Favicon grabber API. | No | ✅ | [Link](https://icon.horse/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="geography-countries"></a>🌎 Geography & Countries

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **REST Countries** | Comprehensive country data (flags, capitals, currencies) (**No Auth**). | No | ✅ | [Link](https://restcountries.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="transportation"></a>🚆 Transportation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BART** | Bay Area Rapid Transit. | 🔑 ApiKey | ✅ | [Link](http://api.bart.gov) |
| **OpenSky Network** | Flight tracking. | No | ✅ | [Link](https://openskynetwork.github.io/opensky-api/) |
| **Transport for London** | Public transport data. | 🔑 ApiKey | ✅ | [Link](https://api.tfl.gov.uk) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="unofficial-community"></a>⚠️ Unofficial & Community APIs

> **⚠️ Important Disclaimer:**  
> These APIs are **not officially supported** by the original services. They are community-maintained, reverse-engineered, or use unofficial methods. Use at your own risk:  
> - 🚨 May break at any time without notice  
> - ⚖️ May violate Terms of Service of the original platform  
> - 🔒 No official support or guarantees  
> - 📉 Rate limits and availability may change  
>  
> **When to use:** Development, testing, or when official APIs are too restrictive/expensive. For production, consider official APIs when available.

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Invidious** | Privacy-focused YouTube front-end and API (no tracking, no ads). | No | ✅ | [Link](https://docs.invidious.io/api/) |
| **Piped** | Alternative YouTube API (privacy-respecting, no Google tracking). | No | ✅ | [Link](https://docs.piped.video/docs/api-documentation/) |
| **NewPipe Extractor** | YouTube, SoundCloud, PeerTube data extraction library. | No | ✅ | [Link](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/) |
| **Bibliogram** | Instagram front-end (read-only, no login required) ⚠️ **Many instances down**. | No | ✅ | [Link](https://bibliogram.art/) |
| **Libreddit** | Reddit alternative front-end (fast, private, lightweight). | No | ✅ | [Link](https://github.com/libreddit/libreddit) |
| **ProxiTok** | TikTok alternative front-end with API support. | No | ✅ | [Link](https://github.com/pablouser1/ProxiTok) |
| **Scribe** | Medium alternative front-end (no tracking, no paywall). | No | ✅ | [Link](https://sr.ht/~edwardloveall/Scribe/) |
| **Rimgo** | Imgur alternative front-end (privacy-respecting). | No | ✅ | [Link](https://codeberg.org/video-prize-ranch/rimgo) |
| **Searx/SearxNG** | Meta search engine with JSON API (aggregates results). | No | ✅ | [Link](https://docs.searxng.org/dev/search_api.html) |
| **yt-dlp API** | YouTube (and 1000+ sites) video/audio download API. | No | ✅ | [Link](https://github.com/yt-dlp/yt-dlp) |
| **Scraptube** | Simple YouTube scraper (no official API needed). | No | ✅ | [Link](https://github.com/dermasmid/scrapetube) |
| **Instaloader** | Instagram scraper (posts, stories, profiles). | No | ✅ | [Link](https://instaloader.github.io/) |
| **TikTok API (Unofficial)** | Various community TikTok scrapers on GitHub. | No | ✅ | [Link](https://github.com/topics/tiktok-api) |
| **Twitter API Alternatives** | Community alternatives like tweet-harvest, twint forks. | No | ✅ | [Link](https://github.com/topics/twitter-scraper) |

**🔍 How to find instances:** Many of these services have multiple public instances. Check their GitHub repos for updated instance lists.

**💡 Self-hosting recommended:** For reliability and privacy, consider self-hosting these services rather than relying on public instances.

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="memes-fun"></a>😂 Memes & Fun

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Advice Slip** | Generate random advice slips (**No Auth**, great for simple widgets). | No | ✅ | [Link](https://api.adviceslip.com/) |
| **Chuck Norris Jokes** | Random Chuck Norris jokes (**No Auth**). | No | ✅ | [Link](https://api.chucknorris.io/) |
| **Dad Jokes** | Random dad jokes (**No Auth**). | No | ✅ | [Link](https://icanhazdadjoke.com/api) |
| **Imgflip** | Get popular meme templates to create your own memes (**No Auth**). | No | ✅ | [Link](https://api.imgflip.com/) |
| **JokeAPI** | Jokes in various categories (**No Auth**). | No | ✅ | [Link](https://jokeapi.dev/) |
| **Useless Facts** | Random useless facts (**No Auth**). | No | ✅ | [Link](https://uselessfacts.jsph.pl/) |
| **Kanye.rest** | Random Kanye West quotes (**No Auth**). | No | ✅ | [Link](https://api.kanye.rest/) |
| **Breaking Bad Quotes** | Random Breaking Bad quotes (**No Auth**). | No | ✅ | [Link](https://breakingbadquotes.xyz/) |
| **Random Dog Facts** | Random dog facts API (**No Auth**). | No | ✅ | [Link](https://kinduff.github.io/dog-api/) |
| **Corporate BS Generator** | Generate corporate jargon (**No Auth**). | No | ✅ | [Link](https://corporatebs-generator.sameerkumar.website/) |
| **Zen Quotes** | Random inspirational quotes (**No Auth**). | No | ✅ | [Link](https://zenquotes.io/) |
| **Affirmations** | Get random positive affirmations (**No Auth**). | No | ✅ | [Link](https://www.affirmations.dev/) |
| **Evil Insult** | Generate evil insults (**No Auth**). | No | ✅ | [Link](https://evilinsult.com/api/) |
| **Tronald Dump** | Random Donald Trump quotes (**No Auth**). | No | ✅ | [Link](https://tronalddump.io/) |
| **Numbers API** | Fun facts about numbers (**No Auth**). | No | ✅ | [Link](http://numbersapi.com/) |
| **Quote Garden** | Collection of 5000+ quotes (**No Auth**). | No | ✅ | [Link](https://pprathameshmore.github.io/QuoteGarden/) |
| **Fun Translations** | Translate text to Yoda, Pirate, etc. | 🔑 ApiKey | ✅ | [Link](https://funtranslations.com/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="jobs-career"></a>💼 Jobs & Career

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Adzuna** | Job board aggregator with salary data. | 🔑 ApiKey | ✅ | [Link](https://developer.adzuna.com/overview) |
| **APIJobs** | Real-time job market data. | 🔑 ApiKey | ✅ | [Link](https://apijobs.dev/) |
| **JSearch** | Job search API (via RapidAPI). | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |
| **Remoteok** | API for remote jobs (often used for job board projects). | No | ✅ | [Link](https://remoteok.com/api) |
| **Reed** | UK job board API. | 🔑 ApiKey | ✅ | [Link](https://www.reed.co.uk/developers) |
| **The Muse** | Job search and company data. | 🔑 ApiKey | ✅ | [Link](https://www.themuse.com/developers/api/v2) |
| **USAJOBS** | US government job listings. | 🔑 ApiKey | ✅ | [Link](https://developer.usajobs.gov/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="weather"></a>🌤️ Weather

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **7Timer!** | Weather forecast. | No | No | [Link](http://www.7timer.info/doc.php?lang=en) |
| **AccuWeather** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://developer.accuweather.com/apis) |
| **Open-Meteo** | Open-source weather API (**No API key required**). | No | ✅ | [Link](https://open-meteo.com/) |
| **Meteoblue** | Weather forecasts and history. | 🔑 ApiKey | ✅ | [Link](https://content.meteoblue.com/en/business-solutions/weather-apis) |
| **Visual Crossing** | Global weather data and forecasts. | 🔑 ApiKey | ✅ | [Link](https://www.visualcrossing.com/weather-api) |
| **OpenWeatherMap** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://openweathermap.org/api) |
| **RainViewer** | Weather radar. | No | ✅ | [Link](https://www.rainviewer.com/api.html) |
| **WeatherAPI** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://www.weatherapi.com/) |
| **Weatherbit** | Weather forecast. | 🔑 ApiKey | ✅ | [Link](https://www.weatherbit.io/api) |
| **Weatherstack** | Real-time & historical world weather data. | 🔑 ApiKey | ✅ | [Link](https://weatherstack.com/) |
| **wttr.in** | Console-oriented weather (**No Auth, Terminal/Browser**). | No | ✅ | [Link](https://github.com/chubin/wttr.in) |
| **7Timer! Weather** | Astronomical and meteorological forecasts (**No Auth**). | No | ✅ | [Link](http://www.7timer.info/doc.php) |
| **Air Quality (OpenAQ)** | Global air quality data (**No Auth**). | No | ✅ | [Link](https://docs.openaq.org/) |
| **Sunrise-Sunset** | Sunrise and sunset times for any location (**No Auth**). | No | ✅ | [Link](https://sunrise-sunset.org/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ThanhNguyxn/awesome-free-apis&type=Date)](https://star-history.com/#ThanhNguyxn/awesome-free-apis&Date)

---

<div align="center">

**Don't forget to ⭐ this repo if you found it useful!**

</div>
