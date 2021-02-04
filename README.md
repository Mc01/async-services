# Async Challenge

Contains the services from:
- Ania
- Janek
- Magda
- Michal

## Setup

Fill in secrets
```
cp .env.template .env && nano .env
cp .env.shared.template .env.shared
```

Build
```
docker-compose up -d
```

Run
```
make run
```

## Example

Example output for 4.02
```
***  Config  ***

  Services: ['0', '1', '2', '3']
  Async mode in services: True
  Keywords sample: 2
  Attempts: 1
---  ---  ---

***  Results  ***

>>>  Service Ania <<<
  Attempt 0 - Keyword how to make sushi: https://async-memes.s3-eu-central-1.amazonaws.com/meme-986-2021-02-04-145421.png
  Attempt 0 - Keyword banana split: https://async-memes.s3-eu-central-1.amazonaws.com/meme-951-2021-02-04-145421.png
---  ---  ---

>>>  Service Janek <<<
  Attempt 0 - Keyword how to make sushi: {}
  Attempt 0 - Keyword banana split: {}
---  ---  ---

>>>  Service Magda <<<
  Attempt 0 - Keyword how to make sushi: http://magda-async:8000/static/images/1612450492_mbUDT0qvCEgTVRkG.jpeg
  Attempt 0 - Keyword banana split: http://magda-async:8000/static/images/1612450498_ANPNofZZJjj685Tw.jpeg
---  ---  ---

>>>  Service Michal <<<
  Attempt 0 - Keyword how to make sushi: who to make sushi
  Attempt 0 - Keyword banana split: banana spilt
---  ---  ---

***  Times  ***

>>>  Service Ania <<<
  Attempt 0 - Time 18.3350175
  :::  Min 18.3350175 Avg 18.3350175 Max 18.3350175
---  ---  ---

>>>  Service Janek <<<
  Attempt 0 - Time 0.0123578
  :::  Min 0.0123578 Avg 0.0123578 Max 0.0123578
---  ---  ---

>>>  Service Magda <<<
  Attempt 0 - Time 19.0046094
  :::  Min 19.0046094 Avg 19.0046094 Max 19.0046094
---  ---  ---

>>>  Service Michal <<<
  Attempt 0 - Time 0.7962074
  :::  Min 0.7962074 Avg 0.7962074 Max 0.7962074
---  ---  ---

***  ***  ***
```
