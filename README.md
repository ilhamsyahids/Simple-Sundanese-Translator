# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Ilham yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Ilham punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Prerequisite
Make sure you have installed:
1. [node js](https://nodejs.org/en/)
2. [npm](https://www.npmjs.com/get-npm)
3. [flask](https://pypi.org/project/Flask/)

## Dependency
Client dependency in `app/package.json`
<br>
Server dependency `flask` and `flask_cors`

## How To Use
In this directory (root), run:
1. Client:
```
npm run client
```
2. Server:
```
npm run server
```
Alternative:
```
$ cd server
$ virtualenv flask
$ flask/bin/pip install flask flask_cors
$ chmod a+x server.py
$ ./server.py
```

## Test Case
```
Sunda - Indonesia
Sunda : nami abdi Ilham
Indonesia : nama saya Ilham
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Ilham
Sunda : nami abdi Ilham
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Video
[Youtube Link](https://youtu.be/i7GNqEHPvXI)

## Note
1. This program work fluenty and tested in Mac OS. It should be well in Windows and Linux.
2. Not all text can be translated.
