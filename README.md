# passphrase

Simple passphrase generator apropos http://xkcd.com/936/. Selects 12 random words from the configured dictionary. 

Here are some of my favorite example passphrases:

* mason's Hobbit barrets
* zamboni Bygone udders
* Advertisers dick dishonesty
* rheumiest Orphan cannonball
* bookworms Bullshit prognosis
* Oz's medicine storehouse
* dual Arabian iotas
* Windsor's armchair Typists

## Installation

```pip install passphrase``` or ```easy_install passphrase```

## Usage

Basic usage:

```
$ passphrase
brain dandy deserve foundation house identified insisted iran paris regiment truly villagers
```

Specify the number of results:

```
$ passphrase -n 3
chair charley slept
```

Specify a language other than English (en):

```
$ passphrase -l fr
anniversaire caméras chan foie foutez nazi organisé pluie ray revue stewart tonne
```

See available languages:

```
$ passphrase -L
ar bg cs da de el en es et fa fi fr he hr hu id it lt lv mk nl no pl pt pt_br ru sk sl sq sr-Cyrl sr-Latn sv tr ur zh
```


