#!/usr/bin/env python3
"""Reorganize README categories and add curated APIs."""

from __future__ import annotations

import re
from dataclasses import dataclass


README_PATH = "README.md"


@dataclass(frozen=True)
class Heading:
    start: int
    end: int
    line: str
    slug: str | None
    title: str | None


HEADING_RE = re.compile(r"(?m)^## (.+)$")
ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>(.+)$')
ROW_RE = re.compile(r"^\| \*\*(.+?)\*\* \|")


NEW_CATEGORY_TITLES = {
    "url-shorteners": "🔗 URL Shorteners",
    "continuous-integration": "⚙️ Continuous Integration",
    "phone-telephony": "📱 Phone & Telephony",
    "text-analysis-nlp": "📝 Text Analysis & NLP",
    "podcasts": "🎙️ Podcasts",
    "events": "🎪 Events",
    "currency-exchange": "💱 Currency Exchange",
    "tracking-logistics": "📦 Tracking & Logistics",
    "iot-smart-devices": "🏠 IoT & Smart Devices",
    "data-validation": "✅ Data Validation",
    "open-source-projects": "🔓 Open Source Projects",
    "personality-quotes": "💭 Personality & Quotes",
}


MOVE_SPECS = [
    ("utilities-tools", "TinyURL", "url-shorteners"),
    ("utilities-tools", "Short.io", "url-shorteners"),
    ("utilities-tools", "1pt", "url-shorteners"),
    ("utilities-tools", "Bitly", "url-shorteners"),
    ("utilities-tools", "CleanURI", "url-shorteners"),
    ("utilities-tools", "ClickMeter", "url-shorteners"),
    ("utilities-tools", "Clico", "url-shorteners"),
    ("utilities-tools", "Cutt.ly", "url-shorteners"),
    ("utilities-tools", "Drivet URL Shortener", "url-shorteners"),
    ("utilities-tools", "Free Url Shortener", "url-shorteners"),
    ("utilities-tools", "Git.io", "url-shorteners"),
    ("utilities-tools", "GoTiny", "url-shorteners"),
    ("utilities-tools", "Kutt", "url-shorteners"),
    ("utilities-tools", "Mgnet.me", "url-shorteners"),
    ("utilities-tools", "Shrtcode", "url-shorteners"),
    ("utilities-tools", "UrlBae", "url-shorteners"),
    ("development", "Rebrandly", "url-shorteners"),
    ("development", "Azure DevOps Health", "continuous-integration"),
    ("development", "Bitrise", "continuous-integration"),
    ("development", "Buddy", "continuous-integration"),
    ("development", "Codeship", "continuous-integration"),
    ("development", "Travis CI", "continuous-integration"),
    ("utilities-tools", "Phone Validation", "phone-telephony"),
    ("utilities-tools", "Phone Specification", "phone-telephony"),
    ("utilities-tools", "Veriphone", "phone-telephony"),
    (
        "development",
        "Cloudmersive Natural Language Processing",
        "text-analysis-nlp",
    ),
    ("development", "Detect Language", "text-analysis-nlp"),
    ("development", "ELI", "text-analysis-nlp"),
    ("development", "Google Cloud Natural", "text-analysis-nlp"),
    ("development", "Hirak OCR", "text-analysis-nlp"),
    ("development", "Hirak Translation", "text-analysis-nlp"),
    ("development", "Lecto Translation", "text-analysis-nlp"),
    ("development", "Semantria", "text-analysis-nlp"),
    ("development", "Sentiment Analysis", "text-analysis-nlp"),
    ("development", "Tisane", "text-analysis-nlp"),
    (
        "development",
        "Watson Natural Language Understanding",
        "text-analysis-nlp",
    ),
    ("development", "Code Detection API", "text-analysis-nlp"),
    ("development", "LibreTranslate", "text-analysis-nlp"),
    ("entertainment", "Podcast Index", "podcasts"),
    ("entertainment", "Eventbrite", "events"),
    ("entertainment", "SeatGeek", "events"),
    ("entertainment", "Ticketmaster", "events"),
    ("finance", "Currencylayer", "currency-exchange"),
    ("finance", "CurrencyAPI", "currency-exchange"),
    ("finance", "CurrencyFreaks", "currency-exchange"),
    ("finance", "Exchangeratesapi", "currency-exchange"),
    ("finance", "Fixer", "currency-exchange"),
    ("finance", "National Bank of Poland", "currency-exchange"),
    ("finance", "Exchangerate.host", "currency-exchange"),
    ("finance", "Frankfurter", "currency-exchange"),
    ("finance", "1Forge", "currency-exchange"),
    ("finance", "Amdoren", "currency-exchange"),
    ("finance", "Bank of Russia", "currency-exchange"),
    ("finance", "Currency-api", "currency-exchange"),
    ("finance", "CurrencyScoop", "currency-exchange"),
    ("finance", "Czech National Bank", "currency-exchange"),
    ("finance", "Economia.Awesome", "currency-exchange"),
    ("finance", "FreeForexAPI", "currency-exchange"),
    ("math-computation", "Open Exchange Rates", "currency-exchange"),
    ("math-computation", "ExchangeRate-API", "currency-exchange"),
    ("math-computation", "VATComply", "currency-exchange"),
    ("utilities-tools", "Aftership", "tracking-logistics"),
    ("utilities-tools", "Correios", "tracking-logistics"),
    ("utilities-tools", "Pixela", "tracking-logistics"),
    ("utilities-tools", "PostalPinCode", "tracking-logistics"),
    ("utilities-tools", "Postmon", "tracking-logistics"),
    ("utilities-tools", "PostNord", "tracking-logistics"),
    ("utilities-tools", "UPS", "tracking-logistics"),
    ("utilities-tools", "WeCanTrack", "tracking-logistics"),
    ("utilities-tools", "WhatPulse", "tracking-logistics"),
    ("development", "Blynk-Cloud", "iot-smart-devices"),
    ("development", "IFTTT", "iot-smart-devices"),
    ("security-validation", "Lob.com", "data-validation"),
    ("security-validation", "US Autocomplete", "data-validation"),
    ("security-validation", "US Extract", "data-validation"),
    ("security-validation", "US Street Address", "data-validation"),
    ("security-validation", "vatlayer", "data-validation"),
    ("development", "Countly", "open-source-projects"),
    ("development", "Creative Commons Catalog", "open-source-projects"),
    ("development", "Drupal.org", "open-source-projects"),
    (
        "development",
        "GitHub Contribution Chart Generator",
        "open-source-projects",
    ),
    ("development", "GitHub ReadMe Stats", "open-source-projects"),
    ("development", "Metabase", "open-source-projects"),
    ("utilities-tools", "Shields.io", "open-source-projects"),
    ("entertainment", "Quotable", "personality-quotes"),
    ("entertainment", "FavQs.com", "personality-quotes"),
    ("entertainment", "Forismatic", "personality-quotes"),
    ("entertainment", "Programming Quotes", "personality-quotes"),
    ("entertainment", "Quotes on Design", "personality-quotes"),
    ("entertainment", "Stoicism Quote", "personality-quotes"),
    ("entertainment", "They Said So Quotes", "personality-quotes"),
    ("entertainment", "Traitify", "personality-quotes"),
    ("entertainment", "Udemy(instructor)", "personality-quotes"),
    ("entertainment", "Vadivelu HTTP Codes", "personality-quotes"),
    ("entertainment", "Dictum", "personality-quotes"),
    ("entertainment", "Inspiration", "personality-quotes"),
    ("entertainment", "Medium", "personality-quotes"),
]


NEW_APIS = {
    "url-shorteners": [
        {
            "name": "BL.INK",
            "description": "URL shortener and branded link management.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://bl.ink/developers",
        },
        {
            "name": "Dub",
            "description": "Open-source short links and analytics.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://dub.co/docs/api-reference/introduction",
        },
        {
            "name": "is.gd",
            "description": "Simple free URL shortening API.",
            "auth": "No",
            "https": "✅",
            "url": "https://is.gd/apishorteningreference.php",
        },
        {
            "name": "Polr",
            "description": "Open-source URL shortener API.",
            "auth": "No",
            "https": "✅",
            "url": "https://docs.polrproject.org/en/latest/developer-guide/api/",
        },
        {
            "name": "Shlink",
            "description": "Self-hosted URL shortener with REST API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://shlink.io/documentation/api-docs/",
        },
        {
            "name": "Tiny.cc",
            "description": "Link shortening and management API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://tiny.cc/api-docs",
        },
        {
            "name": "v.gd",
            "description": "Free URL shortener API service.",
            "auth": "No",
            "https": "✅",
            "url": "https://v.gd/apishorteningreference.php",
        },
        {
            "name": "YOURLS",
            "description": "Self-hosted shortener with extensible API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://yourls.org/#API",
        },
    ],
    "continuous-integration": [
        {
            "name": "AppVeyor",
            "description": "CI/CD builds API (free for OSS).",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.appveyor.com/docs/api/",
        },
        {
            "name": "Buildkite",
            "description": "Pipeline and build automation API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://buildkite.com/docs/apis/rest-api",
        },
        {
            "name": "CircleCI",
            "description": "CI pipelines, workflows, and artifacts API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://circleci.com/docs/api/v2/",
        },
        {
            "name": "Cirrus CI",
            "description": "CI pipelines and task automation API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://cirrus-ci.org/api/",
        },
        {
            "name": "Drone",
            "description": "CI pipeline API for Drone server.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.drone.io/api/",
        },
        {
            "name": "Jenkins",
            "description": "Automation server remote API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.jenkins.io/doc/book/using/remote-access-api/",
        },
        {
            "name": "Semaphore",
            "description": "CI/CD projects, workflows, and jobs API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.semaphoreci.com/reference/api",
        },
        {
            "name": "TeamCity",
            "description": "Build server REST API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.jetbrains.com/help/teamcity/rest/teamcity-rest-api-documentation.html",
        },
    ],
    "phone-telephony": [
        {
            "name": "46elks",
            "description": "SMS and voice telephony API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://46elks.com/docs",
        },
        {
            "name": "Apifonica",
            "description": "Voice call automation API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.apifonica.com/docs/voice-api/",
        },
        {
            "name": "Bandwidth",
            "description": "Voice, messaging, and phone number APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://dev.bandwidth.com/docs/",
        },
        {
            "name": "MessageBird",
            "description": "SMS and omnichannel messaging APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.messagebird.com/api/",
        },
        {
            "name": "NeutrinoAPI Phone Validate",
            "description": "Phone validation and carrier lookup.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.neutrinoapi.com/api/phone-validate/",
        },
        {
            "name": "Plivo",
            "description": "Voice and SMS communication APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.plivo.com/docs/home",
        },
        {
            "name": "Sinch",
            "description": "SMS, voice, and verification APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.sinch.com/",
        },
        {
            "name": "Telnyx",
            "description": "Telephony, messaging, and SIP APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.telnyx.com/api-reference/overview",
        },
        {
            "name": "Textbelt",
            "description": "Lightweight SMS sending API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.textbelt.com/",
        },
    ],
    "text-analysis-nlp": [
        {
            "name": "Dandelion",
            "description": "Entity extraction and text analytics API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://dandelion.eu/docs/api/",
        },
        {
            "name": "DeepL",
            "description": "Translation and multilingual text API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.deepl.com/docs-api",
        },
        {
            "name": "Eden AI",
            "description": "Unified NLP APIs across providers.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.edenai.co/reference/introduction",
        },
        {
            "name": "LanguageTool",
            "description": "Grammar and style checking API.",
            "auth": "No",
            "https": "✅",
            "url": "https://languagetool.org/http-api/swagger-ui/#/",
        },
        {
            "name": "ParallelDots",
            "description": "Sentiment and NLP analysis APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://komprehend.io/",
        },
        {
            "name": "Sapling",
            "description": "Grammar correction and writing APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://sapling.ai/docs/",
        },
        {
            "name": "TextRazor",
            "description": "NLP extraction and classification API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.textrazor.com/docs/rest",
        },
        {
            "name": "Wit.ai",
            "description": "Intent/entity extraction for text/voice.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://wit.ai/docs/http/20240304/",
        },
    ],
    "podcasts": [
        {
            "name": "Acast",
            "description": "Podcast platform and publisher APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.acast.com/",
        },
        {
            "name": "Audioboom",
            "description": "Podcast metadata and episode endpoints.",
            "auth": "No",
            "https": "✅",
            "url": "https://api.audioboom.com/",
        },
        {
            "name": "Buzzsprout",
            "description": "Podcast hosting and episodes API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.buzzsprout.com/api",
        },
        {
            "name": "Fountain",
            "description": "Podcast app developer API resources.",
            "auth": "No",
            "https": "✅",
            "url": "https://fountain.fm/developer",
        },
        {
            "name": "fyyd",
            "description": "Podcast search and metadata API.",
            "auth": "No",
            "https": "✅",
            "url": "https://api.fyyd.de/",
        },
        {
            "name": "gpodder.net",
            "description": "Podcast sync and subscriptions API.",
            "auth": "No",
            "https": "✅",
            "url": "https://gpoddernet.readthedocs.io/en/latest/api/index.html",
        },
        {
            "name": "Podbean",
            "description": "Podcast hosting and distribution API.",
            "auth": "🔐 OAuth",
            "https": "✅",
            "url": "https://developers.podbean.com/",
        },
        {
            "name": "Taddy",
            "description": "GraphQL podcast search and metadata API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://taddy.org/developers",
        },
    ],
    "events": [
        {
            "name": "Eventyay",
            "description": "Open-source event management API.",
            "auth": "No",
            "https": "✅",
            "url": "https://api.eventyay.com/",
        },
        {
            "name": "Luma",
            "description": "Event creation and attendee APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.luma.com/reference/getting-started",
        },
        {
            "name": "OpenAgenda",
            "description": "Event agenda and discovery API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.openagenda.com/",
        },
        {
            "name": "PredictHQ",
            "description": "Event intelligence and impact API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.predicthq.com/",
        },
        {
            "name": "pretix",
            "description": "Ticketing and event operations API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.pretix.eu/dev/api/index.html",
        },
        {
            "name": "Sessionize",
            "description": "CFP sessions and speakers API.",
            "auth": "No",
            "https": "✅",
            "url": "https://sessionize.com/playbook/api/",
        },
        {
            "name": "Ticket Tailor",
            "description": "Ticketing and order management API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.tickettailor.com/",
        },
        {
            "name": "Ti.to",
            "description": "Event ticketing and registrations API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://ti.to/docs/api",
        },
    ],
    "currency-exchange": [
        {
            "name": "Bank of Canada Valet",
            "description": "Free central-bank exchange/economic series API.",
            "auth": "No",
            "https": "✅",
            "url": "https://www.bankofcanada.ca/valet/docs",
        },
        {
            "name": "ECB Data API",
            "description": "Public ECB data API for exchange rates.",
            "auth": "No",
            "https": "✅",
            "url": "https://data.ecb.europa.eu/help/api/data",
        },
        {
            "name": "Fawaz Currency API",
            "description": "Free exchange-rate API (200+ currencies).",
            "auth": "No",
            "https": "✅",
            "url": "https://github.com/fawazahmed0/exchange-api",
        },
        {
            "name": "CurrencyBeacon",
            "description": "Real-time and historical exchange rates.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://currencybeacon.com/api-documentation",
        },
        {
            "name": "FreeCurrencyAPI",
            "description": "Free currency conversion API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://freecurrencyapi.com/docs",
        },
        {
            "name": "CurrencyConverterAPI",
            "description": "Free currency converter.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://currencyconverterapi.com/docs",
        },
    ],
    "tracking-logistics": [
        {
            "name": "17TRACK",
            "description": "Shipment tracking API with free quota.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://asset.17track.net/api/document/v2_en/index.html",
        },
        {
            "name": "Shippo",
            "description": "Shipping API with free test mode.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.goshippo.com/",
        },
        {
            "name": "USPS Track & Confirm",
            "description": "USPS tracking API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.usps.com/business/web-tools-apis/track-and-confirm-api.htm",
        },
        {
            "name": "DHL Shipment Tracking",
            "description": "DHL package tracking API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developer.dhl.com/api-reference/shipment-tracking",
        },
        {
            "name": "FedEx Tracking",
            "description": "FedEx package tracking API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developer.fedex.com/api/en-us/catalog/track.html",
        },
    ],
    "iot-smart-devices": [
        {
            "name": "Adafruit IO",
            "description": "IoT feed/data API with free tier.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://io.adafruit.com/api/docs/",
        },
        {
            "name": "Home Assistant",
            "description": "Self-hosted home automation REST API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.home-assistant.io/docs/api/rest/",
        },
        {
            "name": "ThingsBoard",
            "description": "Open-source IoT platform REST API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://thingsboard.io/docs/reference/rest-api/",
        },
        {
            "name": "Particle Cloud",
            "description": "IoT device management and data API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.particle.io/reference/cloud-apis/api/",
        },
        {
            "name": "Arduino IoT",
            "description": "Arduino IoT Cloud API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.arduino.cc/reference/en/iot/",
        },
        {
            "name": "Tuya Cloud",
            "description": "Smart device management APIs.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developer.tuya.com/en/docs/cloud/",
        },
        {
            "name": "Blynk",
            "description": "IoT device control from cloud.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://docs.blynk.io/",
        },
    ],
    "data-validation": [
        {
            "name": "DeBounce",
            "description": "Email validation API with free credits.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://developers.debounce.com/",
        },
        {
            "name": "Emailable",
            "description": "Email verification API with free tier.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://emailable.com/docs/api",
        },
        {
            "name": "Neutrino Email Validate",
            "description": "Email syntax/DNS/disposable checks.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.neutrinoapi.com/api/email-validate/",
        },
        {
            "name": "Verifalia",
            "description": "Email verification API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://verifalia.com/developers",
        },
        {
            "name": "Byteplant Email Validator",
            "description": "Email validation API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.email-validator.net/api.html",
        },
        {
            "name": "ZeroBounce",
            "description": "Email validation and scoring.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://www.zerobounce.net/docs/email-validation-api-quickstart/v2-get-api-usage/",
        },
    ],
    "open-source-projects": [
        {
            "name": "deps.dev",
            "description": "Open package/dependency intelligence by Google.",
            "auth": "No",
            "https": "✅",
            "url": "https://docs.deps.dev/api/",
        },
        {
            "name": "ecosyste.ms",
            "description": "Open source ecosystem data APIs.",
            "auth": "No",
            "https": "✅",
            "url": "https://docs.ecosyste.ms/",
        },
        {
            "name": "PyPI JSON API",
            "description": "Python package metadata API.",
            "auth": "No",
            "https": "✅",
            "url": "https://docs.pypi.org/api/json/",
        },
        {
            "name": "Packagist",
            "description": "PHP package repository API.",
            "auth": "No",
            "https": "✅",
            "url": "https://packagist.org/apidoc",
        },
        {
            "name": "RubyGems",
            "description": "Ruby package repository API.",
            "auth": "No",
            "https": "✅",
            "url": "https://guides.rubygems.org/rubygems-org-api",
        },
        {
            "name": "Repology",
            "description": "Package version tracking across repos.",
            "auth": "No",
            "https": "✅",
            "url": "https://repology.org/api",
        },
    ],
    "personality-quotes": [
        {
            "name": "Advice Slip",
            "description": "Free random advice API.",
            "auth": "No",
            "https": "✅",
            "url": "https://api.adviceslip.com/",
        },
        {
            "name": "DummyJSON Quotes",
            "description": "Fake quotes dataset API.",
            "auth": "No",
            "https": "✅",
            "url": "https://dummyjson.com/docs/quotes",
        },
        {
            "name": "API-Ninjas Quotes",
            "description": "Curated quotes API.",
            "auth": "🔑 ApiKey",
            "https": "✅",
            "url": "https://api-ninjas.com/api/quotes",
        },
        {
            "name": "Affirmations.dev",
            "description": "Daily affirmations API.",
            "auth": "No",
            "https": "✅",
            "url": "https://www.affirmations.dev/",
        },
        {
            "name": "Zen Quotes",
            "description": "Inspirational quotes API.",
            "auth": "No",
            "https": "✅",
            "url": "https://zenquotes.io/",
        },
        {
            "name": "kanye.rest",
            "description": "Random Kanye West quotes.",
            "auth": "No",
            "https": "✅",
            "url": "https://kanye.rest/",
        },
    ],
}


TABLE_HEADER = [
    "| API Name | Description | Auth | HTTPS | Link |",
    "| :--- | :--- | :---: | :---: | :---: |",
]


def parse_headings(text: str) -> list[Heading]:
    matches = list(HEADING_RE.finditer(text))
    headings: list[Heading] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        line = match.group(1).strip()
        slug = None
        title = None
        anchor_match = ANCHOR_RE.match(line)
        if anchor_match:
            slug = anchor_match.group(1).strip()
            title = anchor_match.group(2).strip()
        headings.append(
            Heading(start=start, end=end, line=line, slug=slug, title=title)
        )
    return headings


def parse_api_rows(section_text: str) -> list[str]:
    rows: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("| **") and stripped.endswith("|"):
            rows.append(stripped)
    return rows


def extract_name(row: str) -> str:
    match = ROW_RE.match(row)
    if not match:
        raise ValueError(f"Invalid API row: {row}")
    return match.group(1).strip()


def format_row(entry: dict[str, str]) -> str:
    return (
        f"| **{entry['name']}** | {entry['description']} | {entry['auth']} | "
        f"{entry['https']} | [Link]({entry['url']}) |"
    )


def find_row_index(rows: list[str], api_name: str) -> int | None:
    for i, row in enumerate(rows):
        if extract_name(row) == api_name:
            return i
    return None


def find_row_globally(
    categories: dict[str, dict[str, object]], api_name: str
) -> tuple[str, int] | None:
    for slug, category in categories.items():
        rows = category["rows"]
        if not isinstance(rows, list):
            continue
        idx = find_row_index(rows, api_name)
        if idx is not None:
            return slug, idx
    return None


def dedupe_rows(rows: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for row in rows:
        key = extract_name(row).lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def insert_after(order: list[str], after_slug: str, new_slugs: list[str]) -> None:
    for slug in new_slugs:
        while slug in order:
            order.remove(slug)
    if after_slug in order:
        pos = order.index(after_slug) + 1
    else:
        pos = len(order)
    for slug in reversed(new_slugs):
        order.insert(pos, slug)


def main() -> int:
    with open(README_PATH, "r", encoding="utf-8") as f:
        original = f.read()

    headings = parse_headings(original)
    category_headings = [
        h for h in headings if h.slug and h.slug != "general-api-usage-guide"
    ]
    if not category_headings:
        raise RuntimeError("No category sections found in README.md")

    first_category_start = min(h.start for h in category_headings)
    last_category_end = max(h.end for h in category_headings)

    categories: dict[str, dict[str, object]] = {}
    for heading in category_headings:
        if heading.slug is None or heading.title is None:
            continue
        section_text = original[heading.start : heading.end]
        categories[heading.slug] = {
            "title": heading.title,
            "rows": parse_api_rows(section_text),
        }

    for slug, title in NEW_CATEGORY_TITLES.items():
        if slug not in categories:
            categories[slug] = {"title": title, "rows": []}

    moved: list[tuple[str, str, str]] = []
    missing_moves: list[tuple[str, str, str]] = []

    for source_slug, api_name, target_slug in MOVE_SPECS:
        source = categories.get(source_slug)
        target = categories.get(target_slug)
        if source is None or target is None:
            missing_moves.append((source_slug, api_name, target_slug))
            continue

        source_rows = source["rows"]
        target_rows = target["rows"]
        if not isinstance(source_rows, list) or not isinstance(target_rows, list):
            missing_moves.append((source_slug, api_name, target_slug))
            continue

        idx = find_row_index(source_rows, api_name)
        actual_source_slug = source_slug

        if idx is None:
            found = find_row_globally(categories, api_name)
            if found is None:
                missing_moves.append((source_slug, api_name, target_slug))
                continue
            actual_source_slug, idx = found
            source_rows = categories[actual_source_slug]["rows"]
            if not isinstance(source_rows, list):
                missing_moves.append((source_slug, api_name, target_slug))
                continue

        row = source_rows.pop(idx)
        target_rows.append(row)
        moved.append((actual_source_slug, api_name, target_slug))

    existing_names: set[str] = set()
    for category in categories.values():
        rows = category["rows"]
        if isinstance(rows, list):
            for row in rows:
                existing_names.add(extract_name(row).lower())

    added_count = 0
    skipped_added = 0
    for slug, entries in NEW_APIS.items():
        rows = categories[slug]["rows"]
        if not isinstance(rows, list):
            continue
        for entry in entries:
            key = entry["name"].lower()
            if key in existing_names:
                skipped_added += 1
                continue
            rows.append(format_row(entry))
            existing_names.add(key)
            added_count += 1

    for slug in NEW_CATEGORY_TITLES:
        rows = categories[slug]["rows"]
        if not isinstance(rows, list):
            continue
        deduped = dedupe_rows(rows)
        deduped.sort(key=lambda row: extract_name(row).lower())
        categories[slug]["rows"] = deduped

    toc_start = original.find("## 📖 Table of Contents")
    if toc_start == -1:
        raise RuntimeError("Table of Contents header not found")
    toc_end = original.find("\n---", toc_start)
    if toc_end == -1:
        raise RuntimeError("Table of Contents block terminator not found")

    old_toc_block = original[toc_start:toc_end]
    toc_label_by_slug: dict[str, str] = {}
    toc_order: list[str] = []

    for line in old_toc_block.splitlines():
        line = line.strip()
        match = re.match(r"- \[(.+)\]\(#([^)]+)\)", line)
        if not match:
            continue
        label = match.group(1)
        slug = match.group(2)
        if slug == "general-api-usage-guide":
            continue
        toc_label_by_slug[slug] = label
        toc_order.append(slug)

    final_order = [slug for slug in toc_order if slug in categories]
    insert_after(
        final_order,
        "development",
        [
            "continuous-integration",
            "text-analysis-nlp",
            "iot-smart-devices",
            "open-source-projects",
        ],
    )
    insert_after(final_order, "email-sms", ["phone-telephony"])
    insert_after(
        final_order,
        "entertainment",
        ["events", "podcasts", "personality-quotes"],
    )
    insert_after(final_order, "finance", ["currency-exchange"])
    insert_after(final_order, "security-validation", ["data-validation"])
    insert_after(final_order, "utilities-tools", ["url-shorteners"])
    insert_after(final_order, "transportation", ["tracking-logistics"])

    for slug in categories:
        if slug not in final_order:
            final_order.append(slug)

    toc_lines = [
        "## 📖 Table of Contents",
        "",
        "- [📘 General Usage Guide](#general-api-usage-guide)",
    ]
    for slug in final_order:
        label = toc_label_by_slug.get(slug)
        if not label:
            label = str(categories[slug]["title"])
        toc_lines.append(f"- [{label}](#{slug})")
    toc_block = "\n".join(toc_lines) + "\n"

    sections: list[str] = []
    for slug in final_order:
        title = str(categories[slug]["title"])
        rows = categories[slug]["rows"]
        if not isinstance(rows, list):
            rows = []
        section_lines = [
            f'## <a id="{slug}"></a>{title}',
            "",
            *TABLE_HEADER,
            *rows,
            "",
            "[⬆ Back to Table of Contents](#-table-of-contents)",
            "",
        ]
        sections.append("\n".join(section_lines))

    categories_block = "\n".join(sections).rstrip() + "\n"

    pre_categories = original[:first_category_start]
    toc_in_pre_start = pre_categories.find("## 📖 Table of Contents")
    if toc_in_pre_start == -1:
        raise RuntimeError("Table of Contents not found before categories")
    toc_in_pre_end = pre_categories.find("\n---", toc_in_pre_start)
    if toc_in_pre_end == -1:
        raise RuntimeError("Table of Contents separator not found before categories")

    pre_categories = (
        pre_categories[:toc_in_pre_start] + toc_block + pre_categories[toc_in_pre_end:]
    )

    post_categories = original[last_category_end:]
    updated = pre_categories + categories_block + post_categories

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    api_count = len(re.findall(r"\|\s*\*\*.+?\*\*\s*\|", updated))
    category_count = len(final_order)

    print(f"Moved APIs: {len(moved)}")
    print(f"Added APIs: {added_count}")
    print(f"Skipped duplicate new APIs: {skipped_added}")
    print(f"Missing move specs: {len(missing_moves)}")
    if missing_moves:
        print("Missing move entries:")
        for source_slug, api_name, target_slug in missing_moves:
            print(f"  - {api_name} ({source_slug} -> {target_slug})")
    print(f"Final API count: {api_count}")
    print(f"Final category count: {category_count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
