# To execute run

### In apiCall.c
```
gcc apiCall.c -lcurl -o a.out
```

```
./a.out
```
### Now a resData.json file will be made, To parse/deserialize it -

### In jsonParse.c

##### dependencies -
```
json-c library
```

run-
```
gcc apiCall.c -ljson-c -o b.out
```

```
./b.out
```
