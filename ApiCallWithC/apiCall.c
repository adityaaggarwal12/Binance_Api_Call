#include<stdio.h>
#include<string.h>
#include<curl/curl.h>

int main(){
    // FILE *fp;
    CURL *curl;
    CURLcode res;
    char url[99];
    curl = curl_easy_init();
    if(curl){
        strcpy(url,"https://api.binance.com/api/v3/exchangeInfo?symbols=[\"BTCUSDT\"]");

	    curl_easy_setopt(curl, CURLOPT_URL, url);
	    res = curl_easy_perform(curl);
        if(res != CURLE_OK){
            fprintf(stderr, "Request Failed: %s \n", curl_easy_strerror(res));
        }else{  
            printf("\nResult of Operation:: %d\n", res["symbols"]);
        }
        curl_easy_cleanup(curl);
    }
    return 0;
}