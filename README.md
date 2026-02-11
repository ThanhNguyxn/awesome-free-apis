# 🚀 Awesome Dev APIs

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

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
- [🔐 Authentication & Identity](#authentication-identity)
- [📚 Books & Literature](#books)
- [⛓️ Blockchain & Web3](#blockchain-web3)
- [🪙 Cryptocurrency](#cryptocurrency)
- [☁️ Cloud Storage & Files](#cloud-storage-files)
- [💻 Development](#development)
- [⚙️ Continuous Integration](#continuous-integration)
- [📝 Text Analysis & NLP](#text-analysis-nlp)
- [🏠 IoT & Smart Devices](#iot-smart-devices)
- [🔓 Open Source Projects](#open-source-projects)
- [📖 Dictionaries](#dictionaries)
- [🎓 Education](#education)
- [📅 Calendar & Holidays](#calendar-holidays)
- [📊 Public Data & Datasets](#public-data)
- [📧 Email & SMS](#email-sms)
- [📱 Phone & Telephony](#phone-telephony)
- [🎮 Entertainment](#entertainment)
- [🎪 Events](#events)
- [🎙️ Podcasts](#podcasts)
- [💭 Personality & Quotes](#personality-quotes)
- [💰 Finance](#finance)
- [💱 Currency Exchange](#currency-exchange)
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
- [✅ Data Validation](#data-validation)
- [🛍️ Shopping](#shopping)
- [🔧 Utilities & Tools](#utilities-tools)
- [🔗 URL Shorteners](#url-shorteners)
- [💬 Social](#social)
- [⚽ Sports](#sports)
- [🎨 Design & Colors](#design-colors)
- [🌎 Geography & Countries](#geography-countries)
- [🚆 Transportation](#transportation)
- [📦 Tracking & Logistics](#tracking-logistics)
- [🌿 Environment & Climate](#environment-climate)
- [🏛️ Government & Civic](#government-civic)
- [📹 Video](#video)
- [🔢 Math & Computation](#math-computation)
- [⚠️ Unofficial & Community APIs](#unofficial-community)
- [😂 Memes & Fun](#memes-fun)
- [💼 Jobs & Career](#jobs-career)
- [🌤️ Weather](#weather)
- [💼 Business](#business)
- [📄 Documents & Productivity](#documents-productivity)

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
| **Dog API v2** | Dog breeds and image endpoints for apps and bots. | No | ✅ | [Link](https://dogapi.dog/docs/api-v2) |
| **Shibe.Online** | Random pictures of Shiba Inu, cats or birds. | No | ✅ | [Link](http://shibe.online/) |
| **The Cat API** | Images of cats (great for testing image grids). | 🔑 ApiKey | ✅ | [Link](https://thecatapi.com/) |
| **The Dog API** | Images and data about dogs. | 🔑 ApiKey | ✅ | [Link](https://thedogapi.com/) |
| **TheCatDB** | Cat breeds and facts database. | 🔑 ApiKey | ✅ | [Link](https://www.thecatapi.com/) |
| **WoRMS** | Marine species taxonomy and classification data. | No | ✅ | [Link](https://www.marinespecies.org/rest/) |
| **Dog CEO** | Dog breeds and random dog images. | No | ✅ | [Link](https://dog.ceo/dog-api/) |
| **xeno-canto** | Bird sounds from around the world. | No | ✅ | [Link](https://xeno-canto.org/explore/api) |
| **PlaceDog** | Placeholder Dog pictures. | No | ✅ | [Link](https://place.dog) |
| **PlaceKitten** | Placeholder Kitten pictures. | No | ✅ | [Link](https://placekitten.com/) |

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
| **Catboy** | Neko images, funny GIFs & more. | No | ✅ | [Link](https://catboys.com/api) |

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
| **Phisherman** | IP/domain/URL reputation. | 🔑 ApiKey | ✅ | [Link](https://phisherman.gg/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="authentication-identity"></a>🔐 Authentication & Identity

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Descope** | Customer identity and authentication flows. | 🔑 ApiKey | ✅ | [Link](https://docs.descope.com/api/) |
| **Frontegg** | Authentication, user management, and multi-tenant identity. | 🔑 ApiKey | ✅ | [Link](https://developers.frontegg.com/) |
| **FusionAuth** | Identity and access management platform. | 🔑 ApiKey | ✅ | [Link](https://fusionauth.io/docs/apis/) |
| **GetOTP** | OTP verification and passwordless login APIs. | 🔑 ApiKey | ✅ | [Link](https://otp.dev/en/docs/) |
| **Keycloak** | Open-source identity and access management APIs. | No | ✅ | [Link](https://www.keycloak.org/docs-api/latest/rest-api/index.html) |
| **Kinde** | Authentication platform for modern apps. | 🔐 OAuth | ✅ | [Link](https://kinde.com/docs/developer-tools/) |
| **Logto** | Open-source auth infrastructure and identity APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.logto.io/) |
| **Magic** | Passwordless authentication and wallet login. | 🔑 ApiKey | ✅ | [Link](https://magic.link/docs/api) |
| **MojoAuth** | Passwordless authentication API and OTP flows. | 🔑 ApiKey | ✅ | [Link](https://mojoauth.com/docs/api) |
| **Ory** | Identity, session, and authorization APIs. | No | ✅ | [Link](https://www.ory.sh/docs/reference/api) |
| **Permit.io** | Authorization and policy management APIs for RBAC/ABAC. | 🔑 ApiKey | ✅ | [Link](https://docs.permit.io/) |
| **Stytch** | Authentication APIs for passwords, OTP, magic links, and OAuth. | 🔑 ApiKey | ✅ | [Link](https://stytch.com/docs/api) |
| **SuperTokens** | Open-source auth solution for session and user management. | No | ✅ | [Link](https://supertokens.com/docs) |
| **Warrant** | Fine-grained authorization and RBAC APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.warrant.dev/) |
| **WorkOS** | Enterprise SSO, SCIM, and user management APIs. | 🔑 ApiKey | ✅ | [Link](https://workos.com/docs/reference) |
| **Micro User Service** | User management and authentication. | 🔑 ApiKey | ✅ | [Link](https://m3o.com/user) |
| **SAWO Labs** | Simplify login and improve user experience by integrating passwordless authen... | 🔑 ApiKey | ✅ | [Link](https://sawolabs.com) |

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
| **The Bible API** | Bible metadata and translations for apps. | 🔑 ApiKey | ✅ | [Link](https://docs.api.bible) |
| **Poetry DB** | Database with over 40,000 poems (**No Auth**). | No | ✅ | [Link](https://poetrydb.org/) |
| **Quran Cloud** | Quran text, translations, and recitations. | No | ✅ | [Link](https://alquran.cloud/api) |
| **Bible API** | Free Bible text in multiple versions (**No Auth**). | No | ✅ | [Link](https://bible-api.com/) |
| **A Bíblia Digital** | Do not worry about managing the multiple versions of the Bible. | 🔑 ApiKey | ✅ | [Link](https://www.abibliadigital.com.br/en) |
| **Bhagavad Gita** | Open Source Shrimad Bhagavad Gita API including 21+ authors translation in Sa... | 🔑 ApiKey | ✅ | [Link](https://docs.bhagavadgitaapi.in) |
| **Bhagavad Gita telugu** | Bhagavad Gita API in telugu and odia languages. | No | ✅ | [Link](https://gita-api.vercel.app) |
| **British National Bibliography** | Books. | No | No | [Link](http://bnb.data.bl.uk/) |
| **Crossref Metadata Search** | Books & Articles Metadata. | No | ✅ | [Link](https://github.com/CrossRef/rest-api-doc) |
| **Ganjoor** | Classic Persian poetry works including access to related manuscripts, recitat... | 🔐 OAuth | ✅ | [Link](https://api.ganjoor.net) |
| **PoetryDB** | Enables you to get instant data from our vast poetry collection. | No | ✅ | [Link](https://github.com/thundercomb/poetrydb#readme) |
| **Quran** | RESTful Quran API with multiple languages. | No | ✅ | [Link](https://quran.api-docs.io/) |
| **Quran-api** | Free Quran API Service with 90+ different languages and 400+ translations. | No | ✅ | [Link](https://github.com/fawazahmed0/quran-api#readme) |
| **Thirukkural** | 1330 Thirukkural poems and explanation in Tamil and English. | No | ✅ | [Link](https://api-thirukkural.web.app/) |
| **Wolne Lektury** | API for obtaining information about e-books available on the WolneLektury.pl ... | No | ✅ | [Link](https://wolnelektury.pl/api/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="blockchain-web3"></a>⛓️ Blockchain & Web3

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Ankr RPC** | Multi-chain RPC infrastructure for Web3 apps. | 🔑 ApiKey | ✅ | [Link](https://www.ankr.com/rpc/) |
| **BlockCypher** | Blockchain data APIs for Bitcoin, Litecoin, Dogecoin, and Dash. | 🔑 ApiKey | ✅ | [Link](https://www.blockcypher.com/dev/bitcoin/) |
| **BscScan** | BNB Chain explorer and contract data APIs. | 🔑 ApiKey | ✅ | [Link](https://bscscan.com/apis) |
| **Chainbase** | Unified blockchain data API across multiple chains. | 🔑 ApiKey | ✅ | [Link](https://docs.chainbase.com/) |
| **Covalent** | Unified API for blockchain transaction and token data. | 🔑 ApiKey | ✅ | [Link](https://www.covalenthq.com/docs/api/) |
| **Chainlink** | Developer resources for decentralized oracle data. | No | ✅ | [Link](https://chain.link/developer-resources) |
| **dRPC** | Distributed RPC provider for EVM and non-EVM chains. | 🔑 ApiKey | ✅ | [Link](https://drpc.org/docs) |
| **Etherscan** | Ethereum explorer and smart contract data APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.etherscan.io/) |
| **FreeRPC** | Free public RPC endpoints for many blockchains. | No | ✅ | [Link](https://www.freerpc.com/) |
| **GetBlock** | Blockchain node infrastructure via unified API. | 🔑 ApiKey | ✅ | [Link](https://getblock.io/) |
| **Helius** | Solana infrastructure APIs for transactions, NFTs, and webhooks. | 🔑 ApiKey | ✅ | [Link](https://docs.helius.dev/) |
| **Infura** | Scalable Ethereum, IPFS, and Web3 APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.infura.io/) |
| **Nownodes** | Multi-chain RPC and blockchain access APIs. | 🔑 ApiKey | ✅ | [Link](https://nownodes.io/) |
| **QuickNode** | Multi-chain RPC infrastructure and blockchain APIs. | 🔑 ApiKey | ✅ | [Link](https://www.quicknode.com/docs) |
| **Solscan** | Solana data APIs for addresses, tokens, and transactions. | 🔑 ApiKey | ✅ | [Link](https://pro-api.solscan.io/pro-api-docs/v2.0) |
| **Tatum** | Blockchain infrastructure and wallet APIs for many chains. | 🔑 ApiKey | ✅ | [Link](https://apidoc.tatum.io/) |
| **The Graph** | GraphQL indexing protocol for querying blockchain data. | 🔑 ApiKey | ✅ | [Link](https://thegraph.com/docs/en/subgraphs/querying/introduction/) |
| **thirdweb** | Developer tooling APIs for smart contracts and wallets. | 🔑 ApiKey | ✅ | [Link](https://portal.thirdweb.com/typescript/v5) |
| **Watchdata** | Multi-chain wallet, NFT, and node APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.watchdata.io/) |
| **Bitquery** | Onchain GraphQL APIs & DEX APIs. | 🔑 ApiKey | ✅ | [Link](https://graphql.bitquery.io/ide) |
| **Chainpoint** | Chainpoint is a global network for anchoring data to the Bitcoin blockchain. | No | ✅ | [Link](https://tierion.com/chainpoint/) |
| **Helium** | Helium is a global, distributed network of Hotspots that create public, long-... | No | ✅ | [Link](https://docs.helium.com/api/blockchain/introduction/) |
| **Steem** | Blockchain-based blogging and social media website. | No | No | [Link](https://developers.steem.io/) |
| **Walltime** | To retrieve Walltime's market info. | No | ✅ | [Link](https://walltime.info/api.html) |

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
| **Mobula** | On-chain crypto data and wallet analytics. | 🔑 ApiKey | ✅ | [Link](https://docs.mobula.io/) |
| **Moralis** | Web3 wallet, NFT, and DeFi data. | 🔑 ApiKey | ✅ | [Link](https://docs.moralis.io/) |
| **Bitcambio** | Get the list of all traded assets in the exchange. | No | ✅ | [Link](https://nova.bitcambio.com.br/api/v3/docs#a-public) |
| **BitcoinAverage** | Digital Asset Price Data for the blockchain industry. | 🔑 ApiKey | ✅ | [Link](https://apiv2.bitcoinaverage.com/) |
| **BitcoinCharts** | Financial and Technical Data related to the Bitcoin Network. | No | ✅ | [Link](https://bitcoincharts.com/about/exchanges/) |
| **blockfrost Cardano** | Interaction with the Cardano mainnet and several testnets. | 🔑 ApiKey | ✅ | [Link](https://blockfrost.io/) |
| **Brave NewCoin** | Real-time and historic crypto data from more than 200+ exchanges. | 🔑 ApiKey | ✅ | [Link](https://bravenewcoin.com/developers) |
| **BtcTurk** | Real-time cryptocurrency data, graphs and API that allows buy&sell. | 🔑 ApiKey | ✅ | [Link](https://docs.btcturk.com/) |
| **Coinbase Pro** | Cryptocurrency Trading Platform. | 🔑 ApiKey | ✅ | [Link](https://docs.pro.coinbase.com/#api) |
| **CoinDCX** | Cryptocurrency Trading Platform. | 🔑 ApiKey | ✅ | [Link](https://docs.coindcx.com/) |
| **Coinigy** | Interacting with Coinigy Accounts and Exchange Directly. | 🔑 ApiKey | ✅ | [Link](https://coinigy.docs.apiary.io) |
| **CoinRanking** | Live Cryptocurrency data. | 🔑 ApiKey | ✅ | [Link](https://developers.coinranking.com/api/documentation) |
| **Coinremitter** | Cryptocurrencies Payment & Prices. | 🔑 ApiKey | ✅ | [Link](https://coinremitter.com/docs) |
| **CoinStats** | Crypto Tracker. | No | ✅ | [Link](https://documenter.getpostman.com/view/5734027/RzZ6Hzr3?version=latest) |
| **CryptAPI** | Cryptocurrency Payment Processor. | No | ✅ | [Link](https://docs.cryptapi.io/) |
| **CryptingUp** | Cryptocurrency data. | No | ✅ | [Link](https://www.cryptingup.com/apidoc/#introduction) |
| **CryptoMarket** | Cryptocurrencies Trading platform. | 🔑 ApiKey | ✅ | [Link](https://api.exchange.cryptomkt.com/) |
| **Cryptonator** | Cryptocurrencies Exchange Rates. | No | ✅ | [Link](https://www.cryptonator.com/api/) |
| **dYdX** | Decentralized cryptocurrency exchange. | 🔑 ApiKey | ✅ | [Link](https://docs.dydx.exchange/) |
| **Ethplorer** | Ethereum tokens, balances, addresses, history of transactions, contracts, and... | 🔑 ApiKey | ✅ | [Link](https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API) |
| **EXMO** | Cryptocurrencies exchange based in UK. | 🔑 ApiKey | ✅ | [Link](https://documenter.getpostman.com/view/10287440/SzYXWKPi) |
| **Hirak Exchange Rates** | Exchange rates between 162 currency & 300 crypto currency update each 5 min, ... | 🔑 ApiKey | ✅ | [Link](https://rates.hirak.site/) |
| **Huobi** | Seychelles based cryptocurrency exchange. | 🔑 ApiKey | ✅ | [Link](https://huobiapi.github.io/docs/spot/v1/en/) |
| **icy.tools** | GraphQL based NFT API. | 🔑 ApiKey | ✅ | [Link](https://developers.icy.tools/) |
| **Indodax** | Trade your Bitcoin and other assets with rupiah. | 🔑 ApiKey | ✅ | [Link](https://github.com/btcid/indodax-official-api-docs) |
| **INFURA Ethereum** | Interaction with the Ethereum mainnet and several testnets. | 🔑 ApiKey | ✅ | [Link](https://infura.io/product/ethereum) |
| **MercadoBitcoin** | Brazilian Cryptocurrency Information. | No | ✅ | [Link](https://www.mercadobitcoin.com.br/api-doc/) |
| **Nexchange** | Automated cryptocurrency exchange service. | No | No | [Link](https://nexchange2.docs.apiary.io/) |
| **NovaDax** | NovaDAX API to access all market data, trading management endpoints. | 🔑 ApiKey | ✅ | [Link](https://doc.novadax.com/en-US/#introduction) |
| **OKEx** | Cryptocurrency exchange based in Seychelles. | 🔑 ApiKey | ✅ | [Link](https://www.okex.com/docs/) |
| **Solana JSON RPC** | Provides various endpoints to interact with the Solana Blockchain. | No | ✅ | [Link](https://docs.solana.com/developing/clients/jsonrpc-api) |
| **Technical Analysis** | Cryptocurrency prices and technical analysis. | 🔑 ApiKey | ✅ | [Link](https://technical-analysis-api.com) |
| **VALR** | Cryptocurrency Exchange based in South Africa. | 🔑 ApiKey | ✅ | [Link](https://docs.valr.com/) |
| **WorldCoinIndex** | Cryptocurrencies Prices. | 🔑 ApiKey | ✅ | [Link](https://www.worldcoinindex.com/apiservice) |
| **ZMOK** | Ethereum JSON RPC API and Web3 provider. | No | ✅ | [Link](https://zmok.io) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="cloud-storage-files"></a>☁️ Cloud Storage & Files

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Backblaze B2** | Cloud object storage API with S3-compatible endpoints. | 🔑 ApiKey | ✅ | [Link](https://www.backblaze.com/apidocs/introduction-to-the-s3-compatible-api) |
| **Box** | Cloud content management and file storage API. | 🔐 OAuth | ✅ | [Link](https://developer.box.com/reference/) |
| **Cloudflare R2** | S3-compatible object storage API without egress fees. | 🔑 ApiKey | ✅ | [Link](https://developers.cloudflare.com/r2/api/s3/api/) |
| **Dropbox** | File storage and sharing APIs. | 🔐 OAuth | ✅ | [Link](https://www.dropbox.com/developers/documentation/http/documentation) |
| **Filebase** | S3-compatible object storage backed by decentralized networks. | 🔑 ApiKey | ✅ | [Link](https://docs.filebase.com/api-documentation) |
| **Filestack** | File uploads, processing, and content delivery APIs. | 🔑 ApiKey | ✅ | [Link](https://www.filestack.com/docs/api/) |
| **GoFile** | File hosting and management APIs. | 🔑 ApiKey | ✅ | [Link](https://gofile.io/api) |
| **Google Drive** | File storage, sharing, and metadata APIs. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/drive/api) |
| **Gyazo** | Image upload and screenshot APIs. | 🔑 ApiKey | ✅ | [Link](https://gyazo.com/api/docs) |
| **ImgBB** | Simple image upload API with free tier. | 🔑 ApiKey | ✅ | [Link](https://api.imgbb.com/) |
| **ImageKit** | Image and media upload, optimization, and delivery APIs. | 🔑 ApiKey | ✅ | [Link](https://imagekit.io/docs/api-reference/) |
| **OneDrive (Microsoft Graph)** | OneDrive file and folder APIs via Microsoft Graph. | 🔐 OAuth | ✅ | [Link](https://learn.microsoft.com/en-us/graph/api/resources/onedrive) |
| **Pinata** | IPFS pinning and decentralized file storage APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.pinata.cloud/) |
| **Storj** | Decentralized cloud object storage APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.storj.io/) |
| **Uploadcare** | File uploads, media processing, and delivery APIs. | 🔑 ApiKey | ✅ | [Link](https://uploadcare.com/docs/api_reference/) |
| **UploadThing** | File upload infrastructure for modern web apps. | 🔑 ApiKey | ✅ | [Link](https://docs.uploadthing.com/) |
| **Web3.Storage** | Decentralized storage API built on IPFS/Filecoin. | 🔑 ApiKey | ✅ | [Link](https://web3.storage/docs/) |
| **AnonFiles** | Upload and share your files anonymously. | No | ✅ | [Link](https://anonfiles.com/docs/api) |
| **BayFiles** | Upload and share your files. | No | ✅ | [Link](https://bayfiles.com/docs/api) |
| **ddownload** | File Sharing and Storage. | 🔑 ApiKey | ✅ | [Link](https://ddownload.com/api) |
| **File.io** | Super simple file sharing, convenient, anonymous and secure. | No | ✅ | [Link](https://www.file.io) |
| **OneDrive** | File Sharing and Storage. | 🔐 OAuth | ✅ | [Link](https://developer.microsoft.com/onedrive) |
| **Pantry** | Free JSON storage for small projects. | No | ✅ | [Link](https://getpantry.cloud/) |
| **Pastebin** | Plain Text Storage. | 🔑 ApiKey | ✅ | [Link](https://pastebin.com/doc_api) |
| **Quip** | File Sharing and Storage for groups. | 🔑 ApiKey | ✅ | [Link](https://quip.com/dev/automation/documentation) |
| **The Null Pointer** | No-bullshit file hosting and URL shortening service. | No | ✅ | [Link](https://0x0.st) |
| **Web3 Storage** | File Sharing and Storage for Free with 1TB Space. | 🔑 ApiKey | ✅ | [Link](https://web3.storage/) |

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
| **Apache Superset** | Dashboarding and query platform APIs. | 🔑 ApiKey | ✅ | [Link](https://superset.apache.org/docs/api/) |
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
| **Databricks** | Lakehouse workspace, jobs, and cluster APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.databricks.com/api/workspace/introduction) |
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
| **IPinfo** | IP Address Information. | No | ✅ | [Link](https://ipinfo.io/developers) |
| **Ipstack** | Locate and identify website visitors by IP address. | 🔑 ApiKey | ✅ | [Link](https://ipstack.com/) |
| **Instatus** | Status page and incident management API. | 🔑 ApiKey | ✅ | [Link](https://instatus.com/help/api) |
| **JSONbin.io** | Free JSON storage. | 🔑 ApiKey | ✅ | [Link](https://jsonbin.io) |
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
| **Redash** | Query, dashboards, and data source automation API. | 🔑 ApiKey | ✅ | [Link](https://redash.io/help/user-guide/integrations-and-api/api) |
| **Screenshotlayer** | Website screenshots. | 🔑 ApiKey | ✅ | [Link](https://screenshotlayer.com/) |
| **Serpstack** | Real-Time Google Search Results. | 🔑 ApiKey | ✅ | [Link](https://serpstack.com/) |
| **SnapAPI** | Screenshot, PDF, and markdown conversion API. | 🔑 ApiKey | ✅ | [Link](https://github.com/opspawn/screenshot-api) |
| **Supabase** | Open source Firebase alternative (database, auth, storage). | 🔑 ApiKey | ✅ | [Link](https://supabase.com/docs/guides/api) |
| **Userstack** | User-Agent String Analysis. | 🔑 ApiKey | ✅ | [Link](https://userstack.com/) |
| **UUID Generator** | Generate UUIDs (v1, v3, v4, v5). | No | ✅ | [Link](https://www.uuidgenerator.net/api) |
| **Vercel** | Deployment platform API. | 🔑 ApiKey | ✅ | [Link](https://vercel.com/docs/rest-api/endpoints) |
| **Cloudinary** | Image and video management API. | 🔑 ApiKey | ✅ | [Link](https://cloudinary.com/documentation/image_upload_api_reference) |
| **Web Scraper** | Web scraping service (ScrapingBee). | 🔑 ApiKey | ✅ | [Link](https://www.scrapingbee.com/documentation/) |
| **EmailJS** | Send emails directly from JavaScript (**Free tier**). | 🔑 ApiKey | ✅ | [Link](https://www.emailjs.com/docs/) |
| **Abstract API** | Suite of useful APIs (IP geolocation, holidays, exchange rates). | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/) |
| **QuickChart** | Generate charts and QR codes. | No | ✅ | [Link](https://quickchart.io/) |
| **Smartsheet** | Spreadsheet-style project management API. | 🔐 OAuth | ✅ | [Link](https://smartsheet.redoc.ly/) |
| **Neon** | Serverless Postgres database (free tier). | 🔑 ApiKey | ✅ | [Link](https://neon.tech/docs/reference/api-reference) |
| **Trello** | Project boards and workflow automation APIs. | 🔐 OAuth | ✅ | [Link](https://developers.trello.com/) |
| **Upstash** | Serverless Redis and Kafka (free tier). | 🔑 ApiKey | ✅ | [Link](https://upstash.com/docs/redis/overall/getstarted) |
| **Novu** | Open-source notification infrastructure. | 🔑 ApiKey | ✅ | [Link](https://docs.novu.co/api-reference/overview) |
| **PostHog** | Open-source product analytics (free tier). | 🔑 ApiKey | ✅ | [Link](https://posthog.com/docs/api) |
| **API Grátis** | Multiples services and public APIs. | No | ✅ | [Link](https://apigratis.com.br/) |
| **ApicAgent** | Extract device details from user-agent string. | No | ✅ | [Link](https://www.apicagent.com) |
| **Base** | Building quick backends. | 🔑 ApiKey | ✅ | [Link](https://www.base-api.io/) |
| **Blague.xyz** | La plus grande API de Blagues FR/The biggest FR jokes API. | 🔑 ApiKey | ✅ | [Link](https://blague.xyz/) |
| **Blitapp** | Schedule screenshots of web pages and sync them to your cloud. | 🔑 ApiKey | ✅ | [Link](https://blitapp.com/api/) |
| **Bored** | Find random activities to fight boredom. | No | ✅ | [Link](https://www.boredapi.com/) |
| **Brainshop.ai** | Make A Free A.I Brain. | 🔑 ApiKey | ✅ | [Link](https://brainshop.ai/) |
| **Browshot** | Easily make screenshots of web pages in any screen size, as any device. | 🔑 ApiKey | ✅ | [Link](https://browshot.com/api/documentation) |
| **Changelogs.md** | Structured changelog metadata from open source projects. | No | ✅ | [Link](https://changelogs.md) |
| **Ciprand** | Secure random string generator. | No | ✅ | [Link](https://github.com/polarspetroll/ciprand) |
| **Contentful Images** | Used to retrieve and apply transformations to images. | 🔑 ApiKey | ✅ | [Link](https://www.contentful.com/developers/docs/references/images-api/) |
| **CORS Proxy** | Get around the dreaded CORS error by using this proxy as a middle man. | No | ✅ | [Link](https://github.com/burhanuday/cors-proxy) |
| **DigitalOcean Status** | Status of all DigitalOcean services. | No | ✅ | [Link](https://status.digitalocean.com/api) |
| **DomainDb Info** | Domain name search to find all domains containing particular words/phrases/etc. | No | ✅ | [Link](https://api.domainsdb.info/) |
| **ExtendsClass JSON Storage** | A simple JSON store API. | No | ✅ | [Link](https://extendsclass.com/json-storage.html) |
| **GeekFlare** | Provide numerous capabilities for important testing and monitoring methods fo... | 🔑 ApiKey | ✅ | [Link](https://apidocs.geekflare.com/docs/geekflare-api) |
| **GETPing** | Trigger an email notification with a simple GET request. | 🔑 ApiKey | ✅ | [Link](https://www.getping.info) |
| **Ghost** | Get Published content into your Website, App or other embedded media. | 🔑 ApiKey | ✅ | [Link](https://ghost.org/) |
| **Gitter** | Chat for Developers. | 🔐 OAuth | ✅ | [Link](https://developer.gitter.im/docs/welcome) |
| **Glitterly** | Image generation API. | 🔑 ApiKey | ✅ | [Link](https://developers.glitterly.app) |
| **Google Firebase** | Google's mobile application development platform that helps build, improve, a... | 🔑 ApiKey | ✅ | [Link](https://firebase.google.com/docs) |
| **Google Fonts** | Metadata for all families served by Google Fonts. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/fonts/docs/developer_api) |
| **Google Keep** | API to read, write, and format Google Keep notes. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/keep/api/reference/rest) |
| **Google Slides** | API to read, write, and format Google Slides presentations. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/slides/api/reference/rest) |
| **Gorest** | Online REST API for Testing and Prototyping. | 🔐 OAuth | ✅ | [Link](https://gorest.co.in/) |
| **Hasura** | GraphQL and REST API Engine with built in Authorization. | 🔑 ApiKey | ✅ | [Link](https://hasura.io/opensource/) |
| **host-t.com** | Basic DNS query via HTTP GET request. | No | ✅ | [Link](https://host-t.com) |
| **HTTP2.Pro** | Test endpoints for client and server HTTP/2 protocol support. | No | ✅ | [Link](https://http2.pro/doc/api) |
| **IBM Text to Speech** | Convert text to speech. | 🔑 ApiKey | ✅ | [Link](https://cloud.ibm.com/docs/text-to-speech/getting-started.html) |
| **Icanhazepoch** | Get Epoch time. | No | ✅ | [Link](https://icanhazepoch.com) |
| **Icanhazip** | IP Address API. | No | ✅ | [Link](https://major.io/icanhazip-com-faq/) |
| **Image-Charts** | Generate charts, QR codes and graph images. | No | ✅ | [Link](https://documentation.image-charts.com/) |
| **import.io** | Retrieve structured data from a website or RSS feed. | 🔑 ApiKey | ✅ | [Link](http://api.docs.import.io/) |
| **ip-fast.com** | IP address, country and city. | No | ✅ | [Link](https://ip-fast.com/docs/) |
| **IP2WHOIS Information Lookup** | WHOIS domain name lookup. | 🔑 ApiKey | ✅ | [Link](https://www.ip2whois.com/) |
| **ipfind.io** | Geographic location of an IP address or any domain name along with some other... | 🔑 ApiKey | ✅ | [Link](https://ipfind.io) |
| **jsDelivr** | Package info and download stats on jsDelivr CDN. | No | ✅ | [Link](https://github.com/jsdelivr/data.jsdelivr.com) |
| **JSON 2 JSONP** | Convert JSON to JSONP (on-the-fly) for easy cross-domain data requests using ... | No | ✅ | [Link](https://json2jsonp.com/) |
| **Kroki** | Creates diagrams from textual descriptions. | No | ✅ | [Link](https://kroki.io) |
| **License-API** | Unofficial REST API for choosealicense.com. | No | ✅ | [Link](https://github.com/cmccandless/license-api/blob/master/README.md) |
| **Logs.to** | Generate logs. | 🔑 ApiKey | ✅ | [Link](https://logs.to/) |
| **Lua Decompiler** | Online Lua 5.1 Decompiler. | No | ✅ | [Link](https://lua-decompiler.ferib.dev/) |
| **MAC address vendor lookup** | Retrieve vendor details and other information regarding a given MAC address o... | 🔑 ApiKey | ✅ | [Link](https://macaddress.io/api) |
| **Micro DB** | Simple database service. | 🔑 ApiKey | ✅ | [Link](https://m3o.com/db) |
| **MicroENV** | Fake Rest API for developers. | No | ✅ | [Link](https://microenv.com/) |
| **Mocky** | Mock user defined test JSON for REST API endpoints. | No | ✅ | [Link](https://designer.mocky.io/) |
| **MY IP** | Get IP address information. | No | ✅ | [Link](https://www.myip.com/api-docs/) |
| **NetworkCalc** | Network calculators, including subnets, DNS, binary, and security tools. | No | ✅ | [Link](https://networkcalc.com/api/docs) |
| **npm Registry** | Query information about your favorite Node.js libraries programatically. | No | ✅ | [Link](https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md) |
| **Open Page Rank** | API for calculating and comparing metrics of different websites using Page Ra... | 🔑 ApiKey | ✅ | [Link](https://www.domcop.com/openpagerank/) |
| **OpenAPIHub** | The All-in-one API Platform. | 🔑 ApiKey | ✅ | [Link](https://hub.openapihub.com/) |
| **OpenGraphr** | Really simple API to retrieve Open Graph data from an URL. | 🔑 ApiKey | ✅ | [Link](https://opengraphr.com/docs/1.0/overview) |
| **oyyi** | API for Fake Data, image/video conversion, optimization, pdf optimization and... | No | ✅ | [Link](https://oyyi.xyz/docs/1.0) |
| **PageCDN** | Public API for javascript, css and font libraries on PageCDN. | 🔑 ApiKey | ✅ | [Link](https://pagecdn.com/docs/public-api) |
| **Postman** | Tool for testing APIs. | 🔑 ApiKey | ✅ | [Link](https://www.postman.com/postman/workspace/postman-public-workspace/documentation/12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a) |
| **ProxyCrawl** | Scraping and crawling anticaptcha service. | 🔑 ApiKey | ✅ | [Link](https://proxycrawl.com) |
| **ProxyKingdom** | Rotating Proxy API that produces a working proxy on every request. | 🔑 ApiKey | ✅ | [Link](https://proxykingdom.com) |
| **Pusher Beams** | Push notifications for Android & iOS. | 🔑 ApiKey | ✅ | [Link](https://pusher.com/beams) |
| **QR code** | Create an easy to read QR code and URL shortener. | No | ✅ | [Link](https://www.qrtag.net/api/) |
| **Qrcode Monkey** | Integrate custom and unique looking QR codes into your system or workflow. | No | ✅ | [Link](https://www.qrcode-monkey.com/qr-code-api-with-logo/) |
| **Random Stuff** | Can be used to get AI Response, jokes, memes, and much more at lightning-fast... | 🔑 ApiKey | ✅ | [Link](https://api-docs.pgamerx.com/) |
| **Rejax** | Reverse AJAX service to notify clients. | 🔑 ApiKey | ✅ | [Link](https://rejax.io/) |
| **RSS feed to JSON** | Returns RSS feed in JSON format using feed URL. | No | ✅ | [Link](https://rss-to-json-serverless-api.vercel.app) |
| **SavePage.io** | A free, RESTful API used to screenshot any desktop, or mobile website. | 🔑 ApiKey | ✅ | [Link](https://www.savepage.io) |
| **ScrapeNinja** | Scraping API with Chrome fingerprint and residential proxies. | 🔑 ApiKey | ✅ | [Link](https://scrapeninja.net) |
| **ScraperApi** | Easily build scalable web scrapers. | 🔑 ApiKey | ✅ | [Link](https://www.scraperapi.com) |
| **scraperBox** | Undetectable web scraping API. | 🔑 ApiKey | ✅ | [Link](https://scraperbox.com/) |
| **scrapestack** | Real-time, Scalable Proxy & Web Scraping REST API. | 🔑 ApiKey | ✅ | [Link](https://scrapestack.com/) |
| **ScrapingAnt** | Headless Chrome scraping with a simple API. | 🔑 ApiKey | ✅ | [Link](https://scrapingant.com) |
| **ScrapingDog** | Proxy API for Web scraping. | 🔑 ApiKey | ✅ | [Link](https://www.scrapingdog.com/) |
| **ScreenshotAPI.net** | Create pixel-perfect website screenshots. | 🔑 ApiKey | ✅ | [Link](https://screenshotapi.net/) |
| **Serialif Color** | Color conversion, complementary, grayscale and contrasted text. | No | ✅ | [Link](https://color.serialif.com/) |
| **Sheetsu** | Easy google sheets integration. | 🔑 ApiKey | ✅ | [Link](https://sheetsu.com/) |
| **SHOUTCLOUD** | ALL-CAPS AS A SERVICE. | No | No | [Link](http://shoutcloud.io/) |
| **Sonar** | Project Sonar DNS Enumeration API. | No | ✅ | [Link](https://github.com/Cgboal/SonarSearch) |
| **SonarQube** | SonarQube REST APIs to detect bugs, code smells & security vulnerabilities. | 🔐 OAuth | ✅ | [Link](https://sonarcloud.io/web_api) |
| **StackExchange** | Q&A forum for developers. | 🔐 OAuth | ✅ | [Link](https://api.stackexchange.com/) |
| **Statically** | A free CDN for developers. | No | ✅ | [Link](https://statically.io/) |
| **Supportivekoala** | Autogenerate images with template. | 🔑 ApiKey | ✅ | [Link](https://developers.supportivekoala.com/) |
| **WebScraping.AI** | Web Scraping API with built-in proxies and JS rendering. | 🔑 ApiKey | ✅ | [Link](https://webscraping.ai/) |
| **ZenRows** | Web Scraping API that bypasses anti-bot solutions while offering JS rendering... | 🔑 ApiKey | ✅ | [Link](https://www.zenrows.com/) |
| **Codeforces** | Get access to Codeforces data. | 🔑 ApiKey | ✅ | [Link](https://codeforces.com/apiHelp) |
| **Hackerearth** | For compiling and running code in several languages. | 🔑 ApiKey | ✅ | [Link](https://www.hackerearth.com/docs/wiki/developers/v4/) |
| **Judge0 CE** | Online code execution system. | 🔑 ApiKey | ✅ | [Link](https://ce.judge0.com/) |
| **KONTESTS** | For upcoming and ongoing competitive coding contests. | No | ✅ | [Link](https://kontests.net/api) |
| **Mintlify** | For programmatically generating documentation for code. | 🔑 ApiKey | ✅ | [Link](https://docs.mintlify.com) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="continuous-integration"></a>⚙️ Continuous Integration

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **AppVeyor** | CI/CD builds API (free for OSS). | 🔑 ApiKey | ✅ | [Link](https://www.appveyor.com/docs/api/) |
| **Azure DevOps Health** | Resource health helps you diagnose and get support when an Azure issue impact... | 🔑 ApiKey | No | [Link](https://docs.microsoft.com/en-us/rest/api/resourcehealth) |
| **Bitrise** | Build tool and processes integrations to create efficient development pipelines. | 🔑 ApiKey | ✅ | [Link](https://api-docs.bitrise.io/) |
| **Buddy** | The fastest continuous integration and continuous delivery platform. | 🔐 OAuth | ✅ | [Link](https://buddy.works/docs/api/getting-started/overview) |
| **Buildkite** | Pipeline and build automation API. | 🔑 ApiKey | ✅ | [Link](https://buildkite.com/docs/apis/rest-api) |
| **CircleCI** | CI pipelines, workflows, and artifacts API. | 🔑 ApiKey | ✅ | [Link](https://circleci.com/docs/api/v2/) |
| **Cirrus CI** | CI pipelines and task automation API. | 🔑 ApiKey | ✅ | [Link](https://cirrus-ci.org/api/) |
| **Codeship** | Codeship is a Continuous Integration Platform in the cloud. | 🔑 ApiKey | ✅ | [Link](https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-overview/) |
| **Drone** | CI pipeline API for Drone server. | 🔑 ApiKey | ✅ | [Link](https://docs.drone.io/api/) |
| **Jenkins** | Automation server remote API. | 🔑 ApiKey | ✅ | [Link](https://www.jenkins.io/doc/book/using/remote-access-api/) |
| **Semaphore** | CI/CD projects, workflows, and jobs API. | 🔑 ApiKey | ✅ | [Link](https://docs.semaphoreci.com/reference/api) |
| **TeamCity** | Build server REST API. | 🔑 ApiKey | ✅ | [Link](https://www.jetbrains.com/help/teamcity/rest/teamcity-rest-api-documentation.html) |
| **Travis CI** | Sync your GitHub projects with Travis CI to test your code in minutes. | 🔑 ApiKey | ✅ | [Link](https://docs.travis-ci.com/api/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="text-analysis-nlp"></a>📝 Text Analysis & NLP

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Cloudmersive Natural Language Processing** | Natural language processing and text analysis. | 🔑 ApiKey | ✅ | [Link](https://www.cloudmersive.com/nlp-api) |
| **Code Detection API** | Detect, label, format and enrich the code in your app or in your data pipeline. | 🔐 OAuth | ✅ | [Link](https://codedetectionapi.runtime.dev) |
| **Dandelion** | Entity extraction and text analytics API. | 🔑 ApiKey | ✅ | [Link](https://dandelion.eu/docs/api/) |
| **DeepL** | Translation and multilingual text API. | 🔑 ApiKey | ✅ | [Link](https://developers.deepl.com/docs-api) |
| **Detect Language** | Detects text language. | 🔑 ApiKey | ✅ | [Link](https://detectlanguage.com/) |
| **Eden AI** | Unified NLP APIs across providers. | 🔑 ApiKey | ✅ | [Link](https://docs.edenai.co/reference/introduction) |
| **ELI** | Natural Language Processing Tools for Thai Language. | 🔑 ApiKey | ✅ | [Link](https://nlp.insightera.co.th/docs/v1.0) |
| **Google Cloud Natural** | Natural language understanding technology, including sentiment, entity and sy... | 🔑 ApiKey | ✅ | [Link](https://cloud.google.com/natural-language/docs/) |
| **Hirak OCR** | Image to text -text recognition- from image more than 100 language, accurate,... | 🔑 ApiKey | ✅ | [Link](https://ocr.hirak.site/) |
| **Hirak Translation** | Translate between 21 of most used languages, accurate, unlimited requests. | 🔑 ApiKey | ✅ | [Link](https://translate.hirak.site/) |
| **LanguageTool** | Grammar and style checking API. | No | ✅ | [Link](https://languagetool.org/http-api/swagger-ui/#/) |
| **Lecto Translation** | Translation API with free tier and reasonable prices. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/lecto-lecto-default/api/lecto-translation/) |
| **LibreTranslate** | Free and open-source translation API (**Self-hosted, No Auth**). | No | ✅ | [Link](https://libretranslate.com/) |
| **ParallelDots** | Sentiment and NLP analysis APIs. | 🔑 ApiKey | ✅ | [Link](https://komprehend.io/) |
| **Sapling** | Grammar correction and writing APIs. | 🔑 ApiKey | ✅ | [Link](https://sapling.ai/docs/) |
| **Semantria** | Text Analytics with sentiment analysis, categorization & named entity extraction. | 🔐 OAuth | ✅ | [Link](https://semantria.readme.io/docs) |
| **Sentiment Analysis** | Multilingual sentiment analysis of texts from different sources. | 🔑 ApiKey | ✅ | [Link](https://www.meaningcloud.com/developer/sentiment-analysis) |
| **TextRazor** | NLP extraction and classification API. | 🔑 ApiKey | ✅ | [Link](https://www.textrazor.com/docs/rest) |
| **Tisane** | Text Analytics with focus on detection of abusive content and law enforcement... | 🔐 OAuth | ✅ | [Link](https://tisane.ai/) |
| **Watson Natural Language Understanding** | Natural language processing for advanced text analysis. | 🔐 OAuth | ✅ | [Link](https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding) |
| **Wit.ai** | Intent/entity extraction for text/voice. | 🔑 ApiKey | ✅ | [Link](https://wit.ai/docs/http/20240304/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="iot-smart-devices"></a>🏠 IoT & Smart Devices

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Adafruit IO** | IoT feed/data API with free tier. | 🔑 ApiKey | ✅ | [Link](https://io.adafruit.com/api/docs/) |
| **Arduino IoT** | Arduino IoT Cloud API. | 🔑 ApiKey | ✅ | [Link](https://www.arduino.cc/reference/en/iot/) |
| **Blynk** | IoT device control from cloud. | 🔑 ApiKey | ✅ | [Link](https://docs.blynk.io/) |
| **Blynk-Cloud** | Control IoT Devices from Blynk IoT Cloud. | 🔑 ApiKey | No | [Link](https://blynkapi.docs.apiary.io/#) |
| **Home Assistant** | Self-hosted home automation REST API. | 🔑 ApiKey | ✅ | [Link](https://developers.home-assistant.io/docs/api/rest/) |
| **IFTTT** | IFTTT Connect API. | No | ✅ | [Link](https://platform.ifttt.com/docs/connect_api) |
| **Particle Cloud** | IoT device management and data API. | 🔑 ApiKey | ✅ | [Link](https://docs.particle.io/reference/cloud-apis/api/) |
| **ThingsBoard** | Open-source IoT platform REST API. | 🔑 ApiKey | ✅ | [Link](https://thingsboard.io/docs/reference/rest-api/) |
| **Tuya Cloud** | Smart device management APIs. | 🔑 ApiKey | ✅ | [Link](https://developer.tuya.com/en/docs/cloud/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="open-source-projects"></a>🔓 Open Source Projects

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Countly** | Countly web analytics. | No | No | [Link](https://api.count.ly/reference) |
| **Creative Commons Catalog** | Search among openly licensed and public domain works. | 🔐 OAuth | ✅ | [Link](https://api.creativecommons.engineering/) |
| **deps.dev** | Open package/dependency intelligence by Google. | No | ✅ | [Link](https://docs.deps.dev/api/) |
| **Drupal.org** | Drupal.org. | No | ✅ | [Link](https://www.drupal.org/drupalorg/docs/api) |
| **ecosyste.ms** | Open source ecosystem data APIs. | No | ✅ | [Link](https://docs.ecosyste.ms/) |
| **GitHub Contribution Chart Generator** | Create an image of your GitHub contributions. | No | ✅ | [Link](https://github-contributions.vercel.app) |
| **GitHub ReadMe Stats** | Add dynamically generated statistics to your GitHub profile ReadMe. | No | ✅ | [Link](https://github.com/anuraghazra/github-readme-stats) |
| **Metabase** | An open source Business Intelligence server to share data and analytics insid... | No | ✅ | [Link](https://www.metabase.com/) |
| **Packagist** | PHP package repository API. | No | ✅ | [Link](https://packagist.org/apidoc) |
| **PyPI JSON API** | Python package metadata API. | No | ✅ | [Link](https://docs.pypi.org/api/json/) |
| **Repology** | Package version tracking across repos. | No | ✅ | [Link](https://repology.org/api) |
| **RubyGems** | Ruby package repository API. | No | ✅ | [Link](https://guides.rubygems.org/rubygems-org-api) |
| **Shields.io** | Quality metadata badges for open source projects (**No Auth**). | No | ✅ | [Link](https://shields.io/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="dictionaries"></a>📖 Dictionaries

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Free Dictionary API** | Free English dictionary API. | No | ✅ | [Link](https://dictionaryapi.dev/) |
| **Merriam-Webster** | Dictionary and thesaurus. | 🔑 ApiKey | ✅ | [Link](https://dictionaryapi.com/) |
| **Oxford Dictionaries** | English dictionary and language data. | 🔑 ApiKey | ✅ | [Link](https://developer.oxforddictionaries.com/) |
| **Urban Dictionary** | Slang dictionary. | No | ✅ | [Link](https://api.urbandictionary.com/v0/define?term=api) |
| **WordsAPI** | Word definitions, synonyms, antonyms. | 🔑 ApiKey | ✅ | [Link](https://www.wordsapi.com/) |
| **Lingua Robot** | Word definitions and language detection (**No Auth**). | No | ✅ | [Link](https://www.linguarobot.io/) |
| **Datamuse** | Word-finding query engine (**No Auth**). | No | ✅ | [Link](https://www.datamuse.com/api/) |
| **Wiktionary API** | Open dictionary and thesaurus data. | No | ✅ | [Link](https://en.wiktionary.org/w/api.php) |
| **Synonyms API** | Find synonyms for any word. | No | ✅ | [Link](https://api-ninjas.com/api/thesaurus) |
| **Purgomalum** | Profanity filter API. | No | ✅ | [Link](https://www.purgomalum.com/) |
| **Chinese Character Web** | Chinese character definitions and pronunciations. | No | No | [Link](http://ccdb.hemiola.com/) |
| **Chinese Text Project** | Online open-access digital library for pre-modern Chinese texts. | No | ✅ | [Link](https://ctext.org/tools/api) |
| **Collins** | Bilingual Dictionary and Thesaurus Data. | 🔑 ApiKey | ✅ | [Link](https://api.collinsdictionary.com/api/v1/documentation/html/) |
| **Synonyms** | Synonyms, thesaurus and antonyms information for any given word. | 🔑 ApiKey | ✅ | [Link](https://www.synonyms.com/synonyms_api.php) |
| **Wordnik** | Dictionary Data. | 🔑 ApiKey | ✅ | [Link](https://developer.wordnik.com) |
| **Words** | Definitions and synonyms for more than 150,000 words. | 🔑 ApiKey | ✅ | [Link](https://www.wordsapi.com/docs/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="education"></a>🎓 Education

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Universities List** | List of universities worldwide. | No | ✅ | [Link](http://universities.hipolabs.com/) |
| **Wikipedia API** | Free encyclopedia data and content (**No Auth**). | No | ✅ | [Link](https://www.mediawiki.org/wiki/API:Main_page) |
| **Wikidata** | Structured knowledge base (**No Auth**). | No | ✅ | [Link](https://www.wikidata.org/wiki/Wikidata:Data_access) |
| **OpenAlex** | Open catalog of scholarly papers (**No Auth**). | No | ✅ | [Link](https://docs.openalex.org/) |
| **Crossref** | Scholarly article metadata (**No Auth**). | No | ✅ | [Link](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) |
| **Calendarific** | Worldwide holidays for 230+ countries. | 🔑 ApiKey | ✅ | [Link](https://calendarific.com/api-documentation) |
| **Coursera API** | Course catalog and metadata. | 🔐 OAuth | ✅ | [Link](https://build.coursera.org/app-platform/catalog) |
| **edX API** | Online course catalog. | 🔐 OAuth | ✅ | [Link](https://courses.edx.org/api-docs/) |
| **Periodic Table** | Chemical element data. | No | ✅ | [Link](https://api-ninjas.com/api/periodictable) |
| **Semantic Scholar** | Scholarly papers and citation graph data. | No | ✅ | [Link](https://api.semanticscholar.org/api-docs/) |
| **CORE API** | Open access research paper metadata. | 🔑 ApiKey | ✅ | [Link](https://api.core.ac.uk/docs/v3) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="calendar-holidays"></a>📅 Calendar & Holidays

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Festivo Public Holidays** | Public holidays and observance data API. | 🔑 ApiKey | ✅ | [Link](https://docs.getfestivo.com/docs/products/public-holidays-api/intro) |
| **HolidayAPI** | Holidays and observances by country and date. | 🔑 ApiKey | ✅ | [Link](https://holidayapi.com/) |
| **Namedays Calendar** | Nameday lookups by date and locale. | No | ✅ | [Link](https://nameday.abalin.net/) |
| **Non-Working Days** | Non-working day and holiday checks. | No | ✅ | [Link](https://isdayoff.ru/) |
| **UK Bank Holidays** | Official UK bank holiday dataset API. | No | ✅ | [Link](https://www.gov.uk/bank-holidays.json) |
| **Public Holidays** | Data on national, regional, and religious holidays via API. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/holidays-api) |
| **Checkiday - National Holiday API** | Industry-leading Holiday API. Over 5,000 holidays and thousands of descriptio... | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/checkiday-api) |
| **Church Calendar** | Catholic liturgical calendar. | No | No | [Link](http://calapi.inadiutorium.cz/) |
| **Czech Namedays Calendar** | Lookup for a name and returns nameday date. | No | No | [Link](https://svatky.adresa.info) |
| **Hebrew Calendar** | Convert between Gregorian and Hebrew, fetch Shabbat and Holiday times, etc. | No | No | [Link](https://www.hebcal.com/home/developer-apis) |
| **LectServe** | Protestant liturgical calendar. | No | No | [Link](http://www.lectserve.com) |
| **Russian Calendar** | Check if a date is a Russian holiday or not. | No | ✅ | [Link](https://github.com/egno/work-calendar) |

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
| **US Census** | US demographics, economics, housing data. | 🔑 ApiKey | ✅ | [Link](https://www.census.gov/data/developers/data-sets.html) |
| **USPTO** | US patent data and applications (**No Auth**). | No | ✅ | [Link](https://developer.uspto.gov/api-catalog) |
| **Eurostat** | European Union statistics database (**No Auth**). | No | ✅ | [Link](https://ec.europa.eu/eurostat/web/main/data/web-services) |
| **API Setu** | An Indian Government platform that provides a lot of APIS for KYC, business, ... | No | ✅ | [Link](https://www.apisetu.gov.in/) |
| **Archive.org** | The Internet Archive. | No | ✅ | [Link](https://archive.readme.io/docs) |
| **Black History Facts** | Contribute or search one of the largest black history fact databases on the web. | 🔑 ApiKey | ✅ | [Link](https://www.blackhistoryapi.io/docs) |
| **BotsArchive** | JSON formatted details about Telegram Bots available in database. | No | ✅ | [Link](https://botsarchive.com/docs.html) |
| **Callook.info** | United States ham radio callsigns. | No | ✅ | [Link](https://callook.info) |
| **CARTO** | Location Information Prediction. | 🔑 ApiKey | ✅ | [Link](https://carto.com/) |
| **CollegeScoreCard.ed.gov** | Data on higher education institutions in the United States. | No | ✅ | [Link](https://collegescorecard.ed.gov/data/) |
| **Enigma Public** | Broadest collection of public data. | 🔑 ApiKey | ✅ | [Link](https://developers.enigma.com/docs) |
| **French Address Search** | Address search via the French Government. | No | ✅ | [Link](https://geo.api.gouv.fr/adresse) |
| **GENESIS** | Federal Statistical Office Germany. | 🔐 OAuth | ✅ | [Link](https://www.destatis.de/EN/Service/OpenData/api-webservice.html) |
| **Joshua Project** | People groups of the world with the fewest followers of Christ. | 🔑 ApiKey | ✅ | [Link](https://api.joshuaproject.net/) |
| **Kaggle** | Create and interact with Datasets, Notebooks, and connect with Kaggle. | 🔑 ApiKey | ✅ | [Link](https://www.kaggle.com/docs/api) |
| **LinkPreview** | Get JSON formatted summary with title, description and preview image for any ... | 🔑 ApiKey | ✅ | [Link](https://www.linkpreview.net) |
| **Lowy Asia Power Index** | Get measure resources and influence to rank the relative power of states in Asia. | No | ✅ | [Link](https://github.com/0x0is1/lowy-index-api-docs) |
| **Microlink.io** | Extract structured data from any website. | No | ✅ | [Link](https://microlink.io) |
| **Nasdaq Data Link** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://docs.data.nasdaq.com/) |
| **Nobel Prize** | Open data about nobel prizes and events. | No | ✅ | [Link](https://www.nobelprize.org/about/developer-zone-2/) |
| **Open Data Minneapolis** | Spatial (GIS) and non-spatial city data for Minneapolis. | No | ✅ | [Link](https://opendata.minneapolismn.gov/) |
| **openAFRICA** | Large datasets repository of African open data. | No | ✅ | [Link](https://africaopendata.org/) |
| **OpenCorporates** | Data on corporate entities and directors in many countries. | 🔑 ApiKey | ✅ | [Link](http://api.opencorporates.com/documentation/API-Reference) |
| **OpenSanctions** | Data on international sanctions, crime and politically exposed persons. | No | ✅ | [Link](https://www.opensanctions.org/docs/api/) |
| **PeakMetrics** | News articles and public datasets. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/peakmetrics-peakmetrics-default/api/peakmetrics-news) |
| **Recreation Information Database** | Recreational areas, federal lands, historic sites, museums, and other attract... | 🔑 ApiKey | ✅ | [Link](https://ridb.recreation.gov/) |
| **Teleport** | Quality of Life Data. | No | ✅ | [Link](https://developers.teleport.org/) |
| **Umeå Open Data** | Open data of the city Umeå in northen Sweden. | No | ✅ | [Link](https://opendata.umea.se/api/) |
| **University of Oslo** | Courses, lecture videos, detailed information for courses etc. for the Univer... | No | ✅ | [Link](https://data.uio.no/) |
| **UPC database** | More than 1.5 million barcode numbers from all around the world. | 🔑 ApiKey | ✅ | [Link](https://upcdatabase.org/api) |
| **Urban Observatory** | The largest set of publicly available real time urban data in the UK. | No | No | [Link](https://urbanobservatory.ac.uk) |
| **EPO** | European patent search system api. | 🔐 OAuth | ✅ | [Link](https://developers.epo.org/) |
| **PatentsView** | API is intended to explore and visualize trends/patterns across the US innova... | No | ✅ | [Link](https://patentsview.org/apis/purpose) |
| **TIPO** | Taiwan patent search system api. | 🔑 ApiKey | ✅ | [Link](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="email-sms"></a>📧 Email & SMS

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Mailgun** | Email service for developers (free tier). | 🔑 ApiKey | ✅ | [Link](https://documentation.mailgun.com/) |
| **Mailchimp** | Email marketing and audience management APIs. | 🔑 ApiKey | ✅ | [Link](https://mailchimp.com/developer/) |
| **Mailjet** | Transactional email and marketing API. | 🔑 ApiKey | ✅ | [Link](https://www.mailjet.com/) |
| **Resend** | Modern email API for developers (free tier). | 🔑 ApiKey | ✅ | [Link](https://resend.com/docs/api-reference/introduction) |
| **SendGrid** | Email delivery service (free tier: 100/day). | 🔑 ApiKey | ✅ | [Link](https://docs.sendgrid.com/api-reference) |
| **Twilio** | SMS, voice, and messaging (trial credits). | 🔑 ApiKey | ✅ | [Link](https://www.twilio.com/docs/usage/api) |
| **Tomba** | Email finder and verifier API. | 🔑 ApiKey | ✅ | [Link](https://tomba.io/api) |
| **Vonage (Nexmo)** | SMS and voice APIs (trial credits). | 🔑 ApiKey | ✅ | [Link](https://developer.vonage.com/api) |
| **OneSignal** | Push notifications platform (free tier). | 🔑 ApiKey | ✅ | [Link](https://documentation.onesignal.com/reference) |
| **Pushover** | Simple push notifications API. | 🔑 ApiKey | ✅ | [Link](https://pushover.net/api) |
| **Mailtrap** | Email testing and sending API. | 🔑 ApiKey | ✅ | [Link](https://api-docs.mailtrap.io/) |
| **Email Validation** | Validate email addresses for deliverability and spam. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/email-verification-validation-api) |
| **Cloudmersive Validate** | Validate email addresses, phone numbers, VAT numbers and domain names. | 🔑 ApiKey | ✅ | [Link](https://cloudmersive.com/validate-api) |
| **Disify** | Validate and detect disposable and temporary email addresses. | No | ✅ | [Link](https://www.disify.com/) |
| **DropMail** | GraphQL API for creating and managing ephemeral e-mail inboxes. | No | ✅ | [Link](https://dropmail.me/api/#live-demo) |
| **EVA** | Validate email addresses. | No | ✅ | [Link](https://eva.pingutil.com/) |
| **Guerrilla Mail** | Disposable temporary Email addresses. | No | ✅ | [Link](https://www.guerrillamail.com/GuerrillaMailAPI.html) |
| **ImprovMX** | API for free email forwarding service. | 🔑 ApiKey | ✅ | [Link](https://improvmx.com/api) |
| **Kickbox** | Email verification API. | No | ✅ | [Link](https://open.kickbox.com/) |
| **mail.gw** | 10 Minute Mail. | No | ✅ | [Link](https://docs.mail.gw) |
| **mail.tm** | Temporary Email Service. | No | ✅ | [Link](https://docs.mail.tm) |
| **MailboxValidator** | Validate email address to improve deliverability. | 🔑 ApiKey | ✅ | [Link](https://www.mailboxvalidator.com/api-email-free) |
| **MailCheck.ai** | Prevent users to sign up with temporary email addresses. | No | ✅ | [Link](https://www.mailcheck.ai/#documentation) |
| **Verifier** | Verifies that a given email is real. | 🔑 ApiKey | ✅ | [Link](https://verifier.meetchopra.com/docs#/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="phone-telephony"></a>📱 Phone & Telephony

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **46elks** | SMS and voice telephony API. | 🔑 ApiKey | ✅ | [Link](https://46elks.com/docs) |
| **Apifonica** | Voice call automation API. | 🔑 ApiKey | ✅ | [Link](https://www.apifonica.com/docs/voice-api/) |
| **Bandwidth** | Voice, messaging, and phone number APIs. | 🔑 ApiKey | ✅ | [Link](https://dev.bandwidth.com/docs/) |
| **MessageBird** | SMS and omnichannel messaging APIs. | 🔑 ApiKey | ✅ | [Link](https://developers.messagebird.com/api/) |
| **NeutrinoAPI Phone Validate** | Phone validation and carrier lookup. | 🔑 ApiKey | ✅ | [Link](https://www.neutrinoapi.com/api/phone-validate/) |
| **Phone Specification** | Rest Api for Phone specifications. | No | ✅ | [Link](https://github.com/azharimm/phone-specs-api) |
| **Phone Validation** | Validate phone numbers globally. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/phone-validation-api) |
| **Plivo** | Voice and SMS communication APIs. | 🔑 ApiKey | ✅ | [Link](https://www.plivo.com/docs/home) |
| **Sinch** | SMS, voice, and verification APIs. | 🔑 ApiKey | ✅ | [Link](https://developers.sinch.com/) |
| **Telnyx** | Telephony, messaging, and SIP APIs. | 🔑 ApiKey | ✅ | [Link](https://developers.telnyx.com/api-reference/overview) |
| **Textbelt** | Lightweight SMS sending API. | 🔑 ApiKey | ✅ | [Link](https://www.textbelt.com/) |
| **Veriphone** | Phone number validation & carrier lookup. | 🔑 ApiKey | ✅ | [Link](https://veriphone.io) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="entertainment"></a>🎮 Entertainment

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **OMDb** | Open Movie Database. | 🔑 ApiKey | ✅ | [Link](http://www.omdbapi.com/) |
| **Quiz API** | Random trivia questions (**No Auth**). | No | ✅ | [Link](https://quizapi.io/) |
| **Activities when get bored** | Random suggestions for activities. | No | ✅ | [Link](https://rapidapi.com/bored/api/bored-api/) |
| **Simkl** | Movies, TV, Anime metadata. | 🔑 ApiKey | ✅ | [Link](https://simkl.com/apidoc/) |
| **TMDb** | The Movie Database. | 🔑 ApiKey | ✅ | [Link](https://developers.themoviedb.org/3) |
| **TVmaze** | TV shows and episode data (**No Auth**). | No | ✅ | [Link](https://www.tvmaze.com/api) |
| **Trakt** | TV and Movie tracking. | 🔐 OAuth | ✅ | [Link](https://trakt.docs.apiary.io/) |
| **Watchmode** | Streaming availability. | 🔑 ApiKey | ✅ | [Link](https://api.watchmode.com/) |
| **Trivia API** | Trivia questions in various categories (**No Auth**). | No | ✅ | [Link](https://the-trivia-api.com/) |
| **StreamElements** | Twitch/YouTube live streaming data & overlays. | 🔑 ApiKey | ✅ | [Link](https://dev.streamelements.com/) |
| **TheTVDB** | TV database with episodes and artwork. | 🔑 ApiKey | ✅ | [Link](https://thetvdb.github.io/v4-api/) |
| **Board Game Atlas** | Board game database and reviews. | 🔑 ApiKey | ✅ | [Link](https://www.boardgameatlas.com/api/docs) |
| **Corporate Buzz Words** | REST API for Corporate Buzz Words. | No | ✅ | [Link](https://github.com/sameerkumar18/corporate-bs-generator-api) |
| **Fun Fact** | A simple HTTPS api that can randomly select and return a fact from the FFA da... | No | ✅ | [Link](https://api.aakhilv.me) |
| **Meme Maker** | REST API for create your own meme. | No | ✅ | [Link](https://mememaker.github.io/API/) |
| **NaMoMemes** | Memes on Narendra Modi. | No | ✅ | [Link](https://github.com/theIYD/NaMoMemes) |
| **Techy** | JSON and Plaintext API for tech-savvy sounding phrases. | No | ✅ | [Link](https://techy-api.vercel.app/) |
| **Yo Momma Jokes** | REST API for Yo Momma Jokes. | No | ✅ | [Link](https://github.com/beanboi7/yomomma-apiv2) |
| **Biriyani As A Service** | Biriyani images placeholder. | No | ✅ | [Link](https://biriyani.anoram.com/) |
| **FOAAS** | Fuck Off As A Service. | No | No | [Link](http://www.foaas.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="events"></a>🎪 Events

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Eventbrite** | Find events. | 🔐 OAuth | ✅ | [Link](https://www.eventbrite.com/platform/api/) |
| **Eventyay** | Open-source event management API. | No | ✅ | [Link](https://api.eventyay.com/) |
| **Luma** | Event creation and attendee APIs. | 🔑 ApiKey | ✅ | [Link](https://docs.luma.com/reference/getting-started) |
| **OpenAgenda** | Event agenda and discovery API. | 🔑 ApiKey | ✅ | [Link](https://developers.openagenda.com/) |
| **PredictHQ** | Event intelligence and impact API. | 🔑 ApiKey | ✅ | [Link](https://docs.predicthq.com/) |
| **pretix** | Ticketing and event operations API. | 🔑 ApiKey | ✅ | [Link](https://docs.pretix.eu/dev/api/index.html) |
| **SeatGeek** | Search events, venues and performers. | 🔑 ApiKey | ✅ | [Link](https://platform.seatgeek.com/) |
| **Sessionize** | CFP sessions and speakers API. | No | ✅ | [Link](https://sessionize.com/playbook/api/) |
| **Ti.to** | Event ticketing and registrations API. | 🔑 ApiKey | ✅ | [Link](https://ti.to/docs/api) |
| **Ticket Tailor** | Ticketing and order management API. | 🔑 ApiKey | ✅ | [Link](https://developers.tickettailor.com/) |
| **Ticketmaster** | Search events, attractions, or venues. | 🔑 ApiKey | ✅ | [Link](http://developer.ticketmaster.com/products-and-docs/apis/getting-started/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="podcasts"></a>🎙️ Podcasts

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Acast** | Podcast platform and publisher APIs. | 🔑 ApiKey | ✅ | [Link](https://developers.acast.com/) |
| **Audioboom** | Podcast metadata and episode endpoints. | No | ✅ | [Link](https://api.audioboom.com/) |
| **Buzzsprout** | Podcast hosting and episodes API. | 🔑 ApiKey | ✅ | [Link](https://www.buzzsprout.com/api) |
| **Fountain** | Podcast app developer API resources. | No | ✅ | [Link](https://fountain.fm/developer) |
| **fyyd** | Podcast search and metadata API. | No | ✅ | [Link](https://api.fyyd.de/) |
| **gpodder.net** | Podcast sync and subscriptions API. | No | ✅ | [Link](https://gpoddernet.readthedocs.io/en/latest/api/index.html) |
| **Podbean** | Podcast hosting and distribution API. | 🔐 OAuth | ✅ | [Link](https://developers.podbean.com/) |
| **Podcast Index** | Open podcast data and search. | 🔑 ApiKey | ✅ | [Link](https://podcastindex-org.github.io/docs-api/) |
| **Taddy** | GraphQL podcast search and metadata API. | 🔑 ApiKey | ✅ | [Link](https://taddy.org/developers) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="personality-quotes"></a>💭 Personality & Quotes

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Affirmations.dev** | Daily affirmations API. | No | ✅ | [Link](https://www.affirmations.dev/) |
| **API-Ninjas Quotes** | Curated quotes API. | 🔑 ApiKey | ✅ | [Link](https://api-ninjas.com/api/quotes) |
| **Dictum** | API to get access to the collection of the most inspiring expressions of mankind. | No | ✅ | [Link](https://github.com/fisenkodv/dictum) |
| **DummyJSON Quotes** | Fake quotes dataset API. | No | ✅ | [Link](https://dummyjson.com/docs/quotes) |
| **FavQs.com** | FavQs allows you to collect, discover and share your favorite quotes. | 🔑 ApiKey | ✅ | [Link](https://favqs.com/api) |
| **Forismatic** | Inspirational Quotes. | No | No | [Link](http://forismatic.com/en/api/) |
| **Inspiration** | Motivational and Inspirational quotes. | No | ✅ | [Link](https://inspiration.goprogram.ai/docs/) |
| **Medium** | Community of readers and writers offering unique perspectives on ideas. | 🔐 OAuth | ✅ | [Link](https://github.com/Medium/medium-api-docs) |
| **Programming Quotes** | Programming Quotes API for open source projects. | No | ✅ | [Link](https://github.com/skolakoda/programming-quotes-api) |
| **Quotable** | Random quotes (**No Auth**). | No | ✅ | [Link](https://github.com/lukePeavey/quotable) |
| **Quotes on Design** | Inspirational Quotes. | No | ✅ | [Link](https://quotesondesign.com/api/) |
| **Stoicism Quote** | Quotes about Stoicism. | No | ✅ | [Link](https://github.com/tlcheah2/stoic-quote-lambda-public-api) |
| **They Said So Quotes** | Quotes Trusted by many fortune brands around the world. | No | ✅ | [Link](https://theysaidso.com/api/) |
| **Traitify** | Assess, collect and analyze Personality. | No | ✅ | [Link](https://app.traitify.com/developer) |
| **Udemy(instructor)** | API for instructors on Udemy. | 🔑 ApiKey | ✅ | [Link](https://www.udemy.com/developers/instructor/) |
| **Vadivelu HTTP Codes** | On demand HTTP Codes with images. | No | ✅ | [Link](https://vadivelu.anoram.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="finance"></a>💰 Finance

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Alpaca** | Commission-free stock trading. | 🔑 ApiKey | ✅ | [Link](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/) |
| **Alpha Vantage** | Realtime and historical stock data. | 🔑 ApiKey | ✅ | [Link](https://www.alphavantage.co/) |
| **Binlist** | BIN/IIN Lookup. | No | ✅ | [Link](https://binlist.net/) |
| **CoinDesk** | Bitcoin Price Index (BPI) data (**No Auth**). | No | ✅ | [Link](https://www.coindesk.com/coindesk-api) |
| **Financial Modeling Prep** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://site.financialmodelingprep.com/developer/docs) |
| **Finnhub** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://finnhub.io/docs/api) |
| **FRED** | Economic data. | 🔑 ApiKey | ✅ | [Link](https://fred.stlouisfed.org/docs/api/fred/) |
| **Klarna** | Payments. | 🔑 ApiKey | ✅ | [Link](https://docs.klarna.com/api/) |
| **MercadoPago** | Payments. | 🔑 ApiKey | ✅ | [Link](https://www.mercadopago.com.br/developers/es/reference) |
| **Marketstack** | Real-time, intraday and historical market data. | 🔑 ApiKey | ✅ | [Link](https://marketstack.com/) |
| **Plaid** | Connect bank accounts. | 🔑 ApiKey | ✅ | [Link](https://www.plaid.com/docs) |
| **Polygon** | Stock market data. | 🔑 ApiKey | ✅ | [Link](https://polygon.io/) |
| **Square** | Payments, checkout, and commerce APIs. | 🔐 OAuth | ✅ | [Link](https://developer.squareup.com/reference/square) |
| **Stripe** | Payments. | 🔑 ApiKey | ✅ | [Link](https://stripe.com/docs/api) |
| **Tax Data API** | Tax rates and validation. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/tax_data-api) |
| **VAT Validation** | Validate VAT numbers and calculate VAT rates. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/vat-validation-rates-api) |
| **Aletheia** | Insider trading data, earnings call analysis, financial statements, and more. | 🔑 ApiKey | ✅ | [Link](https://aletheiaapi.com/) |
| **Banco do Brasil** | All Banco do Brasil financial transaction APIs. | 🔐 OAuth | ✅ | [Link](https://developers.bb.com.br/home) |
| **Bank Data API** | Instant IBAN and SWIFT number validation across the globe. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/bank_data-api) |
| **Billplz** | Payment platform. | 🔑 ApiKey | ✅ | [Link](https://www.billplz.com/api) |
| **Boleto.Cloud** | A api to generate boletos in Brazil. | 🔑 ApiKey | ✅ | [Link](https://boleto.cloud/) |
| **Citi** | All Citigroup account and statement data APIs. | 🔑 ApiKey | ✅ | [Link](https://sandbox.developerhub.citi.com/api-catalog-list) |
| **Econdb** | Global macroeconomic data. | No | ✅ | [Link](https://www.econdb.com/api/) |
| **Fed Treasury** | U.S. Department of the Treasury Data. | No | ✅ | [Link](https://fiscaldata.treasury.gov/api-documentation/) |
| **Finage** | Finage is a stock, currency, cryptocurrency, indices, and ETFs real-time & hi... | 🔑 ApiKey | ✅ | [Link](https://finage.co.uk) |
| **Front Accounting APIs** | Front accounting is multilingual and multicurrency software for small businesses. | 🔐 OAuth | ✅ | [Link](https://frontaccounting.com/fawiki/index.php?n=Devel.SimpleAPIModule) |
| **Hotstoks** | Stock market data powered by SQL. | 🔑 ApiKey | ✅ | [Link](https://hotstoks.com?utm_source=public-apis) |
| **IEX Cloud** | Realtime & Historical Stock and Market Data. | 🔑 ApiKey | ✅ | [Link](https://iexcloud.io/docs/api/) |
| **IG** | Spreadbetting and CFD Market Data. | 🔑 ApiKey | ✅ | [Link](https://labs.ig.com/gettingstarted) |
| **Indian Mutual Fund** | Get complete history of India Mutual Funds Data. | No | ✅ | [Link](https://www.mfapi.in/) |
| **Intrinio** | A wide selection of financial data feeds. | 🔑 ApiKey | ✅ | [Link](https://intrinio.com/) |
| **Mono** | Connect with users’ bank accounts and access transaction data in Africa. | 🔑 ApiKey | ✅ | [Link](https://mono.co/) |
| **Moov** | The Moov API makes it simple for platforms to send, receive, and store money. | 🔑 ApiKey | ✅ | [Link](https://docs.moov.io/api/) |
| **Nordigen** | Connect to bank accounts using official bank APIs and get raw transaction data. | 🔑 ApiKey | ✅ | [Link](https://nordigen.com/en/account_information_documenation/integration/quickstart_guide/) |
| **OpenFIGI** | Equity, index, futures, options symbology from Bloomberg LP. | 🔑 ApiKey | ✅ | [Link](https://www.openfigi.com/api) |
| **Portfolio Optimizer** | Portfolio analysis and optimization. | No | ✅ | [Link](https://portfoliooptimizer.io/) |
| **Razorpay IFSC** | Indian Financial Systems Code (Bank Branch Codes) | No | ✅ | [Link](https://razorpay.com/docs/) |
| **Real Time Finance** | Websocket API to access realtime stock data. | 🔑 ApiKey | No | [Link](https://github.com/Real-time-finance/finance-websocket-API/) |
| **SEC EDGAR Data** | API to access annual reports of public US companies. | No | ✅ | [Link](https://www.sec.gov/edgar/sec-api-documentation) |
| **SmartAPI** | Gain access to set of <SmartAPI> and create end-to-end broking services. | 🔑 ApiKey | ✅ | [Link](https://smartapi.angelbroking.com/) |
| **StockData** | Real-Time, Intraday & Historical Market Data, News and Sentiment API. | 🔑 ApiKey | ✅ | [Link](https://www.StockData.org) |
| **Styvio** | Realtime and historical stock data and current stock sentiment. | 🔑 ApiKey | ✅ | [Link](https://www.Styvio.com) |
| **Tradier** | US equity/option market data (delayed, intraday, historical) | 🔐 OAuth | ✅ | [Link](https://developer.tradier.com) |
| **Twelve Data** | Stock market data (real-time & historical) | 🔑 ApiKey | ✅ | [Link](https://twelvedata.com/) |
| **WallstreetBets** | WallstreetBets Stock Comments Sentiment Analysis. | No | ✅ | [Link](https://dashboard.nbshare.io/apps/reddit/api/) |
| **Yahoo Finance** | Real time low latency Yahoo Finance API for stock market, crypto currencies, ... | 🔑 ApiKey | ✅ | [Link](https://www.yahoofinanceapi.com/) |
| **YNAB** | Budgeting & Planning. | 🔐 OAuth | ✅ | [Link](https://api.youneedabudget.com/) |
| **Zoho Books** | Online accounting software, built for your business. | 🔐 OAuth | ✅ | [Link](https://www.zoho.com/books/api/v3/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="currency-exchange"></a>💱 Currency Exchange

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **1Forge** | Forex currency market data. | 🔑 ApiKey | ✅ | [Link](https://1forge.com/forex-data-api/api-documentation) |
| **Amdoren** | Free currency API with over 150 currencies. | 🔑 ApiKey | ✅ | [Link](https://www.amdoren.com/currency-api/) |
| **Bank of Canada Valet** | Free central-bank exchange/economic series API. | No | ✅ | [Link](https://www.bankofcanada.ca/valet/docs) |
| **Bank of Russia** | Exchange rates and currency conversion. | No | ✅ | [Link](https://www.cbr.ru/development/SXML/) |
| **Currency-api** | Free Currency Exchange Rates API with 150+ Currencies & No Rate Limits. | No | ✅ | [Link](https://github.com/fawazahmed0/currency-api#readme) |
| **CurrencyAPI** | Real-time currency rates and conversion. | 🔑 ApiKey | ✅ | [Link](https://currencyapi.com/) |
| **CurrencyBeacon** | Real-time and historical exchange rates. | 🔑 ApiKey | ✅ | [Link](https://currencybeacon.com/api-documentation) |
| **CurrencyConverterAPI** | Free currency converter. | 🔑 ApiKey | ✅ | [Link](https://currencyconverterapi.com/docs) |
| **CurrencyFreaks** | Exchange rates and currency conversion API. | 🔑 ApiKey | ✅ | [Link](https://currencyfreaks.com/) |
| **Currencylayer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://currencylayer.com/) |
| **CurrencyScoop** | Real-time and historical currency rates JSON API. | 🔑 ApiKey | ✅ | [Link](https://currencyscoop.com/api-documentation) |
| **Czech National Bank** | A collection of exchange rates. | No | ✅ | [Link](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.xml) |
| **ECB Data API** | Public ECB data API for exchange rates. | No | ✅ | [Link](https://data.ecb.europa.eu/help/api/data) |
| **Economia.Awesome** | Portuguese free currency prices and conversion with no rate limits. | No | ✅ | [Link](https://docs.awesomeapi.com.br/api-de-moedas) |
| **ExchangeRate-API** | Currency exchange rate conversion data. | No | ✅ | [Link](https://www.exchangerate-api.com/docs/free) |
| **Exchangerate.host** | Foreign exchange & crypto rates. | 🔑 ApiKey | ✅ | [Link](https://exchangerate.host/) |
| **Exchangeratesapi** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://exchangeratesapi.io/) |
| **Fawaz Currency API** | Free exchange-rate API (200+ currencies). | No | ✅ | [Link](https://github.com/fawazahmed0/exchange-api) |
| **Fixer** | Exchange rates and currency conversion. | 🔑 ApiKey | ✅ | [Link](https://fixer.io/) |
| **Frankfurter** | Open source exchange rates API. | No | ✅ | [Link](https://www.frankfurter.app/) |
| **FreeCurrencyAPI** | Free currency conversion API. | 🔑 ApiKey | ✅ | [Link](https://freecurrencyapi.com/docs) |
| **FreeForexAPI** | Real-time foreign exchange rates for major currency pairs. | No | ✅ | [Link](https://freeforexapi.com/Home/Api) |
| **National Bank of Poland** | Official exchange rates from NBP. | No | ✅ | [Link](https://api.nbp.pl/en.html) |
| **Open Exchange Rates** | Currency conversion and exchange rates. | 🔑 ApiKey | ✅ | [Link](https://docs.openexchangerates.org/) |
| **VATComply** | VAT rates and FX conversion data. | No | ✅ | [Link](https://www.vatcomply.com/documentation) |

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
| **Tasty** | Recipes from Tasty (via RapidAPI). | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/apidojo/api/tasty/) |
| **Ninjas Recipe** | Recipe search with nutrition data. | 🔑 ApiKey | ✅ | [Link](https://api-ninjas.com/api/recipe) |
| **Open Brewery DB** | Brewery database worldwide. | No | ✅ | [Link](https://www.openbrewerydb.org/) |
| **Punk API** | BrewDog beer recipes and data (community fork). | No | ✅ | [Link](https://punkapi-alxiw.amvera.io/v3/) |
| **Yelp Fusion** | Business and restaurant reviews. | 🔑 ApiKey | ✅ | [Link](https://docs.developer.yelp.com/) |
| **Zomato** | Restaurant search and reviews. | 🔑 ApiKey | ✅ | [Link](https://developers.zomato.com/api) |
| **BaconMockup** | Resizable bacon placeholder images. | No | ✅ | [Link](https://baconmockup.com/) |
| **Chomp** | Data about various grocery products and foods. | 🔑 ApiKey | ✅ | [Link](https://chompthis.com/api/) |
| **Edamam recipes** | Recipe Search. | 🔑 ApiKey | ✅ | [Link](https://developer.edamam.com/edamam-docs-recipe-api) |
| **Foodish** | Random pictures of food dishes. | No | ✅ | [Link](https://github.com/surhud004/Foodish#readme) |
| **Fruityvice** | Data about all kinds of fruit. | No | ✅ | [Link](https://www.fruityvice.com) |
| **Kroger** | Supermarket Data. | 🔑 ApiKey | ✅ | [Link](https://developer.kroger.com/reference) |
| **LCBO** | Alcohol. | 🔑 ApiKey | ✅ | [Link](https://lcboapi.com/) |
| **Systembolaget** | Govornment owned liqour store in Sweden. | 🔑 ApiKey | ✅ | [Link](https://api-portal.systembolaget.se) |
| **TacoFancy** | Community-driven taco database. | No | No | [Link](https://github.com/evz/tacofancy-api) |
| **The Report of the Week** | Food & Drink Reviews. | No | ✅ | [Link](https://github.com/andyklimczak/TheReportOfTheWeek-API) |
| **Untappd** | Social beer sharing. | 🔐 OAuth | ✅ | [Link](https://untappd.com/api/docs) |
| **What's on the menu?** | NYPL human-transcribed historical menu collection. | 🔑 ApiKey | No | [Link](http://nypl.github.io/menus-api/) |
| **WhiskyHunter** | Past online whisky auctions statistical data. | No | ✅ | [Link](https://whiskyhunter.net/api/) |
| **Zestful** | Parse recipe ingredients. | 🔑 ApiKey | ✅ | [Link](https://zestfuldata.com/) |

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
| **Animal Crossing: New Horizons** | API for critters, fossils, art, music, furniture and villagers. | No | ✅ | [Link](http://acnhapi.com/) |
| **Autochess VNG** | Rest Api for Autochess VNG. | No | ✅ | [Link](https://github.com/didadadida93/autochess-vng-api) |
| **Barter.VG** | Provides information about Game, DLC, Bundles, Giveaways, Trading. | No | ✅ | [Link](https://github.com/bartervg/barter.vg/wiki) |
| **Bugsnax** | Get information about Bugsnax. | No | ✅ | [Link](https://www.bugsnaxapi.com/) |
| **CheapShark** | Steam/PC Game Prices and Deals. | No | ✅ | [Link](https://www.cheapshark.com/api) |
| **Comic Vine** | Comics. | No | ✅ | [Link](https://comicvine.gamespot.com/api/documentation) |
| **Cross Universe** | Cross Universe Card Data. | No | ✅ | [Link](https://crossuniverse.psychpsyo.com/apiDocs.html) |
| **Destiny The Game** | Bungie Platform API. | 🔑 ApiKey | ✅ | [Link](https://bungie-net.github.io/multi/index.html) |
| **Digimon TCG** | Search for Digimon cards in digimoncard.io. | No | ✅ | [Link](https://documenter.getpostman.com/view/14059948/TzecB4fH) |
| **Disney** | Information of Disney characters. | No | ✅ | [Link](https://disneyapi.dev) |
| **Dungeons and Dragons (Alternate)** | Includes all monsters and spells from the SRD (System Reference Document) as ... | No | ✅ | [Link](https://open5e.com/) |
| **FFXIV Collect** | Final Fantasy XIV data on collectables. | No | ✅ | [Link](https://ffxivcollect.com/) |
| **FIFA Ultimate Team** | FIFA Ultimate Team items API. | No | ✅ | [Link](https://www.easports.com/fifa/ultimate-team/api/fut/item) |
| **FunTranslations** | Translate Text into funny languages. | No | ✅ | [Link](https://api.funtranslations.com/) |
| **GDBrowser** | Easy way to use the Geometry Dash Servers. | No | ✅ | [Link](https://gdbrowser.com/api) |
| **Geek-Jokes** | Fetch a random geeky/programming related joke for use in all sorts of applica... | No | ✅ | [Link](https://github.com/sameerkumar18/geek-joke-api) |
| **Giant Bomb** | Video Games. | 🔑 ApiKey | ✅ | [Link](https://www.giantbomb.com/api/documentation) |
| **GraphQL Pokemon** | GraphQL powered Pokemon API. Supports generations 1 through 8. | No | ✅ | [Link](https://github.com/favware/graphql-pokemon) |
| **GW2Spidy** | GW2Spidy API, Items data on the Guild Wars 2 Trade Market. | No | ✅ | [Link](https://github.com/rubensayshi/gw2spidy/wiki) |
| **Halo** | Halo 5 and Halo Wars 2 Information. | 🔑 ApiKey | ✅ | [Link](https://developer.haloapi.com/) |
| **Hearthstone** | Hearthstone Cards Information. | 🔑 ApiKey | ✅ | [Link](http://hearthstoneapi.com/) |
| **Humble Bundle** | Humble Bundle's current bundles. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/Ziggoto/api/humble-bundle) |
| **Humor** | Humor, Jokes, and Memes. | 🔑 ApiKey | ✅ | [Link](https://humorapi.com) |
| **Hytale** | Hytale blog posts and jobs. | No | ✅ | [Link](https://hytale-api.com/) |
| **Jokes One** | Joke of the day and large category of jokes accessible via REST API. | 🔑 ApiKey | ✅ | [Link](https://jokes.one/api/joke/) |
| **Jservice** | Jeopardy Question Database. | No | No | [Link](http://jservice.io) |
| **Magic The Gathering** | Magic The Gathering Game Information. | No | No | [Link](http://magicthegathering.io/) |
| **MMO Games** | MMO Games Database, News and Giveaways. | No | ✅ | [Link](https://www.mmobomb.com/api) |
| **mod.io** | Cross Platform Mod API. | 🔑 ApiKey | ✅ | [Link](https://docs.mod.io) |
| **Mojang** | Mojang / Minecraft API. | 🔑 ApiKey | ✅ | [Link](https://wiki.vg/Mojang_API) |
| **Path of Exile** | Path of Exile Game Information. | 🔐 OAuth | ✅ | [Link](https://www.pathofexile.com/developer/docs) |
| **PlayerDB** | Query Minecraft, Steam and XBox Accounts. | No | ✅ | [Link](https://playerdb.co/) |
| **PokéAPI (GraphQL)** | The Unofficial GraphQL for PokeAPI. | No | ✅ | [Link](https://github.com/mazipan/graphql-pokeapi) |
| **Pokémon TCG** | Pokémon TCG Information. | No | ✅ | [Link](https://pokemontcg.io) |
| **Psychonauts** | Psychonauts World Characters Information and PSI Powers. | No | ✅ | [Link](https://psychonauts-api.netlify.app/) |
| **Puyo Nexus** | Puyo Puyo information from Puyo Nexus Wiki. | No | ✅ | [Link](https://github.com/deltadex7/puyodb-api-deno) |
| **RPS 101** | Rock, Paper, Scissors with 101 objects. | No | ✅ | [Link](https://rps101.pythonanywhere.com/api) |
| **RuneScape** | RuneScape and OSRS RPGs information. | No | ✅ | [Link](https://runescape.wiki/w/Application_programming_interface) |
| **Sakura CardCaptor** | Sakura CardCaptor Cards Information. | No | ✅ | [Link](https://github.com/JessVel/sakura-card-captor-api) |
| **SpaceTradersAPI** | A playable inter-galactic space trading MMOAPI. | 🔐 OAuth | ✅ | [Link](https://spacetraders.io?rel=pub-apis) |
| **Steam** | Steam Web API documentation. | 🔑 ApiKey | ✅ | [Link](https://steamapi.xpaw.me/) |
| **SuperHeroes** | All SuperHeroes and Villains data from all universes under a single API. | 🔑 ApiKey | ✅ | [Link](https://superheroapi.com) |
| **Tebex** | Tebex API for information about game purchases. | 🔑 ApiKey | ✅ | [Link](https://docs.tebex.io/plugin/) |
| **TETR.IO** | TETR.IO Tetra Channel API. | No | ✅ | [Link](https://tetr.io/about/api/) |
| **Universalis** | Final Fantasy XIV market board data. | No | ✅ | [Link](https://universalis.app/docs/index.html) |
| **Warface (non-official)** | Official API proxy with better data structure and more features. | No | ✅ | [Link](https://api.wfstats.cf) |
| **Wargaming.net** | Wargaming.net info and stats. | 🔑 ApiKey | ✅ | [Link](https://developers.wargaming.net/) |
| **When is next MCU film** | Upcoming MCU film information. | No | ✅ | [Link](https://github.com/DiljotSG/MCU-Countdown/blob/develop/docs/API.md) |
| **xkcd** | Retrieve xkcd comics as JSON. | No | ✅ | [Link](https://xkcd.com/json.html) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="geocoding"></a>🌍 Geocoding

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **IP-API** | IP to location. | No | No | [Link](https://ip-api.com/docs) |
| **Mapbox** | Maps and geocoding. | 🔑 ApiKey | ✅ | [Link](https://docs.mapbox.com/) |
| **Bing Maps** | Maps, geocoding, and routing APIs. | 🔑 ApiKey | ✅ | [Link](https://www.microsoft.com/maps/) |
| **Nominatim** | OpenStreetMap Geocoding. | No | ✅ | [Link](https://nominatim.org/release-docs/latest/api/Overview/) |
| **OpenStreetMap** | Map data. | 🔐 OAuth | ✅ | [Link](http://wiki.openstreetmap.org/wiki/API) |
| **Geocodio** | Geocoding and reverse geocoding for US/Canada. | 🔑 ApiKey | ✅ | [Link](https://www.geocod.io/docs/) |
| **LocationIQ** | Geocoding and maps (free tier: 5000 req/day). | 🔑 ApiKey | ✅ | [Link](https://locationiq.com/docs) |
| **Zippopotam.us** | Postal/zip code lookup for 60+ countries (**No Auth**). | No | ✅ | [Link](https://api.zippopotam.us/) |
| **IP Geolocation** | Geolocate website visitors from their IPs. | 🔑 ApiKey | ✅ | [Link](https://www.abstractapi.com/ip-geolocation-api) |
| **Actinia Grass GIS** | Actinia is an open source REST API for geographical data that uses GRASS GIS. | 🔑 ApiKey | ✅ | [Link](https://actinia.mundialis.de/api_docs/) |
| **administrative-divisons-db** | Get all administrative divisions of a country. | No | ✅ | [Link](https://github.com/kamikazechaser/administrative-divisions-db) |
| **adresse.data.gouv.fr** | Address database of France, geocoding and reverse. | No | ✅ | [Link](https://adresse.data.gouv.fr) |
| **Airtel IP** | IP Geolocation API. Collecting data from multiple sources. | No | ✅ | [Link](https://sys.airtel.lv/ip2country/1.1.1.1/?full=true) |
| **Apiip** | Get location information by IP address. | 🔑 ApiKey | ✅ | [Link](https://apiip.net/) |
| **Battuta** | A (country/region/city) in-cascade location API. | 🔑 ApiKey | No | [Link](http://battuta.medunes.net) |
| **BigDataCloud** | Provides fast and accurate IP geolocation APIs along with security checks and... | 🔑 ApiKey | ✅ | [Link](https://www.bigdatacloud.com/ip-geolocation-apis) |
| **bng2latlong** | Convert British OSGB36 easting and northing (British National Grid) to WGS84 ... | No | ✅ | [Link](https://www.getthedata.com/bng2latlong) |
| **Cartes.io** | Create maps and markers for anything. | No | ✅ | [Link](https://github.com/M-Media-Group/Cartes.io/wiki/API) |
| **Cep.la** | Brazil RESTful API to find information about streets, zip codes, neighborhood... | No | No | [Link](http://cep.la/) |
| **CitySDK** | Open APIs for select European cities. | No | ✅ | [Link](http://www.citysdk.eu/citysdk-toolkit/) |
| **Ducks Unlimited** | API explorer that gives a query URL with a JSON response of locations and cities. | No | ✅ | [Link](https://gis.ducks.org/datasets/du-university-chapters/api) |
| **GeoApi** | French geographical data. | No | ✅ | [Link](https://api.gouv.fr/api/geoapi.html) |
| **Geoapify** | Forward and reverse geocoding, address autocomplete. | 🔑 ApiKey | ✅ | [Link](https://www.geoapify.com/api/geocoding-api/) |
| **Geocod.io** | Address geocoding / reverse geocoding in bulk. | 🔑 ApiKey | ✅ | [Link](https://www.geocod.io/) |
| **Geocode.xyz** | Provides worldwide forward/reverse geocoding, batch geocoding and geoparsing. | No | ✅ | [Link](https://geocode.xyz/api) |
| **Geocodify.com** | Worldwide geocoding, geoparsing and autocomplete for addresses. | 🔑 ApiKey | ✅ | [Link](https://geocodify.com/) |
| **Geodata.gov.gr** | Open geospatial data and API service for Greece. | No | ✅ | [Link](https://geodata.gov.gr/en/) |
| **GeoDataSource** | Geocoding of city name by using latitude and longitude coordinates. | 🔑 ApiKey | ✅ | [Link](https://www.geodatasource.com/web-service) |
| **GeoDB Cities** | Get global city, region, and country data. | 🔑 ApiKey | ✅ | [Link](http://geodb-cities-api.wirefreethought.com/) |
| **GeographQL** | A Country, State, and City GraphQL API. | No | ✅ | [Link](https://geographql.netlify.app) |
| **Geokeo** | Geokeo geocoding service- with 2500 free api requests daily. | No | ✅ | [Link](https://geokeo.com) |
| **geoPlugin** | IP geolocation and currency conversion. | No | ✅ | [Link](https://www.geoplugin.com) |
| **Google Earth Engine** | A cloud-based platform for planetary-scale environmental data analysis. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/earth-engine/) |
| **Google Maps** | Create/customize digital maps based on Google Maps data. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/maps/) |
| **Graph Countries** | Country-related data like currencies, languages, flags, regions+subregions an... | No | ✅ | [Link](https://github.com/lennertVanSever/graphcountries) |
| **HelloSalut** | Get hello translation following user language. | No | ✅ | [Link](https://fourtonfish.com/project/hellosalut-api/) |
| **Hirak IP to Country** | Ip to location with country code, currency code & currency name, fast respons... | 🔑 ApiKey | ✅ | [Link](https://iplocation.hirak.site/) |
| **IBGE** | Aggregate services of IBGE (Brazilian Institute of Geography and Statistics) | No | ✅ | [Link](https://servicodados.ibge.gov.br/api/docs/) |
| **IP 2 Country** | Map an IP to a country. | No | ✅ | [Link](https://ip2country.info) |
| **IP Address Details** | Find geolocation with ip address. | No | ✅ | [Link](https://ipinfo.io/) |
| **IP Vigilante** | Free IP Geolocation API. | No | ✅ | [Link](https://www.ipvigilante.com/) |
| **IP2Proxy** | Detect proxy and VPN using IP address. | 🔑 ApiKey | ✅ | [Link](https://www.ip2location.com/web-service/ip2proxy) |
| **ipapi.co** | Find IP address location information. | No | ✅ | [Link](https://ipapi.co/api/#introduction) |
| **ipapi.com** | Real-time Geolocation & Reverse IP Lookup REST API. | 🔑 ApiKey | ✅ | [Link](https://ipapi.com/) |
| **IPGEO** | Unlimited free IP Address API with useful information. | No | ✅ | [Link](https://api.techniknews.net/ipgeo/) |
| **IPInfoDB** | Free Geolocation tools and APIs for country, region, city and time zone looku... | 🔑 ApiKey | ✅ | [Link](https://www.ipinfodb.com/api) |
| **Kakao Maps** | Kakao Maps provide multiple APIs for Korean maps. | 🔑 ApiKey | ✅ | [Link](https://apis.map.kakao.com) |
| **keycdn IP Location Finder** | Get the IP geolocation data through the simple REST API. All the responses ar... | 🔑 ApiKey | ✅ | [Link](https://tools.keycdn.com/geo) |
| **Longdo Map** | Interactive map with detailed places and information portal in Thailand. | 🔑 ApiKey | ✅ | [Link](https://map.longdo.com/docs/) |
| **MapQuest** | To access tools and resources to map the world. | 🔑 ApiKey | ✅ | [Link](https://developer.mapquest.com/) |
| **Mexico** | Mexico RESTful zip codes API. | No | ✅ | [Link](https://github.com/IcaliaLabs/sepomex) |
| **One Map, Singapore** | Singapore Land Authority REST API services for Singapore addresses. | 🔑 ApiKey | ✅ | [Link](https://www.onemap.gov.sg/docs/) |
| **OnWater** | Determine if a lat/lon is on water or land. | No | ✅ | [Link](https://onwater.io/) |
| **Open Topo Data** | Elevation and ocean depth for a latitude and longitude. | No | ✅ | [Link](https://www.opentopodata.org) |
| **OpenCage** | Forward and reverse geocoding using open data. | 🔑 ApiKey | ✅ | [Link](https://opencagedata.com) |
| **Pinball Map** | A crowdsourced map of public pinball machines. | No | ✅ | [Link](https://pinballmap.com/api/v1/docs) |
| **Postali** | Mexico Zip Codes API. | No | ✅ | [Link](https://postali.app/api) |
| **PostcodeData.nl** | Provide geolocation data based on postcode for Dutch addresses. | No | No | [Link](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) |
| **Postcodes.io** | Postcode lookup & Geolocation for the UK. | No | ✅ | [Link](https://postcodes.io) |
| **Queimadas INPE** | Access to heat focus data (probable wildfire) | No | ✅ | [Link](https://queimadas.dgi.inpe.br/queimadas/dados-abertos/) |
| **RoadGoat Cities** | Cities content & photos API. | 🔑 ApiKey | ✅ | [Link](https://www.roadgoat.com/business/cities-api) |
| **Rwanda Locations** | Rwanda Provences, Districts, Cities, Capital City, Sector, cells, villages an... | No | ✅ | [Link](https://rapidapi.com/victorkarangwa4/api/rwanda) |
| **SLF** | German city, country, river, database. | No | ✅ | [Link](https://github.com/slftool/slftool.github.io/blob/master/API.md) |
| **SpotSense** | Add location based interactions to your mobile app. | 🔑 ApiKey | ✅ | [Link](https://spotsense.io/) |
| **Telize** | Telize offers location information from any IP address. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/fcambus/api/telize/) |
| **TomTom** | Maps, Directions, Places and Traffic APIs. | 🔑 ApiKey | ✅ | [Link](https://developer.tomtom.com/) |
| **Uebermaps** | Discover and share maps with friends. | 🔑 ApiKey | ✅ | [Link](https://uebermaps.com/api/v2) |
| **US ZipCode** | Validate and append data for any US ZipCode. | 🔑 ApiKey | ✅ | [Link](https://www.smarty.com/docs/cloud/us-zipcode-api) |
| **Utah AGRC** | Utah Web API for geocoding Utah addresses. | 🔑 ApiKey | ✅ | [Link](https://api.mapserv.utah.gov) |
| **ViaCep** | Brazil RESTful zip codes API. | No | ✅ | [Link](https://viacep.com.br) |
| **What3Words** | Three words as rememberable and unique coordinates worldwide. | 🔑 ApiKey | ✅ | [Link](https://what3words.com) |
| **Yandex.Maps Geocoder** | Use geocoding to get an object's coordinates from its address. | 🔑 ApiKey | ✅ | [Link](https://yandex.com/dev/maps/geocoder) |
| **ZipCodeAPI** | US zip code distance, radius and location API. | 🔑 ApiKey | ✅ | [Link](https://www.zipcodeapi.com) |
| **Ziptastic** | Get the country, state, and city of any US zip-code. | No | ✅ | [Link](https://ziptasticapi.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="health"></a>❤️ Health

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BMI Calculator** | Calculate BMI and other metrics. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/navii/api/bmi-calculator/) |
| **Edamam Nutrition** | Nutrition analysis. | 🔑 ApiKey | ✅ | [Link](https://developer.edamam.com/edamam-nutrition-api) |
| **Nutritionix** | Nutrition database. | 🔑 ApiKey | ✅ | [Link](https://developer.nutritionix.com/) |
| **OpenFDA** | Public FDA data about drugs, devices, and foods. | No | ✅ | [Link](https://open.fda.gov/apis/) |
| **Disease.sh** | COVID-19 and disease statistics (**No Auth**). | No | ✅ | [Link](https://disease.sh/) |
| **ClinicalTrials.gov** | Clinical trials database (**No Auth**). | No | ✅ | [Link](https://clinicaltrials.gov/data-api/api) |
| **ExerciseDB** | Exercise data with images and animations. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb) |
| **WHO GHO** | World Health Organization health data (**No Auth**). | No | ✅ | [Link](https://www.who.int/data/gho/info/gho-odata-api) |
| **WGER** | Open source workout manager API. | No | ✅ | [Link](https://wger.de/en/software/api) |
| **PubChem** | Chemical compound data. | No | ✅ | [Link](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) |
| **RxNav** | Drug vocabularies and interaction data. | No | ✅ | [Link](https://lhncbc.nlm.nih.gov/RxNav/APIs/index.html) |
| **NPI Registry** | US healthcare provider registry search. | No | ✅ | [Link](https://clinicaltables.nlm.nih.gov/apidoc/npi_org/v3/doc.html) |
| **CMS.gov** | Access to the data from the CMS - medicare.gov. | 🔑 ApiKey | ✅ | [Link](https://data.cms.gov/provider-data/) |
| **Coronavirus** | HTTP API for Latest Covid-19 Data. | No | ✅ | [Link](https://pipedream.com/@pravin/http-api-for-latest-wuhan-coronavirus-data-2019-ncov-p_G6CLVM/readme) |
| **Coronavirus in the UK** | UK Government coronavirus data, including deaths and cases by region. | No | ✅ | [Link](https://coronavirus.data.gov.uk/details/developers-guide) |
| **Covid Tracking Project** | Covid-19  data for the US. | No | ✅ | [Link](https://covidtracking.com/data/api/version-2) |
| **Covid-19** | Covid 19 spread, infection and recovery. | No | ✅ | [Link](https://covid19api.com/) |
| **Covid-19 Datenhub** | Maps, datasets, applications and more in the context of COVID-19. | No | ✅ | [Link](https://npgeo-corona-npgeo-de.hub.arcgis.com) |
| **Covid-19 Government Response** | Government measures tracker to fight against the Covid-19 pandemic. | No | ✅ | [Link](https://covidtracker.bsg.ox.ac.uk) |
| **Covid-19 India** | Covid 19 statistics state and district wise about cases, vaccinations, recove... | No | ✅ | [Link](https://data.covid19india.org/) |
| **Covid-19 JHU CSSE** | Open-source API for exploring Covid19 cases based on JHU CSSE. | No | ✅ | [Link](https://nuttaphat.com/covid19-api/) |
| **Covid-19 Live Data** | Global and countrywise data of Covid 19 daily Summary, confirmed cases, recov... | No | ✅ | [Link](https://github.com/mathdroid/covid-19-api) |
| **Covid-19 Philippines** | Unofficial Covid-19 Web API for Philippines from data collected by DOH. | No | ✅ | [Link](https://github.com/Simperfy/Covid-19-API-Philippines-DOH) |
| **COVID-19 Tracker Canada** | Details on Covid-19 cases across Canada. | No | ✅ | [Link](https://api.covid19tracker.ca/docs/1.0/overview) |
| **COVID-ID** | Indonesian government Covid data per province. | No | ✅ | [Link](https://data.covid19.go.id/public/api/prov.json) |
| **Dataflow Kit COVID-19** | COVID-19 live statistics into sites per hour. | No | ✅ | [Link](https://covid-19.dataflowkit.com) |
| **FoodData Central** | National Nutrient Database for Standard Reference. | 🔑 ApiKey | ✅ | [Link](https://fdc.nal.usda.gov/) |
| **Healthcare.gov** | Educational content about the US Health Insurance Marketplace. | No | ✅ | [Link](https://www.healthcare.gov/developers/) |
| **Humanitarian Data Exchange** | Humanitarian Data Exchange (HDX) is open platform for sharing data across cri... | No | ✅ | [Link](https://data.humdata.org/) |
| **Infermedica** | NLP based symptom checker and patient triage API for health diagnosis from text. | 🔑 ApiKey | ✅ | [Link](https://developer.infermedica.com/docs/) |
| **LAPIS** | SARS-CoV-2 genomic sequences from public sources. | No | ✅ | [Link](https://cov-spectrum.ethz.ch/public) |
| **Lexigram** | NLP that extracts mentions of clinical concepts from text, gives access to cl... | 🔑 ApiKey | ✅ | [Link](https://docs.lexigram.io/) |
| **MyVaccination** | Vaccination data for Malaysia. | No | ✅ | [Link](https://documenter.getpostman.com/view/16605343/Tzm8GG7u) |
| **NPPES** | National Plan & Provider Enumeration System, info on healthcare providers reg... | No | ✅ | [Link](https://npiregistry.cms.hhs.gov/registry/help-api) |
| **Open Data NHS Scotland** | Medical reference data and statistics by Public Health Scotland. | No | ✅ | [Link](https://www.opendata.nhs.scot) |
| **Orion Health** | Medical platform which allows the development of applications for different h... | 🔐 OAuth | ✅ | [Link](https://developer.orionhealth.io/) |
| **Quarantine** | Coronavirus API with free COVID-19 live updates. | No | ✅ | [Link](https://quarantine.country/coronavirus/api/) |

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
| **Tavily** | AI-powered search API for agents. | 🔑 ApiKey | ✅ | [Link](https://tavily.com/) |
| **ElevenLabs** | AI voice generation and text-to-speech. | 🔑 ApiKey | ✅ | [Link](https://elevenlabs.io/docs/api-reference) |
| **AI For Thai** | Free Various Thai AI API. | 🔑 ApiKey | ✅ | [Link](https://aiforthai.in.th/index.php) |
| **Deepcode** | AI for code review. | No | ✅ | [Link](https://www.deepcode.ai) |
| **EXUDE-API** | Used for the primary ways for filtering the stopping, stemming words from the... | No | ✅ | [Link](http://uttesh.com/exude-api/) |
| **Hirak FaceAPI** | Face detection, face recognition with age estimation/gender estimation, accur... | 🔑 ApiKey | ✅ | [Link](https://faceapi.hirak.site/) |
| **Inferdo** | Computer Vision services like Facial detection, Image labeling, NSFW classifi... | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/user/inferdo) |
| **IPS Online** | Face and License Plate Anonymization. | 🔑 ApiKey | ✅ | [Link](https://docs.identity.ps/docs) |
| **Irisnet** | Realtime content moderation API that blocks or blurs unwanted images in real-... | 🔑 ApiKey | ✅ | [Link](https://irisnet.de/api/) |
| **Keen IO** | Data Analytics. | 🔑 ApiKey | ✅ | [Link](https://keen.io/) |
| **MessengerX.io** | A FREE API for developers to build and monetize personalized ML based chat apps. | 🔑 ApiKey | ✅ | [Link](https://messengerx.rtfd.io) |
| **OpenVisionAPI** | Open source computer vision API based on open source models. | No | ✅ | [Link](https://openvisionapi.com) |
| **Perspective** | NLP API to return probability that if text is toxic, obscene, insulting or th... | 🔑 ApiKey | ✅ | [Link](https://perspectiveapi.com) |
| **SkyBiometry** | Face Detection, Face Recognition and Face Grouping. | 🔑 ApiKey | ✅ | [Link](https://skybiometry.com/documentation/) |
| **Time Door** | A time series analysis API. | 🔑 ApiKey | ✅ | [Link](https://timedoor.io) |
| **Unplugg** | Forecasting API for timeseries data. | 🔑 ApiKey | ✅ | [Link](https://unplu.gg/test_api.html) |

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
| **Bacon Ipsum** | A Meatier Lorem Ipsum Generator. | No | ✅ | [Link](https://baconipsum.com/json-api/) |
| **FakeJSON** | Service to generate test and fake data. | 🔑 ApiKey | ✅ | [Link](https://fakejson.com) |
| **GeneradorDNI** | Data generator API. Profiles, vehicles, banks and cards, etc. | 🔑 ApiKey | ✅ | [Link](https://api.generadordni.es) |
| **ItsThisForThat** | Generate Random startup ideas. | No | ✅ | [Link](https://itsthisforthat.com/api.php) |
| **Loripsum** | The "lorem ipsum" generator that doesn't suck. | No | No | [Link](http://loripsum.net/) |
| **Mailsac** | Disposable Email. | 🔑 ApiKey | ✅ | [Link](https://mailsac.com/docs/api) |
| **Metaphorsum** | Generate demo paragraphs giving number of words and sentences. | No | No | [Link](http://metaphorpsum.com/) |
| **QuickMocker** | API mocking tool to generate contextual, fake or random data. | No | ✅ | [Link](https://quickmocker.com) |
| **Random Data** | Random data generator. | No | ✅ | [Link](https://random-data-api.com) |
| **Randommer** | Random data generator. | 🔑 ApiKey | ✅ | [Link](https://randommer.io/randommer-api) |
| **This Person Does not Exist** | Generates real-life faces of people who do not exist. | No | ✅ | [Link](https://thispersondoesnotexist.com) |
| **Toolcarton** | Generate random testimonial data. | No | ✅ | [Link](https://testimonialapi.toolcarton.com/) |
| **What The Commit** | Random commit message generator. | No | No | [Link](http://whatthecommit.com/index.txt) |
| **Yes No** | Generate yes or no randomly. | No | ✅ | [Link](https://yesno.wtf/api) |

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
| **Jamendo** | Free music licensing and streaming. | 🔐 OAuth | ✅ | [Link](https://developer.jamendo.com/v3.0) |
| **Setlist.fm** | Concert setlist data. | 🔑 ApiKey | ✅ | [Link](https://api.setlist.fm/docs/1.0/index.html) |
| **7digital** | Api of Music store 7digital. | 🔐 OAuth | ✅ | [Link](https://docs.7digital.com/reference) |
| **AI Mastering** | Automated Music Mastering. | 🔑 ApiKey | ✅ | [Link](https://aimastering.com/api_docs/) |
| **Bandcamp** | API of Music store Bandcamp. | 🔐 OAuth | ✅ | [Link](https://bandcamp.com/developer) |
| **Bandsintown** | Music Events. | No | ✅ | [Link](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0) |
| **Freesound** | Music Samples. | 🔑 ApiKey | ✅ | [Link](https://freesound.org/docs/api/) |
| **Gaana** | API to retrieve song information from Gaana. | No | ✅ | [Link](https://github.com/cyberboysumanjay/GaanaAPI) |
| **Genrenator** | Music genre generator. | No | ✅ | [Link](https://binaryjazz.us/genrenator-api/) |
| **JioSaavn** | API to retrieve song information, album meta data and many more from JioSaavn. | No | ✅ | [Link](https://github.com/cyberboysumanjay/JioSaavnAPI) |
| **KKBOX** | Get music libraries, playlists, charts, and perform out of KKBOX's platform. | 🔐 OAuth | ✅ | [Link](https://developer.kkbox.com) |
| **KSoft.Si Lyrics** | API to get lyrics for songs. | 🔑 ApiKey | ✅ | [Link](https://docs.ksoft.si/api/lyrics-api) |
| **Napster** | Music. | 🔑 ApiKey | ✅ | [Link](https://developer.napster.com/api/v2.2) |
| **Openwhyd** | Download curated playlists of streaming tracks (YouTube, SoundCloud, etc...) | No | ✅ | [Link](https://openwhyd.github.io/openwhyd/API) |
| **Phishin** | A web-based archive of legal live audio recordings of the improvisational roc... | 🔑 ApiKey | ✅ | [Link](https://phish.in/api-docs) |
| **Songkick** | Music Events. | 🔑 ApiKey | ✅ | [Link](https://www.songkick.com/developer/) |
| **Songlink / Odesli** | Get all the services on which a song is available. | 🔑 ApiKey | ✅ | [Link](https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741) |
| **Songsterr** | Provides guitar, bass and drums tabs and chords. | No | ✅ | [Link](https://www.songsterr.com/a/wa/api/) |
| **TasteDive** | Similar artist API (also works for movies and TV shows) | 🔑 ApiKey | ✅ | [Link](https://tastedive.com/read/api) |
| **Vagalume** | Crowdsourced lyrics and music knowledge. | 🔑 ApiKey | ✅ | [Link](https://api.vagalume.com.br/docs/) |

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

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="photography"></a>📷 Photography

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Art Institute of Chicago** | Museum artwork data (**No Auth**). | No | ✅ | [Link](https://api.artic.edu/docs/) |
| **Giphy** | GIFs. | 🔑 ApiKey | ✅ | [Link](https://developers.giphy.com/docs/) |
| **Met Museum** | Metropolitan Museum of Art collection (**No Auth**). | No | ✅ | [Link](https://metmuseum.github.io/) |
| **Pexels** | Free stock photos. | 🔑 ApiKey | ✅ | [Link](https://www.pexels.com/api/) |
| **Picsum Photos** | The Lorem Ipsum for photos. | No | ✅ | [Link](https://picsum.photos/) |
| **Pixabay** | Free stock photos and videos. | 🔑 ApiKey | ✅ | [Link](https://pixabay.com/api/docs/) |
| **Flickr** | Photo sharing and management. | 🔑 ApiKey | ✅ | [Link](https://www.flickr.com/services/api/) |
| **NASA Image Library** | NASA's image and video library (**No Auth**). | No | ✅ | [Link](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf) |
| **Unsplash** | High-quality photos. | 🔐 OAuth | ✅ | [Link](https://unsplash.com/developers) |
| **Imgix** | Real-time image processing and optimization. | 🔑 ApiKey | ✅ | [Link](https://docs.imgix.com/) |
| **Remove.bg** | AI background removal from images. | 🔑 ApiKey | ✅ | [Link](https://www.remove.bg/api) |
| **Placeholder** | Custom placeholder images (**No Auth**). | No | ✅ | [Link](https://placeholder.com/) |
| **apilayer mediastack** | Free, Simple REST API for Live News & Blog Articles. | 🔑 ApiKey | ✅ | [Link](https://mediastack.com/) |
| **Associated Press** | Search for news and metadata from Associated Press. | 🔑 ApiKey | ✅ | [Link](https://developer.ap.org/) |
| **Chronicling America** | Provides access to millions of pages of historic US newspapers from the Libra... | No | No | [Link](http://chroniclingamerica.loc.gov/about/api/) |
| **Feedbin** | RSS reader. | 🔐 OAuth | ✅ | [Link](https://github.com/feedbin/feedbin-api) |
| **Graphs for Coronavirus** | Each Country separately and Worldwide Graphs for Coronavirus. Daily updates. | No | ✅ | [Link](https://corona.dnsforfamily.com/api.txt) |
| **Inshorts News** | Provides news from inshorts. | No | ✅ | [Link](https://github.com/cyberboysumanjay/Inshorts-News-API) |
| **MarketAux** | Live stock market news with tagged tickers + sentiment and stats JSON API. | 🔑 ApiKey | ✅ | [Link](https://www.marketaux.com/) |
| **New York Times** | The New York Times Developer Network. | 🔑 ApiKey | ✅ | [Link](https://developer.nytimes.com/) |
| **NewsData** | News data API for live-breaking news and headlines from reputed  news sources. | 🔑 ApiKey | ✅ | [Link](https://newsdata.io/docs) |
| **NewsX** | Get or Search Latest Breaking News with ML Powered Summaries 🤖. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/machaao-inc-machaao-inc-default/api/newsx/) |
| **NPR One** | Personalized news listening experience from NPR. | 🔐 OAuth | ✅ | [Link](http://dev.npr.org/api/) |
| **Spaceflight News** | Spaceflight related news 🚀. | No | ✅ | [Link](https://spaceflightnewsapi.net) |
| **The Old Reader** | RSS reader. | 🔑 ApiKey | ✅ | [Link](https://github.com/theoldreader/api) |
| **Trove** | Search through the National Library of Australia collection of 1000s of digit... | 🔑 ApiKey | ✅ | [Link](https://trove.nla.gov.au/about/create-something/using-api) |
| **APITemplate.io** | Dynamically generate images and PDFs from templates with a simple API. | 🔑 ApiKey | ✅ | [Link](https://apitemplate.io) |
| **Bruzu** | Image generation with query string. | 🔑 ApiKey | ✅ | [Link](https://docs.bruzu.com) |
| **CheetahO** | Photo optimization and resize. | 🔑 ApiKey | ✅ | [Link](https://cheetaho.com/docs/getting-started/) |
| **Dagpi** | Image manipulation and processing. | 🔑 ApiKey | ✅ | [Link](https://dagpi.xyz) |
| **DynaPictures** | Generate Hundreds of Personalized Images in Minutes. | 🔑 ApiKey | ✅ | [Link](https://dynapictures.com/docs/) |
| **Getty Images** | Build applications using the world's most powerful imagery. | 🔐 OAuth | ✅ | [Link](http://developers.gettyimages.com/en/) |
| **Google Photos** | Integrate Google Photos with your apps or devices. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/photos) |
| **Image Upload** | Image Optimization. | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/image_upload-api) |
| **Imgur** | Images. | 🔐 OAuth | ✅ | [Link](https://apidocs.imgur.com/) |
| **ObjectCut** | Image Background removal. | 🔑 ApiKey | ✅ | [Link](https://objectcut.com/) |
| **PhotoRoom** | Remove background from images. | 🔑 ApiKey | ✅ | [Link](https://www.photoroom.com/api/) |
| **PlaceKeanu** | Resizable Keanu Reeves placeholder images with grayscale and young Keanu options. | No | ✅ | [Link](https://placekeanu.com/) |
| **Readme typing SVG** | Customizable typing and deleting text SVG. | No | ✅ | [Link](https://github.com/DenverCoder1/readme-typing-svg) |
| **ReSmush.it** | Photo optimization. | No | No | [Link](https://resmush.it/api) |
| **shutterstock** | Stock Photos and Videos. | 🔐 OAuth | ✅ | [Link](https://api-reference.shutterstock.com/) |
| **Sirv** | Image management solutions like optimization, manipulation, hosting. | 🔑 ApiKey | ✅ | [Link](https://apidocs.sirv.com/) |
| **Wallhaven** | Wallpapers. | 🔑 ApiKey | ✅ | [Link](https://wallhaven.cc/help/api) |
| **Webdam** | Images. | 🔐 OAuth | ✅ | [Link](https://www.damsuccess.com/hc/en-us/articles/202134055-REST-API) |

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
| **Astronomy API** | Astronomy calculations and celestial data. | 🔑 ApiKey | ✅ | [Link](https://astronomyapi.com/) |
| **GBIF** | Global biodiversity occurrence data (**No Auth**). | No | ✅ | [Link](https://www.gbif.org/developer/summary) |
| **arcsecond.io** | Multiple astronomy data sources. | No | ✅ | [Link](https://api.arcsecond.io/) |
| **CORE** | Access the world's Open Access research papers. | 🔑 ApiKey | ✅ | [Link](https://core.ac.uk/services#api) |
| **iDigBio** | Access millions of museum specimens from organizations around the world. | No | ✅ | [Link](https://github.com/idigbio/idigbio-search-api/wiki) |
| **inspirehep.net** | High Energy Physics info. system. | No | ✅ | [Link](https://github.com/inspirehep/rest-api-doc) |
| **isEven (humor)** | Check if a number is even. | No | ✅ | [Link](https://isevenapi.xyz/) |
| **ISRO** | ISRO Space Crafts Information. | No | ✅ | [Link](https://isro.vercel.app) |
| **ITIS** | Integrated Taxonomic Information System. | No | ✅ | [Link](https://www.itis.gov/ws_description.html) |
| **Materials Platform for Data Science** | Curated experimental data for materials science. | 🔑 ApiKey | ✅ | [Link](https://mpds.io) |
| **Minor Planet Center** | Asterank.com Information. | No | No | [Link](http://www.asterank.com/mpc) |
| **NASA ADS** | NASA Astrophysics Data System. | 🔐 OAuth | ✅ | [Link](https://ui.adsabs.harvard.edu/help/api/api-docs.html) |
| **Noctua** | REST API used to access NoctuaSky features. | No | ✅ | [Link](https://api.noctuasky.com/api/v1/swaggerdoc/) |
| **Numbers** | Number of the day, random number, number facts and anything else you want to ... | 🔑 ApiKey | ✅ | [Link](https://math.tools/api/numbers/) |
| **Open Notify** | ISS astronauts, current location, etc. | No | No | [Link](http://open-notify.org/Open-Notify-API/) |
| **Purple Air** | Real Time Air Quality Monitoring. | No | ✅ | [Link](https://www2.purpleair.com/) |
| **Remote Calc** | Decodes base64 encoding and parses it to return a solution to the calculation... | No | ✅ | [Link](https://github.com/elizabethadegbaju/remotecalc) |
| **SHARE** | A free, open, dataset about research and scholarly activities. | No | ✅ | [Link](https://share.osf.io/api/v2/) |
| **Times Adder** | With this API you can add each of the times introduced in the array sended. | No | ✅ | [Link](https://github.com/FranP-code/API-Times-Adder) |
| **TLE** | Satellite information. | No | ✅ | [Link](https://tle.ivanstanojevic.me/#/docs) |
| **USGS Water Services** | Water quality and level info for rivers and lakes. | No | ✅ | [Link](https://waterservices.usgs.gov/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="security-validation"></a>🔐 Security & Validation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **HaveIBeenPwned** | Check if email or password has been compromised in a data breach. | 🔑 ApiKey | ✅ | [Link](https://haveibeenpwned.com/API/v3) |
| **Google reCAPTCHA** | Bot protection and CAPTCHA service. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/recaptcha) |
| **Cloudflare Turnstile** | Privacy-first CAPTCHA alternative. | 🔑 ApiKey | ✅ | [Link](https://developers.cloudflare.com/turnstile/) |
| **Shodan** | Internet-connected devices search engine. | 🔑 ApiKey | ✅ | [Link](https://developer.shodan.io/) |
| **Mozilla Observatory** | Website security analysis (**No Auth**). | No | ✅ | [Link](https://observatory.mozilla.org/) |
| **MSRC** | Microsoft vulnerability and CVRF data feeds. | No | ✅ | [Link](https://msrc.microsoft.com/report/developer) |
| **SSL Labs** | SSL/TLS server testing (**No Auth**). | No | ✅ | [Link](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md) |
| **SecurityTrails** | Domain and DNS intelligence. | 🔑 ApiKey | ✅ | [Link](https://securitytrails.com/corp/api) |
| **CertSpotter** | Certificate transparency monitoring. | No | ✅ | [Link](https://sslmate.com/certspotter/api/) |
| **FullHunt** | Attack surface discovery and monitoring. | 🔑 ApiKey | ✅ | [Link](https://api-docs.fullhunt.io/) |
| **Application Environment Verification** | Android library and API to verify the safety of user devices, detect rooted d... | 🔑 ApiKey | ✅ | [Link](https://github.com/fingerprintjs/aev) |
| **BinaryEdge** | Provide access to BinaryEdge 40fy scanning platform. | 🔑 ApiKey | ✅ | [Link](https://docs.binaryedge.io/api-v2.html) |
| **BitWarden** | Best open-source password manager. | 🔐 OAuth | ✅ | [Link](https://bitwarden.com/help/api/) |
| **Botd** | Botd is a browser library for JavaScript bot detection. | 🔑 ApiKey | ✅ | [Link](https://github.com/fingerprintjs/botd) |
| **Bugcrowd** | Bugcrowd API for interacting and tracking the reported issues programmatically. | 🔑 ApiKey | ✅ | [Link](https://docs.bugcrowd.com/api/getting-started/) |
| **Censys** | Search engine for Internet connected host and devices. | 🔑 ApiKey | ✅ | [Link](https://search.censys.io/api) |
| **Complete Criminal Checks** | Provides data of offenders from all U.S. States and Pureto Rico. | 🔑 ApiKey | ✅ | [Link](https://completecriminalchecks.com/Developers) |
| **CRXcavator** | Chrome extension risk scoring. | 🔑 ApiKey | ✅ | [Link](https://crxcavator.io/apidocs) |
| **EmailRep** | Email address threat and risk prediction. | No | ✅ | [Link](https://docs.emailrep.io/) |
| **Escape** | An API for escaping different kind of queries. | No | ✅ | [Link](https://github.com/polarspetroll/EscapeAPI) |
| **FilterLists** | Lists of filters for adblockers and firewalls. | No | ✅ | [Link](https://filterlists.com) |
| **FingerprintJS Pro** | Fraud detection API offering highly accurate browser fingerprinting. | 🔑 ApiKey | ✅ | [Link](https://dev.fingerprintjs.com/docs) |
| **FraudLabs Pro** | Screen order information using AI to detect frauds. | 🔑 ApiKey | ✅ | [Link](https://www.fraudlabspro.com/developer/api/screen-order) |
| **GreyNoise** | Query IPs in the GreyNoise dataset and retrieve a subset of the full IP conte... | 🔑 ApiKey | ✅ | [Link](https://docs.greynoise.io/reference/get_v3-community-ip) |
| **HackerOne** | The industry’s first hacker API that helps increase productivity towards crea... | 🔑 ApiKey | ✅ | [Link](https://api.hackerone.com/) |
| **Hashable** | A REST API to access high level cryptographic functions and methods. | No | ✅ | [Link](https://hashable.space/pages/api/) |
| **Intelligence X** | Perform OSINT via Intelligence X. | 🔑 ApiKey | ✅ | [Link](https://github.com/IntelligenceX/SDK/blob/master/Intelligence%20X%20API.pdf) |
| **LoginRadius** | Managed User Authentication Service. | 🔑 ApiKey | ✅ | [Link](https://www.loginradius.com/docs/) |
| **Mozilla http scanner** | Mozilla observatory http scanner. | No | ✅ | [Link](https://github.com/mozilla/http-observatory/blob/master/httpobs/docs/api.md) |
| **Mozilla tls scanner** | Mozilla observatory tls scanner. | No | ✅ | [Link](https://github.com/mozilla/tls-observatory#api-endpoints) |
| **National Vulnerability Database** | U.S. National Vulnerability Database. | No | ✅ | [Link](https://nvd.nist.gov/vuln/Data-Feeds/JSON-feed-changelog) |
| **Passwordinator** | Generate random passwords of varying complexities. | No | ✅ | [Link](https://github.com/fawazsullia/password-generator/) |
| **PhishStats** | Phishing database. | No | ✅ | [Link](https://phishstats.info/) |
| **Privacy.com** | Generate merchant-specific and one-time use credit card numbers that link bac... | 🔑 ApiKey | ✅ | [Link](https://privacy.com/developer/docs) |
| **Pulsedive** | Scan, search and collect threat intelligence data in real-time. | 🔑 ApiKey | ✅ | [Link](https://pulsedive.com/api/) |
| **Spyse** | Access data on all Internet assets and build powerful attack surface manageme... | 🔑 ApiKey | ✅ | [Link](https://spyse-dev.readme.io/reference/quick-start) |
| **Threat Jammer** | Risk scoring service from curated threat intelligence data. | 🔑 ApiKey | ✅ | [Link](https://threatjammer.com/docs/index) |
| **UK Police** | UK Police data. | No | ✅ | [Link](https://data.police.uk/docs/) |
| **Virushee** | Virushee file/data scanning. | No | ✅ | [Link](https://api.virushee.com/) |
| **VulDB** | VulDB API allows to initiate queries for one or more items along with transac... | 🔑 ApiKey | ✅ | [Link](https://vuldb.com/?doc.api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="data-validation"></a>✅ Data Validation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Byteplant Email Validator** | Email validation API. | 🔑 ApiKey | ✅ | [Link](https://www.email-validator.net/api.html) |
| **DeBounce** | Email validation API with free credits. | 🔑 ApiKey | ✅ | [Link](https://developers.debounce.com/) |
| **Emailable** | Email verification API with free tier. | 🔑 ApiKey | ✅ | [Link](https://emailable.com/docs/api) |
| **Lob.com** | US Address Verification. | 🔑 ApiKey | ✅ | [Link](https://lob.com/) |
| **Neutrino Email Validate** | Email syntax/DNS/disposable checks. | 🔑 ApiKey | ✅ | [Link](https://www.neutrinoapi.com/api/email-validate/) |
| **US Autocomplete** | Enter address data quickly with real-time address suggestions. | 🔑 ApiKey | ✅ | [Link](https://www.smarty.com/docs/cloud/us-autocomplete-pro-api) |
| **US Extract** | Extract postal addresses from any text including emails. | 🔑 ApiKey | ✅ | [Link](https://www.smarty.com/products/apis/us-extract-api) |
| **US Street Address** | Validate and append data for any US postal address. | 🔑 ApiKey | ✅ | [Link](https://www.smarty.com/docs/cloud/us-street-api) |
| **vatlayer** | VAT number validation. | 🔑 ApiKey | ✅ | [Link](https://vatlayer.com/documentation) |
| **Verifalia** | Email verification API. | 🔑 ApiKey | ✅ | [Link](https://verifalia.com/developers) |
| **ZeroBounce** | Email validation and scoring. | 🔑 ApiKey | ✅ | [Link](https://www.zerobounce.net/docs/email-validation-api-quickstart/v2-get-api-usage/) |

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
| **Barcode Lookup** | Product data from UPC/EAN barcodes. | 🔑 ApiKey | ✅ | [Link](https://www.barcodelookup.com/api) |
| **Digi-Key** | Retrieve price and inventory of electronic components as well as place orders. | 🔐 OAuth | ✅ | [Link](https://www.digikey.com/en/resources/api-solutions) |
| **Flipkart Marketplace** | Product listing management, Order Fulfilment in the Flipkart Marketplace. | 🔐 OAuth | ✅ | [Link](https://seller.flipkart.com/api-docs/FMSAPI.html) |
| **Lazada** | Retrieve product ratings and seller performance metrics. | 🔑 ApiKey | ✅ | [Link](https://open.lazada.com/doc/doc.htm) |
| **Octopart** | Electronic part data for manufacturing, design, and sourcing. | 🔑 ApiKey | ✅ | [Link](https://octopart.com/api/v4/reference) |
| **OLX Poland** | Integrate with local sites by posting, managing adverts and communicating wit... | 🔑 ApiKey | ✅ | [Link](https://developer.olx.pl/api/doc#section/) |
| **Rappi** | Manage orders from Rappi's app. | 🔐 OAuth | ✅ | [Link](https://dev-portal.rappi.com/) |
| **Tokopedia** | Tokopedia's Official API for integration of various services from Tokopedia. | 🔐 OAuth | ✅ | [Link](https://developer.tokopedia.com/openapi/guide/#/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="utilities-tools"></a>🔧 Utilities & Tools

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **DiceBear Avatars** | Generate random SVG avatars (**No Auth**). | No | ✅ | [Link](https://www.dicebear.com/) |
| **FakerAPI** | Generate fake data for testing (**No Auth, 1000 req/day**). | No | ✅ | [Link](https://fakerapi.it/en) |
| **ipify** | A simple public IP address API (**No Auth**). | No | ✅ | [Link](https://www.ipify.org/) |
| **Pravatar** | Placeholder avatar images (**No Auth**). | No | ✅ | [Link](https://pravatar.cc/) |
| **QR Code Generator** | Dynamic QR code generation API. | No | ✅ | [Link](https://goqr.me/api/) |
| **RoboHash** | Generate unique robot/monster avatars (**No Auth**). | No | ✅ | [Link](https://robohash.org/) |
| **UI Avatars** | Generate avatar placeholders from initials (**No Auth, 28M+ daily requests**). | No | ✅ | [Link](https://ui-avatars.com/) |
| **URLBox** | Website screenshot API. | 🔑 ApiKey | ✅ | [Link](https://www.urlbox.io/) |
| **DuckDuckGo Instant Answer** | Quick, concise answers for definitions, calculations, and conversions. | No | ✅ | [Link](https://duckduckgo.com/api) |
| **Country.is** | Get country from IP address (**No Auth**). | No | ✅ | [Link](https://country.is/) |
| **Text Art API** | Generate text-based art (**No Auth**). | No | ✅ | [Link](http://patorjk.com/software/taag/) |
| **JSONLint** | JSON validation API. | No | ✅ | [Link](https://jsonlint.com/) |
| **Carbon Screenshot** | Create beautiful images of code snippets. | No | ✅ | [Link](https://carbon.now.sh/) |
| **PDF.co** | PDF generation, conversion and manipulation. | 🔑 ApiKey | ✅ | [Link](https://apidocs.pdf.co/) |
| **Cal.com** | Open source scheduling API (Calendly alternative). | 🔑 ApiKey | ✅ | [Link](https://cal.com/docs/api-reference) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="url-shorteners"></a>🔗 URL Shorteners

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **1pt** | A simple URL shortener. | No | ✅ | [Link](https://github.com/1pt-co/api/blob/main/README.md) |
| **Bitly** | URL shortener and link management. | 🔐 OAuth | ✅ | [Link](http://dev.bitly.com/get_started.html) |
| **BL.INK** | URL shortener and branded link management. | 🔑 ApiKey | ✅ | [Link](https://bl.ink/developers) |
| **CleanURI** | URL shortener service. | No | ✅ | [Link](https://cleanuri.com/docs) |
| **ClickMeter** | Monitor, compare and optimize your marketing links. | 🔑 ApiKey | ✅ | [Link](https://support.clickmeter.com/hc/en-us/categories/201474986) |
| **Clico** | URL shortener service. | 🔑 ApiKey | ✅ | [Link](https://cli.com/swagger-ui/index.html?configUrl=/v3/api-docs/swagger-config) |
| **Cutt.ly** | URL shortener service. | 🔑 ApiKey | ✅ | [Link](https://cutt.ly/api-documentation/cuttly-links-api) |
| **Drivet URL Shortener** | Shorten a long URL easily and fast. | No | ✅ | [Link](https://wiki.drivet.xyz/en/url-shortener/add-links) |
| **Dub** | Open-source short links and analytics. | 🔑 ApiKey | ✅ | [Link](https://dub.co/docs/api-reference/introduction) |
| **Free Url Shortener** | Free URL Shortener offers a powerful API to interact with other sites. | No | ✅ | [Link](https://ulvis.net/developer.html) |
| **Git.io** | Git.io URL shortener. | No | ✅ | [Link](https://github.blog/2011-11-10-git-io-github-url-shortener/) |
| **GoTiny** | A lightweight URL shortener, focused on ease-of-use for the developer and end... | No | ✅ | [Link](https://github.com/robvanbakel/gotiny-api) |
| **is.gd** | Simple free URL shortening API. | No | ✅ | [Link](https://is.gd/apishorteningreference.php) |
| **Kutt** | Free Modern URL Shortener. | 🔑 ApiKey | ✅ | [Link](https://docs.kutt.it/) |
| **Mgnet.me** | Torrent URL shorten API. | No | ✅ | [Link](http://mgnet.me/api.html) |
| **Polr** | Open-source URL shortener API. | No | ✅ | [Link](https://docs.polrproject.org/en/latest/developer-guide/api/) |
| **Rebrandly** | URL shortener API. | 🔑 ApiKey | ✅ | [Link](https://developers.rebrandly.com/docs) |
| **Shlink** | Self-hosted URL shortener with REST API. | 🔑 ApiKey | ✅ | [Link](https://shlink.io/documentation/api-docs/) |
| **Short.io** | URL shortener with analytics. | 🔑 ApiKey | ✅ | [Link](https://developers.short.io/) |
| **Shrtcode** | URl Shortener with multiple Domains. | No | ✅ | [Link](https://shrtco.de/docs) |
| **Tiny.cc** | Link shortening and management API. | 🔑 ApiKey | ✅ | [Link](https://tiny.cc/api-docs) |
| **TinyURL** | URL shortener API (**No Auth**). | No | ✅ | [Link](https://tinyurl.com/app/dev) |
| **UrlBae** | Simple and efficient short link creation. | 🔑 ApiKey | ✅ | [Link](https://urlbae.com/developers) |
| **v.gd** | Free URL shortener API service. | No | ✅ | [Link](https://v.gd/apishorteningreference.php) |
| **YOURLS** | Self-hosted shortener with extensible API. | 🔑 ApiKey | ✅ | [Link](https://yourls.org/#API) |

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
| **4chan** | Simple image-based bulletin board dedicated to a variety of topics. | No | ✅ | [Link](https://github.com/4chan/4chan-API) |
| **Ayrshare** | Social media APIs to post, get analytics, and manage multiple users social me... | 🔑 ApiKey | ✅ | [Link](https://www.ayrshare.com) |
| **aztro** | Daily horoscope info for yesterday, today, and tomorrow. | No | ✅ | [Link](https://aztro.sameerkumar.website/) |
| **Blogger** | The Blogger APIs allows client applications to view and update Blogger content. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/blogger/) |
| **Cisco Spark** | Team Collaboration Software. | 🔐 OAuth | ✅ | [Link](https://developer.ciscospark.com) |
| **Dangerous Discord Database** | Database of malicious Discord accounts. | 🔑 ApiKey | ✅ | [Link](https://discord.riverside.rocks/docs/index.php) |
| **Disqus** | Communicate with Disqus data. | 🔐 OAuth | ✅ | [Link](https://disqus.com/api/docs/auth/) |
| **Doge-Meme** | Top meme posts from r/dogecoin which include 'Meme' flair. | No | ✅ | [Link](https://api.doge-meme.lol/docs) |
| **Foursquare** | Interact with Foursquare users and places (geolocation-based checkins, photos... | 🔐 OAuth | ✅ | [Link](https://developer.foursquare.com/) |
| **Fuck Off as a Service** | Asks someone to fuck off. | No | ✅ | [Link](https://www.foaas.com) |
| **Full Contact** | Get Social Media profiles and contact Information. | 🔐 OAuth | ✅ | [Link](https://docs.fullcontact.com/) |
| **Hashnode** | A blogging platform built for developers. | No | ✅ | [Link](https://hashnode.com) |
| **Kakao** | Kakao Login, Share on KakaoTalk, Social Plugins and more. | 🔐 OAuth | ✅ | [Link](https://developers.kakao.com/) |
| **Lanyard** | Retrieve your presence on Discord through an HTTP REST API or WebSocket. | No | ✅ | [Link](https://github.com/Phineas/lanyard) |
| **Meetup.com** | Data about Meetups from Meetup.com. | 🔑 ApiKey | ✅ | [Link](https://www.meetup.com/api/guide) |
| **Microsoft Graph** | Access the data and intelligence in Microsoft 365, Windows 10, and Enterprise... | 🔐 OAuth | ✅ | [Link](https://docs.microsoft.com/en-us/graph/api/overview) |
| **NAVER** | NAVER Login, Share on NAVER, Social Plugins and more. | 🔐 OAuth | ✅ | [Link](https://developers.naver.com/main/) |
| **Open Collective** | Get Open Collective data. | No | ✅ | [Link](https://docs.opencollective.com/help/developers/api) |
| **Product Hunt** | The best new products in tech. | 🔐 OAuth | ✅ | [Link](https://api.producthunt.com/v2/docs) |
| **TamTam** | Bot API to interact with TamTam. | 🔑 ApiKey | ✅ | [Link](https://dev.tamtam.chat/) |
| **Telegram MTProto** | Read and write Telegram data. | 🔐 OAuth | ✅ | [Link](https://core.telegram.org/api#getting-started) |
| **Telegraph** | Create attractive blogs easily, to share. | 🔑 ApiKey | ✅ | [Link](https://telegra.ph/api) |
| **Trash Nothing** | A freecycling community with thousands of free items posted every day. | 🔐 OAuth | ✅ | [Link](https://trashnothing.com/developer) |
| **vk** | Read and write vk data. | 🔐 OAuth | ✅ | [Link](https://vk.com/dev/sites) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="sports"></a>⚽ Sports

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **TheSportsDB** | Open crowd-sourced sports data and artwork. | 🔑 ApiKey | ✅ | [Link](https://www.thesportsdb.com/api.php) |
| **API-Football** | Football (soccer) live scores, fixtures, stats. | 🔑 ApiKey | ✅ | [Link](https://www.api-football.com/documentation-v3) |
| **Football-Data.org** | Football data and statistics (**Free tier**). | 🔑 ApiKey | ✅ | [Link](https://www.football-data.org/documentation/quickstart) |
| **NBA API** | NBA stats and scores (**No Auth**). | No | ✅ | [Link](https://github.com/swar/nba_api) |
| **ESPN** | Sports scores and news. | No | ✅ | [Link](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b) |
| **OpenF1** | Real-time Formula 1 race data (**No Auth**). | No | ✅ | [Link](https://openf1.org/) |
| **API-Sports** | Multi-sport live data (free tier). | 🔑 ApiKey | ✅ | [Link](https://api-sports.io/) |
| **CricketData** | Live cricket scores and statistics. | 🔑 ApiKey | ✅ | [Link](https://cricketdata.org/) |
| **PandaScore** | Esports data and statistics. | 🔑 ApiKey | ✅ | [Link](https://developers.pandascore.co/) |
| **NHL API** | NHL hockey statistics and schedules. | No | ✅ | [Link](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md) |
| **Football Prediction** | Football match predictions. | 🔑 ApiKey | ✅ | [Link](https://boggio-analytics.com/fp-api/) |
| **SofaScore** | Live sports scores and stats. | No | ✅ | [Link](https://api.sofascore.com/) |
| **ApiMedic** | ApiMedic offers a medical symptom checker API primarily for patients. | 🔑 ApiKey | ✅ | [Link](https://apimedic.com/) |
| **Canadian Football League (CFL)** | Official JSON API providing real-time league, team and player statistics abou... | 🔑 ApiKey | ✅ | [Link](http://api.cfl.ca/) |
| **Cloudbet** | Official Cloudbet API provides real-time sports odds and betting API to place... | 🔑 ApiKey | ✅ | [Link](https://www.cloudbet.com/api/) |
| **CollegeFootballData.com** | Unofficial detailed American college football statistics, records, and result... | 🔑 ApiKey | ✅ | [Link](https://collegefootballdata.com) |
| **Ergast F1** | F1 data from the beginning of the world championships in 1950. | No | ✅ | [Link](http://ergast.com/mrd/) |
| **Fitbit** | Fitbit Information. | 🔐 OAuth | ✅ | [Link](https://dev.fitbit.com/) |
| **Football** | A simple Open Source Football API to get squads’ stats, best scorers and more. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/GiulianoCrescimbeni/api/football98/) |
| **Football (Soccer) Videos** | Embed codes for goals and highlights from Premier League, Bundesliga, Serie A... | No | ✅ | [Link](https://www.scorebat.com/video-api/) |
| **Football Standings** | Display football standings e.g epl, la liga, serie a etc. The data is based o... | No | ✅ | [Link](https://github.com/azharimm/football-standings-api) |
| **Football-Data** | Football data with matches info, players, teams, and competitions. | 🔑 ApiKey | ✅ | [Link](https://www.football-data.org) |
| **JCDecaux Bike** | JCDecaux's self-service bicycles. | 🔑 ApiKey | ✅ | [Link](https://developer.jcdecaux.com/) |
| **NBA Data** | All NBA Stats DATA, Games, Livescore, Standings, Statistics. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/api-sports/api/api-nba/) |
| **NBA Stats** | Current and historical NBA Statistics. | No | ✅ | [Link](https://any-api.com/nba_com/nba_com/docs/API_Description) |
| **NHL Records and Stats** | NHL historical data and statistics. | No | ✅ | [Link](https://gitlab.com/dword4/nhlapi) |
| **Oddsmagnet** | Odds history from multiple UK bookmakers. | No | ✅ | [Link](https://data.oddsmagnet.com) |
| **OpenLigaDB** | Crowd sourced sports league results. | No | ✅ | [Link](https://www.openligadb.de) |
| **Premier League Standings** | All Current Premier League Standings and Statistics. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/heisenbug/api/premier-league-live-scores/) |
| **Sport List & Data** | List of and resources related to sports. | No | ✅ | [Link](https://developers.decathlon.com/products/sports) |
| **Sport Places** | Crowd-source sports places around the world. | No | ✅ | [Link](https://developers.decathlon.com/products/sport-places) |
| **Sport Vision** | Identify sport, brands and gear in an image. Also does image sports captioning. | 🔑 ApiKey | ✅ | [Link](https://developers.decathlon.com/products/sport-vision) |
| **Sportmonks Football** | Football score/schedule, news api, tv channels, stats, history, display stand... | 🔑 ApiKey | ✅ | [Link](https://docs.sportmonks.com/football/) |
| **Squiggle** | Fixtures, results and predictions for Australian Football League matches. | No | ✅ | [Link](https://api.squiggle.com.au) |
| **Strava** | Connect with athletes, activities and more. | 🔐 OAuth | ✅ | [Link](https://strava.github.io/api/) |
| **SuredBits** | Query sports data, including teams, players, games, scores and statistics. | No | No | [Link](https://suredbits.com/api/) |
| **Tredict** | Get and set activities, health data and more. | 🔐 OAuth | ✅ | [Link](https://www.tredict.com/blog/oauth_docs/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="design-colors"></a>🎨 Design & Colors

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Colormind** | AI-powered color palette generator (**No Auth**). | No | ✅ | [Link](http://colormind.io/api-access/) |
| **Placeholder.com** | Simple placeholder image service (**No Auth**). | No | ✅ | [Link](https://placehold.co/) |
| **The Color API** | Color conversion, schemes, and naming (**No Auth**). | No | ✅ | [Link](https://www.thecolorapi.com/) |
| **Dribbble** | Design community and portfolio. | 🔐 OAuth | ✅ | [Link](https://developer.dribbble.com/) |
| **Behance** | Creative work showcase. | 🔑 ApiKey | ✅ | [Link](https://www.behance.net/dev) |
| **Icon Horse** | Favicon grabber API. | No | ✅ | [Link](https://icon.horse/) |
| **Logo.dev** | Company logos and brand asset API. | 🔑 ApiKey | ✅ | [Link](https://www.logo.dev/) |
| **LogoKit** | Brand, stock, and crypto logo API. | 🔑 ApiKey | ✅ | [Link](https://docs.logokit.com/) |
| **Brandfetch** | Company logos and brand assets. | 🔑 ApiKey | ✅ | [Link](https://docs.brandfetch.com/) |
| **SVG Repo** | Free SVG icons and vectors. | No | ✅ | [Link](https://www.svgrepo.com/) |
| **Font Awesome** | Icon library and toolkit APIs. | 🔑 ApiKey | ✅ | [Link](https://fontawesome.com/docs/apis) |
| **Améthyste** | Generate images for Discord users. | 🔑 ApiKey | ✅ | [Link](https://api.amethyste.moe/) |
| **ColourLovers** | Get various patterns, palettes and images. | No | No | [Link](http://www.colourlovers.com/api) |
| **Cooper Hewitt** | Smithsonian Design Museum. | 🔑 ApiKey | ✅ | [Link](https://collection.cooperhewitt.org/api) |
| **EmojiHub** | Get emojis by categories and groups. | No | ✅ | [Link](https://github.com/cheatsnake/emojihub) |
| **Europeana** | European Museum and Galleries content. | 🔑 ApiKey | ✅ | [Link](https://pro.europeana.eu/resources/apis/search) |
| **Harvard Art Museums** | Art. | 🔑 ApiKey | No | [Link](https://github.com/harvardartmuseums/api-docs) |
| **Iconfinder** | Icons. | 🔑 ApiKey | ✅ | [Link](https://developer.iconfinder.com) |
| **Icons8** | Icons (find "search icon" hyperlink in page) | No | ✅ | [Link](https://img.icons8.com/) |
| **Lordicon** | Icons with predone Animations. | No | ✅ | [Link](https://lordicon.com/) |
| **Noun Project** | Icons. | 🔐 OAuth | No | [Link](http://api.thenounproject.com/index.html) |
| **PHP-Noise** | Noise Background Image Generator. | No | ✅ | [Link](https://php-noise.com/) |
| **Pixel Encounter** | SVG Icon Generator. | No | ✅ | [Link](https://pixelencounter.com/api) |
| **Word Cloud** | Easily create word clouds. | 🔑 ApiKey | ✅ | [Link](https://wordcloudapi.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="geography-countries"></a>🌎 Geography & Countries

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **REST Countries** | Comprehensive country data (flags, capitals, currencies) (**No Auth**). | No | ✅ | [Link](https://restcountries.com/) |
| **Country State City** | Countries, states, and cities database. | 🔑 ApiKey | ✅ | [Link](https://countrystatecity.in/) |
| **GeoNames** | Worldwide geographical database (free registration). | No | ✅ | [Link](https://www.geonames.org/export/web-services.html) |
| **Flagpedia** | Country flags in SVG and PNG (**No Auth**). | No | ✅ | [Link](https://flagpedia.net/download/api) |
| **World Time API** | Current time by timezone (**No Auth**). | No | ✅ | [Link](https://worldtimeapi.org/) |
| **GeoJS** | IP geolocation and geo data (**No Auth**). | No | ✅ | [Link](https://www.geojs.io/) |
| **CountryLayer** | Country data including flags and borders. | 🔑 ApiKey | ✅ | [Link](https://countrylayer.com/) |
| **Open Elevation** | Elevation data for any coordinates. | No | ✅ | [Link](https://open-elevation.com/) |
| **IPGeolocation Timezone** | Timezone data by coordinates. | 🔑 ApiKey | ✅ | [Link](https://ipgeolocation.io/timezone-api.html) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="transportation"></a>🚆 Transportation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **BART** | Bay Area Rapid Transit. | 🔑 ApiKey | ✅ | [Link](http://api.bart.gov) |
| **OpenSky Network** | Flight tracking. | No | ✅ | [Link](https://openskynetwork.github.io/opensky-api/) |
| **Transport for London** | Public transport data. | 🔑 ApiKey | ✅ | [Link](https://api.tfl.gov.uk) |
| **OpenRouteService** | Directions, geocoding, isochrones. | 🔑 ApiKey | ✅ | [Link](https://openrouteservice.org/) |
| **Transitland** | Global transit data aggregator (**No Auth**). | No | ✅ | [Link](https://www.transit.land/documentation) |
| **HERE Maps** | Mapping, routing, and traffic (free tier). | 🔑 ApiKey | ✅ | [Link](https://developer.here.com/) |
| **GraphHopper** | Route planning and optimization. | 🔑 ApiKey | ✅ | [Link](https://docs.graphhopper.com/) |
| **Citybikes** | Bike sharing station data worldwide. | No | ✅ | [Link](https://api.citybik.es/v2/) |
| **ADS-B Exchange** | Flight tracking data. | No | ✅ | [Link](https://www.adsbexchange.com/data/) |
| **GTFS Realtime** | Public transit real-time data standard. | No | ✅ | [Link](https://gtfs.org/) |
| **MBTA v3** | Boston transit routes and predictions. | No | ✅ | [Link](https://api-v3.mbta.com/) |
| **MTA** | NYC subway real-time feed APIs. | No | ✅ | [Link](https://api.mta.info/#/subwayRealTimeFeeds) |
| **airportsapi** | Get name and website-URL for airports by ICAO code. | No | ✅ | [Link](https://airport-web.appspot.com/api/docs/) |
| **AIS Hub** | Real-time data of any marine and inland vessel equipped with AIS tracking system. | 🔑 ApiKey | No | [Link](http://www.aishub.net/api) |
| **Amadeus for Developers** | Travel Search - Limited usage. | 🔐 OAuth | ✅ | [Link](https://developers.amadeus.com/self-service) |
| **AviationAPI** | FAA Aeronautical Charts and Publications, Airport Information, and Airport We... | No | ✅ | [Link](https://docs.aviationapi.com) |
| **AZ511** | Access traffic data from the ADOT API. | 🔑 ApiKey | ✅ | [Link](https://www.az511.com/developers/doc) |
| **BC Ferries** | Sailing times and capacities for BC Ferries. | No | ✅ | [Link](https://www.bcferriesapi.ca) |
| **BIC-Boxtech** | Container technical detail for the global container fleet. | 🔐 OAuth | ✅ | [Link](https://docs.bic-boxtech.org/) |
| **Boston MBTA Transit** | Stations and predicted arrivals for MBTA. | 🔑 ApiKey | ✅ | [Link](https://www.mbta.com/developers/v3-api) |
| **Community Transit** | Transitland API. | No | ✅ | [Link](https://github.com/transitland/transitland-datastore/blob/master/README.md#api-endpoints) |
| **Compare Flight Prices** | API for comparing flight prices across platforms. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/obryan-software-obryan-software-default/api/compare-flight-prices/) |
| **CTS** | CTS Realtime API. | 🔑 ApiKey | ✅ | [Link](https://api.cts-strasbourg.eu/) |
| **Grab** | Track deliveries, ride fares, payments and loyalty points. | 🔐 OAuth | ✅ | [Link](https://developer.grab.com/docs/) |
| **Icelandic APIs** | Open APIs that deliver services in or regarding Iceland. | No | ✅ | [Link](http://docs.apis.is/) |
| **Impala Hotel Bookings** | Hotel content, rates and room bookings. | 🔑 ApiKey | ✅ | [Link](https://docs.impala.travel/docs/booking-api/) |
| **Izi** | Audio guide for travellers. | 🔑 ApiKey | ✅ | [Link](http://api-docs.izi.travel/) |
| **Land Transport Authority DataMall, Singapore** | Singapore transport information. | 🔑 ApiKey | No | [Link](https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf) |
| **Metro Lisboa** | Delays in subway lines. | No | No | [Link](http://app.metrolisboa.pt/status/getLinhas.php) |
| **Navitia** | The open API for building cool stuff with transport data. | 🔑 ApiKey | ✅ | [Link](https://doc.navitia.io/) |
| **Open Charge Map** | Global public registry of electric vehicle charging locations. | 🔑 ApiKey | ✅ | [Link](https://openchargemap.org/site/develop/api) |
| **Railway Transport for France** | SNCF public API. | 🔑 ApiKey | ✅ | [Link](https://www.digital.sncf.com/startup/api) |
| **REFUGE Restrooms** | Provides safe restroom access for transgender, intersex and gender nonconform... | No | ✅ | [Link](https://www.refugerestrooms.org/api/docs/#!/restrooms) |
| **Sabre for Developers** | Travel Search - Limited usage. | 🔑 ApiKey | ✅ | [Link](https://developer.sabre.com/guides/travel-agency/quickstart/getting-started-in-travel) |
| **Schiphol Airport** | Schiphol. | 🔑 ApiKey | ✅ | [Link](https://developer.schiphol.nl/) |
| **Tankerkoenig** | German realtime gas/diesel prices. | 🔑 ApiKey | ✅ | [Link](https://creativecommons.tankerkoenig.de/swagger/) |
| **Transport for Atlanta, US** | Marta. | No | No | [Link](http://www.itsmarta.com/app-developer-resources.aspx) |
| **Transport for Auckland, New Zealand** | Auckland Transport. | No | ✅ | [Link](https://dev-portal.at.govt.nz/) |
| **Transport for Belgium** | The iRail API is a third-party API for Belgian public transport by train. | No | ✅ | [Link](https://docs.irail.be/) |
| **Transport for Berlin, Germany** | Third-party VBB API. | No | ✅ | [Link](https://github.com/derhuerst/vbb-rest/blob/3/docs/index.md) |
| **Transport for Bordeaux, France** | Bordeaux Métropole public transport and more (France) | 🔑 ApiKey | ✅ | [Link](https://opendata.bordeaux-metropole.fr/explore/) |
| **Transport for Budapest, Hungary** | Budapest public transport API. | No | ✅ | [Link](https://bkkfutar.docs.apiary.io) |
| **Transport for Chicago, US** | Chicago Transit Authority (CTA) | 🔑 ApiKey | No | [Link](http://www.transitchicago.com/developers/) |
| **Transport for Czech Republic** | Czech transport API. | No | ✅ | [Link](https://www.chaps.cz/eng/products/idos-internet) |
| **Transport for Finland** | Finnish transport API. | No | ✅ | [Link](https://digitransit.fi/en/developers/) |
| **Transport for Grenoble, France** | Grenoble public transport. | No | No | [Link](https://www.mobilites-m.fr/pages/opendata/OpenDataApi.html) |
| **Transport for Hessen, Germany** | RMV API (Public Transport in Hessen) | No | ✅ | [Link](https://opendata.rmv.de/site/start.html) |
| **Transport for Honolulu, US** | Honolulu Transportation Information. | 🔑 ApiKey | No | [Link](http://hea.thebus.org/api_info.asp) |
| **Transport for Lisbon, Portugal** | Data about buses routes, parking and traffic. | 🔑 ApiKey | ✅ | [Link](https://emel.city-platform.com/opendata/) |
| **Transport for Los Angeles, US** | Data about positions of Metro vehicles in real time and travel their routes. | No | ✅ | [Link](https://developer.metro.net/api/) |
| **Transport for Manchester, England** | TfGM transport network data. | 🔑 ApiKey | ✅ | [Link](https://developer.tfgm.com/) |
| **Transport for Norway** | Transport APIs and dataset for Norway. | No | ✅ | [Link](https://developer.entur.org/) |
| **Transport for Ottawa, Canada** | OC Transpo API. | 🔑 ApiKey | ✅ | [Link](https://www.octranspo.com/en/plan-your-trip/travel-tools/developers) |
| **Transport for Paris, France** | RATP Open Data API. | No | No | [Link](http://data.ratp.fr/api/v1/console/datasets/1.0/search/) |
| **Transport for Philadelphia, US** | SEPTA APIs. | No | No | [Link](http://www3.septa.org/hackathon/) |
| **Transport for Sao Paulo, Brazil** | SPTrans. | 🔐 OAuth | No | [Link](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) |
| **Transport for Spain** | Public trains of Spain. | No | ✅ | [Link](https://data.renfe.com/api/1/util/snippet/api_info.html?resource_id=a2368cff-1562-4dde-8466-9635ea3a572a) |
| **Transport for Sweden** | Public Transport consumer. | 🔐 OAuth | ✅ | [Link](https://www.trafiklab.se/api) |
| **Transport for Switzerland** | Official Swiss Public Transport Open Data. | 🔑 ApiKey | ✅ | [Link](https://opentransportdata.swiss/en/) |
| **Transport for The Netherlands** | NS, only trains. | 🔑 ApiKey | No | [Link](http://www.ns.nl/reisinformatie/ns-api) |
| **Transport for Toronto, Canada** | TTC. | No | ✅ | [Link](https://myttc.ca/developers) |
| **Transport for UK** | Transport API and dataset for UK. | 🔑 ApiKey | ✅ | [Link](https://developer.transportapi.com) |
| **Transport for United States** | NextBus API. | No | No | [Link](https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf) |
| **Transport for Vancouver, Canada** | TransLink. | 🔐 OAuth | ✅ | [Link](https://developer.translink.ca/) |
| **Transport for Washington, US** | Washington Metro transport API. | 🔐 OAuth | ✅ | [Link](https://developer.wmata.com/) |
| **transport.rest** | Community maintained, developer-friendly public transport API. | No | ✅ | [Link](https://transport.rest) |
| **Tripadvisor** | Rating content for a hotel, restaurant, attraction or destination. | 🔑 ApiKey | ✅ | [Link](https://developer-tripadvisor.com/home/) |
| **Uber** | Uber ride requests and price estimation. | 🔐 OAuth | ✅ | [Link](https://developer.uber.com/products) |
| **Velib metropolis, Paris, France** | Velib Open Data API. | No | ✅ | [Link](https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole) |
| **Brazilian Vehicles and Prices** | Vehicles information from Fundação Instituto de Pesquisas Econômicas - Fipe. | No | ✅ | [Link](https://deividfortuna.github.io/fipe/) |
| **Helipaddy sites** | Helicopter and passenger drone landing site directory, Helipaddy data and muc... | 🔑 ApiKey | ✅ | [Link](https://helipaddy.com/api/) |
| **Kelley Blue Book** | Vehicle info, pricing, configuration, plus much more. | 🔑 ApiKey | ✅ | [Link](http://developer.kbb.com/#!/data/1-Default) |
| **Mercedes-Benz** | Telematics data, remotely access vehicle functions, car configurator, locate ... | 🔑 ApiKey | ✅ | [Link](https://developer.mercedes-benz.com/apis) |
| **NHTSA** | NHTSA Product Information Catalog and Vehicle Listing. | No | ✅ | [Link](https://vpic.nhtsa.dot.gov/api/) |
| **Smartcar** | Lock and unlock vehicles and get data like odometer reading and location. Wor... | 🔐 OAuth | ✅ | [Link](https://smartcar.com/docs/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="tracking-logistics"></a>📦 Tracking & Logistics

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **17TRACK** | Shipment tracking API with free quota. | 🔑 ApiKey | ✅ | [Link](https://asset.17track.net/api/document/v2_en/index.html) |
| **Aftership** | API to update, manage and track shipment efficiently. | 🔑 ApiKey | ✅ | [Link](https://developers.aftership.com/reference/quick-start) |
| **Correios** | Integration to provide information and prepare shipments using Correio's serv... | 🔑 ApiKey | ✅ | [Link](https://cws.correios.com.br/ajuda) |
| **DHL Shipment Tracking** | DHL package tracking API. | 🔑 ApiKey | ✅ | [Link](https://developer.dhl.com/api-reference/shipment-tracking) |
| **FedEx Tracking** | FedEx package tracking API. | 🔑 ApiKey | ✅ | [Link](https://developer.fedex.com/api/en-us/catalog/track.html) |
| **Pixela** | API for recording and tracking habits or effort, routines. | 🔑 ApiKey | ✅ | [Link](https://pixe.la) |
| **PostalPinCode** | API for getting Pincode details in India. | No | ✅ | [Link](http://www.postalpincode.in/Api-Details) |
| **Postmon** | An API to query Brazilian ZIP codes and orders easily, quickly and free. | No | No | [Link](http://postmon.com.br) |
| **PostNord** | Provides information about parcels in transport for Sweden and Denmark. | 🔑 ApiKey | No | [Link](https://developer.postnord.com/api) |
| **Shippo** | Shipping API with free test mode. | 🔑 ApiKey | ✅ | [Link](https://docs.goshippo.com/) |
| **UPS** | Shipment and Address information. | 🔑 ApiKey | ✅ | [Link](https://www.ups.com/upsdeveloperkit) |
| **USPS Track & Confirm** | USPS tracking API. | 🔑 ApiKey | ✅ | [Link](https://www.usps.com/business/web-tools-apis/track-and-confirm-api.htm) |
| **WeCanTrack** | Automatically place subids in affiliate links to attribute affiliate conversi... | 🔑 ApiKey | ✅ | [Link](https://docs.wecantrack.com) |
| **WhatPulse** | Small application that measures your keyboard/mouse usage. | No | ✅ | [Link](https://developer.whatpulse.org/#web-api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="environment-climate"></a>🌿 Environment & Climate

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Carbon Interface** | CO2 emissions for flights, shipping, and energy. | 🔑 ApiKey | ✅ | [Link](https://docs.carboninterface.com/) |
| **Global Forest Watch** | Deforestation and forest monitoring data. | 🔑 ApiKey | ✅ | [Link](https://www.globalforestwatch.org/help/developers/) |
| **OpenWeatherMap Air Pollution** | Air quality index and pollutant data. | 🔑 ApiKey | ✅ | [Link](https://openweathermap.org/api/air-pollution) |
| **WaterQuality (EPA)** | US water quality monitoring data. | No | ✅ | [Link](https://www.waterqualitydata.us/) |
| **PurpleAir** | Real-time air quality sensor data. | 🔑 ApiKey | ✅ | [Link](https://api.purpleair.com/) |
| **AQICN** | World air quality index data. | No | ✅ | [Link](https://aqicn.org/api/) |
| **Climatiq** | Carbon footprint calculations API. | 🔑 ApiKey | ✅ | [Link](https://www.climatiq.io/docs) |
| **NOAA Climate Data Online** | Historical climate and weather data. | 🔑 ApiKey | ✅ | [Link](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) |
| **BreezoMeter Pollen** | Daily Forecast pollen conditions data for a specific location. | 🔑 ApiKey | ✅ | [Link](https://docs.breezometer.com/api-documentation/pollen-api/v2/) |
| **CO2 Offset** | API calculates and validates the carbon footprint. | No | ✅ | [Link](https://co2offset.io/api.html) |
| **Danish data service Energi** | Open energy data from Energinet to society. | No | ✅ | [Link](https://www.energidataservice.dk/) |
| **GrünstromIndex** | Green Power Index for Germany (Grünstromindex/GSI) | No | No | [Link](https://gruenstromindex.de/) |
| **IQAir** | Air quality and weather data. | 🔑 ApiKey | ✅ | [Link](https://www.iqair.com/air-pollution-data-api) |
| **Luchtmeetnet** | Predicted and actual air quality components for The Netherlands (RIVM) | No | ✅ | [Link](https://api-docs.luchtmeetnet.nl/) |
| **National Grid ESO** | Open data from Great Britain’s Electricity System Operator. | No | ✅ | [Link](https://data.nationalgrideso.com/) |
| **PM2.5 Open Data Portal** | Open low-cost PM2.5 sensor data. | No | ✅ | [Link](https://pm25.lass-net.org/#apis) |
| **PM25.in** | Air quality of China. | 🔑 ApiKey | No | [Link](http://www.pm25.in/api_doc) |
| **PVWatts** | Energy production photovoltaic (PV) energy systems. | 🔑 ApiKey | ✅ | [Link](https://developer.nrel.gov/docs/solar/pvwatts/v6/) |
| **Srp Energy** | Hourly usage energy report for Srp customers. | 🔑 ApiKey | ✅ | [Link](https://srpenergy-api-client-python.readthedocs.io/en/latest/api.html) |
| **UK Carbon Intensity** | The Official Carbon Intensity API for Great Britain developed by National Grid. | No | ✅ | [Link](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v1-0-0) |
| **Website Carbon** | API to estimate the carbon footprint of loading web pages. | No | ✅ | [Link](https://api.websitecarbon.com/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="government-civic"></a>🏛️ Government & Civic

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Google Civic Information** | US voting and representative information. | 🔑 ApiKey | ✅ | [Link](https://developers.google.com/civic-information) |
| **OpenFEC** | US Federal Election Commission data. | No | ✅ | [Link](https://api.open.fec.gov/developers/) |
| **Congress.gov** | US legislation and congressional records. | No | ✅ | [Link](https://api.congress.gov/) |
| **Open States** | US state legislature data. | 🔑 ApiKey | ✅ | [Link](https://docs.openstates.org/) |
| **UK Parliament** | UK parliamentary data and members. | No | ✅ | [Link](https://members-api.parliament.uk/index.html) |
| **data.europa.eu** | EU open data portal API. | No | ✅ | [Link](https://data.europa.eu/en) |
| **Federal Register** | US federal rules and notices data. | No | ✅ | [Link](https://www.federalregister.gov/developers/documentation/api/v1) |
| **OpenSecrets** | US political finance transparency data. | 🔑 ApiKey | ✅ | [Link](https://www.opensecrets.org/open-data/api) |
| **USASpending** | US federal spending data API. | No | ✅ | [Link](https://api.usaspending.gov/) |
| **Bank Negara Malaysia Open Data** | Malaysia Central Bank Open Data. | No | ✅ | [Link](https://apikijangportal.bnm.gov.my/) |
| **BCLaws** | Access to the laws of British Columbia. | No | No | [Link](https://www.bclaws.gov.bc.ca/civix/template/complete/api/index.html) |
| **Brazil** | Community driven API for Brazil Public Data. | No | ✅ | [Link](https://brasilapi.com.br/) |
| **Brazil Central Bank Open Data** | Brazil Central Bank Open Data. | No | ✅ | [Link](https://dadosabertos.bcb.gov.br/) |
| **Brazil Receita WS** | Consult companies by CNPJ for Brazilian companies. | No | ✅ | [Link](https://www.receitaws.com.br/) |
| **Brazilian Chamber of Deputies Open Data** | Provides legislative information in Apis XML and JSON, as well as files in va... | No | ✅ | [Link](https://dadosabertos.camara.leg.br/swagger/api.html) |
| **City, Berlin** | Berlin(DE) City Open Data. | No | ✅ | [Link](https://daten.berlin.de/) |
| **City, Gdańsk** | Gdańsk (PL) City Open Data. | No | ✅ | [Link](https://ckan.multimediagdansk.pl/en) |
| **City, Gdynia** | Gdynia (PL) City Open Data. | No | No | [Link](http://otwartedane.gdynia.pl/en/api_doc.html) |
| **City, Helsinki** | Helsinki(FI) City Open Data. | No | ✅ | [Link](https://hri.fi/en_gb/) |
| **City, Lviv** | Lviv(UA) City Open Data. | No | ✅ | [Link](https://opendata.city-adm.lviv.ua/) |
| **City, Nantes Open Data** | Nantes(FR) City Open Data. | 🔑 ApiKey | ✅ | [Link](https://data.nantesmetropole.fr/pages/home/) |
| **City, New York Open Data** | New York (US) City Open Data. | No | ✅ | [Link](https://opendata.cityofnewyork.us/) |
| **City, Toronto Open Data** | Toronto (CA) City Open Data. | No | ✅ | [Link](https://open.toronto.ca/) |
| **Code.gov** | The primary platform for Open Source and code sharing for the U.S. Federal Go... | 🔑 ApiKey | ✅ | [Link](https://code.gov) |
| **Colorado Information Marketplace** | Colorado State Government Open Data. | No | ✅ | [Link](https://data.colorado.gov/) |
| **Data USA** | US Public Data. | No | ✅ | [Link](https://datausa.io/about/api/) |
| **Data.parliament.uk** | Contains live datasets including information about petitions, bills, MP votes... | No | No | [Link](https://explore.data.parliament.uk/?learnmore=Members) |
| **Deutscher Bundestag DIP** | This API provides read access to DIP entities (e.g. activities, persons, prin... | 🔑 ApiKey | ✅ | [Link](https://dip.bundestag.de/documents/informationsblatt_zur_dip_api_v01.pdf) |
| **District of Columbia Open Data** | Contains D.C. government public datasets, including crime, GIS, financial dat... | No | ✅ | [Link](http://opendata.dc.gov/pages/using-apis) |
| **EPA** | Web services and data sets from the US Environmental Protection Agency. | No | ✅ | [Link](https://www.epa.gov/developers/data-data-products#apis) |
| **FBI Wanted** | Access information on the FBI Wanted program. | No | ✅ | [Link](https://www.fbi.gov/wanted/api) |
| **Gazette Data, UK** | UK official public record API. | 🔐 OAuth | ✅ | [Link](https://www.thegazette.co.uk/data) |
| **Gun Policy** | International firearm injury prevention and policy. | 🔑 ApiKey | ✅ | [Link](https://www.gunpolicy.org/api) |
| **INEI** | Peruvian Statistical Government Open Data. | No | No | [Link](http://iinei.inei.gob.pe/microdatos/) |
| **Interpol Red Notices** | Access and search Interpol Red Notices. | No | ✅ | [Link](https://interpol.api.bund.dev/) |
| **Istanbul (İBB) Open Data** | Data sets from the İstanbul Metropolitan Municipality (İBB) | No | ✅ | [Link](https://data.ibb.gov.tr) |
| **National Park Service, US** | Data from the US National Park Service. | 🔑 ApiKey | ✅ | [Link](https://www.nps.gov/subjects/developer/) |
| **Open Government, ACT** | Australian Capital Territory Open Data. | No | ✅ | [Link](https://www.data.act.gov.au/) |
| **Open Government, Argentina** | Argentina Government Open Data. | No | ✅ | [Link](https://datos.gob.ar/) |
| **Open Government, Australia** | Australian Government Open Data. | No | ✅ | [Link](https://www.data.gov.au/) |
| **Open Government, Austria** | Austria Government Open Data. | No | ✅ | [Link](https://www.data.gv.at/) |
| **Open Government, Belgium** | Belgium Government Open Data. | No | ✅ | [Link](https://data.gov.be/) |
| **Open Government, Canada** | Canadian Government Open Data. | No | No | [Link](http://open.canada.ca/en) |
| **Open Government, Colombia** | Colombia Government Open Data. | No | No | [Link](https://www.dane.gov.co/) |
| **Open Government, Cyprus** | Cyprus Government Open Data. | No | ✅ | [Link](https://data.gov.cy/?language=en) |
| **Open Government, Czech Republic** | Czech Republic Government Open Data. | No | ✅ | [Link](https://data.gov.cz/english/) |
| **Open Government, Denmark** | Denmark Government Open Data. | No | ✅ | [Link](https://www.opendata.dk/) |
| **Open Government, Estonia** | Estonia Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://avaandmed.eesti.ee/instructions/opendata-dataset-api) |
| **Open Government, Finland** | Finland Government Open Data. | No | ✅ | [Link](https://www.avoindata.fi/en) |
| **Open Government, France** | French Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://www.data.gouv.fr/) |
| **Open Government, Germany** | Germany Government Open Data. | No | ✅ | [Link](https://www.govdata.de/daten/-/details/govdata-metadatenkatalog) |
| **Open Government, Greece** | Greece Government Open Data. | 🔐 OAuth | ✅ | [Link](https://data.gov.gr/) |
| **Open Government, India** | Indian Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://data.gov.in/) |
| **Open Government, Ireland** | Ireland Government Open Data. | No | ✅ | [Link](https://data.gov.ie/pages/developers) |
| **Open Government, Italy** | Italy Government Open Data. | No | ✅ | [Link](https://www.dati.gov.it/) |
| **Open Government, Korea** | Korea Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://www.data.go.kr/) |
| **Open Government, Lithuania** | Lithuania Government Open Data. | No | ✅ | [Link](https://data.gov.lt/public/api/1) |
| **Open Government, Luxembourg** | Luxembourgish Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://data.public.lu) |
| **Open Government, Mexico** | Mexican Statistical Government Open Data. | No | ✅ | [Link](https://www.inegi.org.mx/datos/) |
| **Open Government, Netherlands** | Netherlands Government Open Data. | No | ✅ | [Link](https://data.overheid.nl/en/ondersteuning/data-publiceren/api) |
| **Open Government, New South Wales** | New South Wales Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://api.nsw.gov.au/) |
| **Open Government, New Zealand** | New Zealand Government Open Data. | No | ✅ | [Link](https://www.data.govt.nz/) |
| **Open Government, Norway** | Norwegian Government Open Data. | No | ✅ | [Link](https://data.norge.no/dataservices) |
| **Open Government, Peru** | Peru Government Open Data. | No | ✅ | [Link](https://www.datosabiertos.gob.pe/) |
| **Open Government, Poland** | Poland Government Open Data. | No | ✅ | [Link](https://dane.gov.pl/en) |
| **Open Government, Portugal** | Portugal Government Open Data. | No | ✅ | [Link](https://dados.gov.pt/en/docapi/) |
| **Open Government, Queensland Government** | Queensland Government Open Data. | No | ✅ | [Link](https://www.data.qld.gov.au/) |
| **Open Government, Romania** | Romania Government Open Data. | No | No | [Link](http://data.gov.ro/) |
| **Open Government, Saudi Arabia** | Saudi Arabia Government Open Data. | No | ✅ | [Link](https://data.gov.sa) |
| **Open Government, Slovakia** | Slovakia Government Open Data. | No | ✅ | [Link](https://data.gov.sk/en/) |
| **Open Government, Slovenia** | Slovenia Government Open Data. | No | ✅ | [Link](https://podatki.gov.si/) |
| **Open Government, South Australian Government** | South Australian Government Open Data. | No | ✅ | [Link](https://data.sa.gov.au/) |
| **Open Government, Spain** | Spain Government Open Data. | No | ✅ | [Link](https://datos.gob.es/en) |
| **Open Government, Sweden** | Sweden Government Open Data. | No | ✅ | [Link](https://www.dataportal.se/en/dataservice/91_29789/api-for-the-statistical-database) |
| **Open Government, Switzerland** | Switzerland Government Open Data. | No | ✅ | [Link](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) |
| **Open Government, Taiwan** | Taiwan Government Open Data. | No | ✅ | [Link](https://data.gov.tw/) |
| **Open Government, Thailand** | Thailand Government Open Data. | 🔑 ApiKey | ✅ | [Link](https://data.go.th/) |
| **Open Government, UK** | UK Government Open Data. | No | ✅ | [Link](https://data.gov.uk/) |
| **Open Government, USA** | United States Government Open Data. | No | ✅ | [Link](https://www.data.gov/) |
| **Open Government, Victoria State Government** | Victoria State Government Open Data. | No | ✅ | [Link](https://www.data.vic.gov.au/) |
| **Open Government, West Australia** | West Australia Open Data. | No | ✅ | [Link](https://data.wa.gov.au/) |
| **PRC Exam Schedule** | Unofficial Philippine Professional Regulation Commission's examination schedule. | No | ✅ | [Link](https://api.whenisthenextboardexam.com/docs/) |
| **Represent by Open North** | Find Canadian Government Representatives. | No | ✅ | [Link](https://represent.opennorth.ca/) |
| **UK Companies House** | UK Companies House Data from the UK government. | 🔐 OAuth | ✅ | [Link](https://developer.company-information.service.gov.uk/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="video"></a>📹 Video

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **api.video** | Video hosting, encoding, and live streaming. | 🔑 ApiKey | ✅ | [Link](https://docs.api.video/) |
| **Mux** | Video infrastructure and analytics. | 🔑 ApiKey | ✅ | [Link](https://docs.mux.com/) |
| **Cloudflare Stream** | Video streaming and delivery. | 🔑 ApiKey | ✅ | [Link](https://developers.cloudflare.com/stream/) |
| **Openverse** | Search openly-licensed media. | No | ✅ | [Link](https://api.openverse.org/v1/) |
| **Vimeo** | Video hosting and sharing platform. | 🔐 OAuth | ✅ | [Link](https://developer.vimeo.com/) |
| **Dailymotion** | Video platform and publishing API. | 🔐 OAuth | ✅ | [Link](https://developers.dailymotion.com/api/) |
| **PeerTube** | Federated video platform API. | No | ✅ | [Link](https://docs.joinpeertube.org/api-rest-reference.html) |
| **An API of Ice And Fire** | Game Of Thrones API. | No | ✅ | [Link](https://anapioficeandfire.com/) |
| **Breaking Bad** | Breaking Bad API. | No | ✅ | [Link](https://breakingbadapi.com/documentation) |
| **Catalogopolis** | Doctor Who API. | No | ✅ | [Link](https://api.catalogopolis.xyz/docs/) |
| **Czech Television** | TV programme of Czech TV. | No | No | [Link](http://www.ceskatelevize.cz/xml/tv-program/) |
| **Dune** | A simple API which provides you with book, character, movie and quotes JSON data. | No | ✅ | [Link](https://github.com/ywalia01/dune-api) |
| **Final Space** | Final Space API. | No | ✅ | [Link](https://finalspaceapi.com/docs/) |
| **Game of Thrones Quotes** | Some Game of Thrones quotes. | No | ✅ | [Link](https://gameofthronesquotes.xyz/) |
| **IMDb API** | Movie, serial and cast information. | 🔑 ApiKey | ✅ | [Link](https://imdbapi.dev/) |
| **IMDbOT** | Unofficial IMDb Movie / Series Information. | No | ✅ | [Link](https://github.com/SpEcHiDe/IMDbOT) |
| **JSON2Video** | Create and edit videos programmatically: watermarks,resizing,slideshows,voice... | 🔑 ApiKey | ✅ | [Link](https://json2video.com) |
| **Lucifer Quotes** | Returns Lucifer quotes. | No | ✅ | [Link](https://github.com/shadowoff09/lucifer-quotes) |
| **MCU Countdown** | A Countdown to the next MCU Film. | No | ✅ | [Link](https://github.com/DiljotSG/MCU-Countdown) |
| **Movie Quote** | Random Movie and Series Quotes. | No | ✅ | [Link](https://github.com/F4R4N/movie-quote/) |
| **Ron Swanson Quotes** | Television. | No | ✅ | [Link](https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api) |
| **STAPI** | Information on all things Star Trek. | No | No | [Link](http://stapi.co) |
| **Stranger Things Quotes** | Returns Stranger Things quotes. | No | ✅ | [Link](https://github.com/shadowoff09/strangerthings-quotes) |
| **Stream** | Czech internet television, films, series and online videos for free. | No | ✅ | [Link](https://api.stream.cz/graphiql) |
| **Stromberg Quotes** | Returns Stromberg quotes and more. | No | ✅ | [Link](https://www.stromberg-api.de/) |
| **SWAPI** | All the Star Wars data you've ever wanted. | No | ✅ | [Link](https://swapi.dev/) |
| **SWAPI GraphQL** | Star Wars GraphQL API. | No | ✅ | [Link](https://graphql.org/swapi-graphql) |
| **The Lord of the Rings** | The Lord of the Rings API. | 🔑 ApiKey | ✅ | [Link](https://the-one-api.dev/) |
| **The Vampire Diaries** | TV Show Data. | 🔑 ApiKey | ✅ | [Link](https://vampire-diaries-api.netlify.app/) |
| **ThronesApi** | Game Of Thrones Characters Data with imagery. | No | ✅ | [Link](https://thronesapi.com/) |
| **TrailerAddict** | Easily embed trailers from TrailerAddict. | 🔑 ApiKey | No | [Link](https://www.traileraddict.com/trailerapi) |
| **TVDB** | Television data. | 🔑 ApiKey | ✅ | [Link](https://thetvdb.com/api-information) |
| **uNoGS** | Unofficial Netflix Online Global Search, Search all netflix regions in one place. | 🔑 ApiKey | ✅ | [Link](https://rapidapi.com/unogs/api/unogsng) |
| **Web Series Quotes Generator** | API generates various Web Series Quote Images. | No | ✅ | [Link](https://github.com/yogeshwaran01/web-series-quotes) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="math-computation"></a>🔢 Math & Computation

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **math.js** | Mathematical expression evaluation API. | No | ✅ | [Link](https://api.mathjs.org/) |
| **CountAPI** | Free counting API for web pages. | No | ✅ | [Link](https://api.countapi.xyz/) |
| **Unit Converter** | Convert between various units. | No | ✅ | [Link](https://api-ninjas.com/api/convertcurrency) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="unofficial-community"></a>⚠️ Unofficial & Community APIs

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
| **Arbeitnow** | Free remote job board API. | No | ✅ | [Link](https://documenter.getpostman.com/view/18545278/UVJbJdKh) |
| **Jobicy** | Remote job listings feed API. | No | ✅ | [Link](https://jobicy.com/jobs-rss-feed) |
| **Himalayas** | Remote jobs API and company data. | No | ✅ | [Link](https://himalayas.app/api) |
| **Arbeitsamt** | API for the "Arbeitsamt", which is a german Job board aggregator. | 🔐 OAuth | ✅ | [Link](https://jobsuche.api.bund.dev/) |
| **Careerjet** | Job search engine. | 🔑 ApiKey | No | [Link](https://www.careerjet.com/partners/api/) |
| **DevITjobs UK** | Jobs with GraphQL. | No | ✅ | [Link](https://devitjobs.uk/job_feed.xml) |
| **Findwork** | Job board. | 🔑 ApiKey | ✅ | [Link](https://findwork.dev/developers/) |
| **Jobs2Careers** | Job aggregator. | 🔑 ApiKey | ✅ | [Link](http://api.jobs2careers.com/api/spec.pdf) |
| **Jooble** | Job search engine. | 🔑 ApiKey | ✅ | [Link](https://jooble.org/api/about) |
| **Juju** | Job search engine. | 🔑 ApiKey | No | [Link](http://www.juju.com/publisher/spec/) |
| **Open Skills** | Job titles, skills and related jobs data. | No | No | [Link](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview) |
| **Upwork** | Freelance job board and management system. | 🔐 OAuth | ✅ | [Link](https://developers.upwork.com/) |
| **WhatJobs** | Job search engine. | 🔑 ApiKey | ✅ | [Link](https://www.whatjobs.com/affiliates) |
| **ZipRecruiter** | Job search app and website. | 🔑 ApiKey | ✅ | [Link](https://www.ziprecruiter.com/publishers) |

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
| **Aemet** | Weather and forecast data from Spain. | 🔑 ApiKey | ✅ | [Link](https://opendata.aemet.es/centrodedescargas/inicio) |
| **APIXU** | Weather. | 🔑 ApiKey | ✅ | [Link](https://www.apixu.com/doc/request.aspx) |
| **AviationWeather** | NOAA aviation weather forecasts and observations. | No | ✅ | [Link](https://www.aviationweather.gov/dataserver) |
| **ColorfulClouds** | Weather. | 🔑 ApiKey | ✅ | [Link](https://open.caiyunapp.com/ColorfulClouds_Weather_API) |
| **Euskalmet** | Meteorological data of the Basque Country. | 🔑 ApiKey | ✅ | [Link](https://opendata.euskadi.eus/api-euskalmet/-/api-de-euskalmet/) |
| **Foreca** | Weather. | 🔐 OAuth | ✅ | [Link](https://developer.foreca.com) |
| **HG Weather** | Provides weather forecast data for cities in Brazil. | 🔑 ApiKey | ✅ | [Link](https://hgbrasil.com/status/weather) |
| **Hong Kong Obervatory** | Provide weather information, earthquake information, and climate data. | No | ✅ | [Link](https://www.hko.gov.hk/en/abouthko/opendata_intro.htm) |
| **MetaWeather** | Weather. | No | ✅ | [Link](https://www.metaweather.com/api/) |
| **Meteorologisk Institutt** | Weather and climate data. | 🔑 ApiKey | ✅ | [Link](https://api.met.no/weatherapi/documentation) |
| **Micro Weather** | Real time weather forecasts and historic data. | 🔑 ApiKey | ✅ | [Link](https://m3o.com/weather/api) |
| **ODWeather** | Weather and weather webcams. | No | No | [Link](http://api.oceandrivers.com/static/docs.html) |
| **Oikolab** | 70+ years of global, hourly historical and forecast weather data from NOAA an... | 🔑 ApiKey | ✅ | [Link](https://docs.oikolab.com) |
| **openSenseMap** | Data from Personal Weather Stations called senseBoxes. | No | ✅ | [Link](https://api.opensensemap.org/) |
| **OpenUV** | Real-time UV Index Forecast. | 🔑 ApiKey | ✅ | [Link](https://www.openuv.io) |
| **QWeather** | Location-based weather data. | 🔑 ApiKey | ✅ | [Link](https://dev.qweather.com/en/) |
| **Storm Glass** | Global marine weather from multiple sources. | 🔑 ApiKey | ✅ | [Link](https://stormglass.io/) |
| **Tomorrow** | Weather API Powered by Proprietary Technology. | 🔑 ApiKey | ✅ | [Link](https://docs.tomorrow.io) |
| **US Weather** | US National Weather Service. | No | ✅ | [Link](https://www.weather.gov/documentation/services-web-api) |
| **weather-api** | A RESTful free API to check the weather. | No | ✅ | [Link](https://github.com/robertoduessmann/weather-api) |
| **Yandex.Weather** | Assesses weather condition in specific locations. | 🔑 ApiKey | ✅ | [Link](https://yandex.com/dev/weather/) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="business"></a>💼 Business

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Charity Search** | Non-profit charity data. | 🔑 ApiKey | No | [Link](http://charityapi.orghunter.com/) |
| **Clearbit Logo** | Search for company logos and embed them in your projects. | 🔑 ApiKey | ✅ | [Link](https://clearbit.com/docs#logo-api) |
| **Domainsdb.info** | Registered Domain Names Search. | No | ✅ | [Link](https://domainsdb.info/) |
| **Freelancer** | Hire freelancers to get work done. | 🔐 OAuth | ✅ | [Link](https://developers.freelancer.com) |
| **Gmail** | Flexible, RESTful access to the user's inbox. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/gmail/api/) |
| **Google Analytics** | Collect, configure and analyze your data to reach the right audience. | 🔐 OAuth | ✅ | [Link](https://developers.google.com/analytics/) |
| **markerapi** | Trademark Search. | No | No | [Link](https://markerapi.com) |
| **ORB Intelligence** | Company lookup. | 🔑 ApiKey | ✅ | [Link](https://api.orb-intelligence.com/docs/) |
| **SwiftKanban** | Kanban software, Visualize Work, Increase Organizations Lead Time, Throughput... | 🔑 ApiKey | ✅ | [Link](https://www.digite.com/knowledge-base/swiftkanban/article/api-for-swift-kanban-web-services/#restapi) |
| **Tenders in Hungary** | Get data for procurements in Hungary in JSON format. | No | ✅ | [Link](https://tenders.guru/hu/api) |
| **Tenders in Poland** | Get data for procurements in Poland in JSON format. | No | ✅ | [Link](https://tenders.guru/pl/api) |
| **Tenders in Romania** | Get data for procurements in Romania in JSON format. | No | ✅ | [Link](https://tenders.guru/ro/api) |
| **Tenders in Spain** | Get data for procurements in Spain in JSON format. | No | ✅ | [Link](https://tenders.guru/es/api) |
| **Tenders in Ukraine** | Get data for procurements in Ukraine in JSON format. | No | ✅ | [Link](https://tenders.guru/ua/api) |

[⬆ Back to Table of Contents](#-table-of-contents)

## <a id="documents-productivity"></a>📄 Documents & Productivity

| API Name | Description | Auth | HTTPS | Link |
| :--- | :--- | :---: | :---: | :---: |
| **Api2Convert** | Online File Conversion API. | 🔑 ApiKey | ✅ | [Link](https://www.api2convert.com/) |
| **Asana** | Programmatic access to all data in your asana system. | 🔑 ApiKey | ✅ | [Link](https://developers.asana.com/docs) |
| **ClickUp** | ClickUp is a robust, cloud-based project management tool for boosting product... | 🔐 OAuth | ✅ | [Link](https://clickup.com/api) |
| **Clockify** | Clockify's REST-based API can be used to push/pull data to/from it & integrat... | 🔑 ApiKey | ✅ | [Link](https://clockify.me/developers-api) |
| **CloudConvert** | Online file converter for audio, video, document, ebook, archive, image, spre... | 🔑 ApiKey | ✅ | [Link](https://cloudconvert.com/api/v2) |
| **Cloudmersive Document and Data Conversion** | HTML/URL to PDF/PNG, Office documents to PDF, image conversion. | 🔑 ApiKey | ✅ | [Link](https://cloudmersive.com/convert-api) |
| **Code::Stats** | Automatic time tracking for programmers. | 🔑 ApiKey | ✅ | [Link](https://codestats.net/api-docs) |
| **CraftMyPDF** | Generate PDF documents from templates with a drop-and-drop editor and a simpl... | 🔑 ApiKey | ✅ | [Link](https://craftmypdf.com) |
| **Flowdash** | Automate business workflows. | 🔑 ApiKey | ✅ | [Link](https://docs.flowdash.com/docs/api-introduction) |
| **Html2PDF** | HTML/URL to PDF. | 🔑 ApiKey | ✅ | [Link](https://html2pdf.app/) |
| **iLovePDF** | Convert, merge, split, extract text and add page numbers for PDFs. Free for 2... | 🔑 ApiKey | ✅ | [Link](https://developer.ilovepdf.com/) |
| **JIRA** | JIRA is a proprietary issue tracking product that allows bug tracking and agi... | 🔐 OAuth | ✅ | [Link](https://developer.atlassian.com/server/jira/platform/rest-apis/) |
| **Mattermost** | An open source platform for developer collaboration. | 🔐 OAuth | ✅ | [Link](https://api.mattermost.com/) |
| **Mercury** | Web parser. | 🔑 ApiKey | ✅ | [Link](https://mercury.postlight.com/web-parser/) |
| **Monday** | Programmatically access and update data inside a monday.com account. | 🔑 ApiKey | ✅ | [Link](https://api.developer.monday.com/docs) |
| **PandaDoc** | DocGen and eSignatures API. | 🔑 ApiKey | ✅ | [Link](https://developers.pandadoc.com) |
| **Pocket** | Bookmarking service. | 🔐 OAuth | ✅ | [Link](https://getpocket.com/developer/) |
| **Podio** | File sharing and productivity. | 🔐 OAuth | ✅ | [Link](https://developers.podio.com) |
| **PrexView** | Data from XML or JSON to PDF, HTML or Image. | 🔑 ApiKey | ✅ | [Link](https://prexview.com) |
| **Restpack** | Provides screenshot, HTML to PDF and content extraction APIs. | 🔑 ApiKey | ✅ | [Link](https://restpack.io/) |
| **Todoist** | Todo Lists. | 🔐 OAuth | ✅ | [Link](https://developer.todoist.com) |
| **Smart Image Enhancement API** | Performs image upscaling by adding detail to images through multiple super-re... | 🔑 ApiKey | ✅ | [Link](https://apilayer.com/marketplace/image_enhancement-api) |
| **Vector Express v2.0** | Free vector file converting API. | No | ✅ | [Link](https://vector.express) |
| **WakaTime** | Automated time tracking leaderboards for programmers. | No | ✅ | [Link](https://wakatime.com/developers) |
| **Zube** | Full stack project management. | 🔐 OAuth | ✅ | [Link](https://zube.io/docs/api) |

[⬆ Back to Table of Contents](#-table-of-contents)
## 🤝 Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

You can also use the GitHub issue templates to suggest new APIs, report bugs, or request improvements.

## 🛡️ Code of Conduct

This project follows the [Code of Conduct](./CODE_OF_CONDUCT.md). Please be respectful and constructive.

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ThanhNguyxn/awesome-free-apis&type=Date)](https://star-history.com/#ThanhNguyxn/awesome-free-apis&Date)

---

<div align="center">

**Don't forget to ⭐ this repo if you found it useful!**

</div>
