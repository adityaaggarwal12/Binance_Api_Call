#include <stdio.h>
#include<json-c/json.h>

#define ll long long
#define mod 1000000007
#define MAXN 100001

int main() {
    FILE *fp;
    char res[1024];

    

    struct json_object *parsed_json;
    struct json_object *symbol;
    struct json_object *price;

    fp = fopen("./resData.json","r");
    fread(res, 1024, 1, fp);
    fclose(fp);

    parsed_json = json_tokener_parse(res);
    json_object_object_get_ex(parsed_json, "symbol", &symbol);
    json_object_object_get_ex(parsed_json, "price", &price);

    printf("Symbol: %s\n", json_object_get_string(symbol));
    printf("Price: %s\n", json_object_get_string(price));

    
    return 0;
}