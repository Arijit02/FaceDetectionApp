package com.arijit.androiduploadpythonclient.Retrofit;

import retrofit2.Retrofit;
import retrofit2.converter.scalars.ScalarsConverterFactory;

public class RetroFitClient {
    private static Retrofit retroFitClient = null;

    public static Retrofit getClient(){

        if (retroFitClient == null){
            retroFitClient = new Retrofit.Builder()
                    .baseUrl("http://10.0.2.2:5000")
                    .addConverterFactory(ScalarsConverterFactory.create())
                    .build();
        }
        return retroFitClient;
    }
}
