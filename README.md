# Numbers API

Simple API to work with numbers. Created to use an example of teaching how to work with APIs.

## The API

### Fibs

The Fibs API generates a sequence of fibbonacci numbers.

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