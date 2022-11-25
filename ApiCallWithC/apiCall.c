#include<stdio.h>
#include<string.h>
#include<curl/curl.h>



int main(){
    FILE *fp;
    CURL *curl;
    CURLcode res;
    char url[99];
    curl = curl_easy_init();
    fp = fopen("./resData.json","w");

    if(curl){
        strcpy(url,"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT");

	    curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        // curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, true);

	    res = curl_easy_perform(curl);
        if(res != CURLE_OK){
            fprintf(stderr, "Request Failed: %s \n", curl_easy_strerror(res));
        }else{  
            printf("\nResult of Operation:: %d\n", res);
        }
        curl_easy_cleanup(curl);        
    }
    return 0;
}