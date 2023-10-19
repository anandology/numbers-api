# Numbers API

Simple API to work with numbers. Created to use an example of teaching how to work with APIs.

## The API

### Add

```
$ curl 'https://numbers.apps.pipal.in/add?a=3&b=4'
7
```

### Fibs

The Fibs API generates a sequence of fibbonacci numbers.

The response is plain text.

**HTTP Method**

GET

**Endpoint**

`/fibs`

**Query Parameters**

| Name | Type | Default Value | Description |
| -----|------| ------------- |-------------|
| a | int | 1  | The first number of the fibonacci sequence |
| b | int | 1  | The second numner of the fibbonacci sequence |
| b | int | 1  | Number of fibonacci numbers to generate |


**Examples**

```
$ curl -i https://numbers.apps.pipal.in/fibs
1
1
2
3
5
8
13
21
34
55
```

### Range

Generates a sequence of numbers. The response is in JSON format.

```
$ curl \
    -H 'content-type: application/json' \
    -d '{"start": 1, "stop": 10}' \
    https://numbers.apps.pipal.in/range
{"result": [1, 2, 3, 4, 5, 6, 7, 8, 9]}

$ curl \
    -H 'content-type: application/json' \
    -d '{"start": 1, "stop": 10, "step": 2}' \
    https://numbers.apps.pipal.in/range
{"result": [1, 3, 5, 7, 9]}
```

### Product

```
$ curl \
    -H 'content-type: application/json' \
    -d '{"numbers": [5, 4, 3, 2, 1]}' \
    https://numbers.apps.pipal.in/product
{"result":120}
```

### Sort

```
$ curl \
    -H 'content-type: application/json' \
    -d '{"numbers": [5, 4, 3, 2, 1]}' \
    https://numbers.apps.pipal.in/sort
{"result":[1,2,3,4,5]}
```
